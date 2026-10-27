"""Gera resposta-teste.json (answers fictícios) a partir do xforms-v2.json de cada pasta.

Segue a primeira opção de cada escolha e só responde o que fica visível, como o portal faz.
Uso: python resposta_teste.py 06-selo-arte 07-negativa-tombamento ...
"""
import json
import re
import sys
from pathlib import Path

PDF = "data:application/pdf;base64,JVBERi0xLjQKMSAwIG9iajw8L1R5cGUvQ2F0YWxvZy9QYWdlcyAyIDAgUj4+ZW5kb2JqCiUlRU9GCg=="
ARQUIVO = [{"name": "teste-anexo.pdf", "type": "application/pdf", "content": PDF}]


def avalia(expr, r):
    # ponytail: só os padrões usados nos 14 (=, <>, >, notempty, and, or); outro padrão quebra o assert
    py = re.sub(r"\{([\w.-]+)\}\s+notempty", lambda m: f"bool(r.get({m.group(1)!r}))", expr)
    py = re.sub(r"\{([\w.-]+)\}", lambda m: f"r.get({m.group(1)!r})", py)
    py = py.replace("<>", "!=").replace(" = ", " == ")
    assert re.fullmatch(r"[\w\s.'()!=<>,\-À-ú]*", py), expr
    try:
        return bool(eval(py, {}, {"r": r}))
    except TypeError:  # comparação com None (ex.: {x} > 0 sem resposta)
        return False


def valor(e):
    t, it, nome = e["type"], e.get("inputType"), e["name"]
    if t in ("radiogroup", "dropdown"):
        c = e["choices"][0]
        return c["value"] if isinstance(c, dict) else c
    if t == "checkbox":
        c = e["choices"][0]
        return [c["value"] if isinstance(c, dict) else c]
    if t == "boolean":
        return True
    if t == "file":
        return ARQUIVO
    if t == "multipletext":
        return {i["name"]: "(67) 99999-0000" for i in e["items"]}
    if t == "comment":
        return "Texto de teste do estudo de formulários da SETDIG."
    if it == "date":
        return "2026-10-01"
    if it == "time":
        return "10:00"
    if it == "email" or "email" in nome:
        return "teste.setdig@exemplo.com.br"
    padrao = e.get("maskSettings", {}).get("pattern", "")
    if padrao:
        return re.sub(r"9", lambda _: "1", padrao) if "cpf" not in nome else "529.982.247-25"
    if nome.startswith("nome"):
        return "Pessoa Teste SETDIG"
    return "Teste"


def gera(pasta):
    form = json.loads((Path(pasta) / "xforms-v2.json").read_text(encoding="utf-8"))
    r = {}
    for p in form["pages"]:
        if p.get("visibleIf") and not avalia(p["visibleIf"], r):
            continue
        for e in p["elements"]:
            if e["type"] in ("html", "expression") or (e.get("visibleIf") and not avalia(e["visibleIf"], r)):
                continue
            r[e["name"]] = valor(e)
    (Path(pasta) / "resposta-teste.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return r


if __name__ == "__main__":
    for pasta in sys.argv[1:]:
        print(pasta, len(gera(pasta)), "respostas")
