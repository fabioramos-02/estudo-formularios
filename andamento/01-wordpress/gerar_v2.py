"""Gera xforms-v2.json a partir de xforms-v1-demo.json (versão no ar no demo-aws).

Rodar: python gerar_v2.py
"""
import copy
import json
from pathlib import Path

PASTA = Path(__file__).resolve().parent
v1 = json.loads((PASTA / "xforms-v1-demo.json").read_text(encoding="utf-8"))
v2 = copy.deepcopy(v1)
pag = {p["name"]: p for p in v2["pages"]}

CPF_REGEX = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CORRECOES = {
    "FERTEL – Rede Eduvativa MS (SEGOV)": "FERTEL – Rede Educativa MS (SEGOV)",
    "Subsecretaria de Poíticas Públicas para Promoção da Igualdade Racial (SEC)":
        "Subsecretaria de Políticas Públicas para Promoção da Igualdade Racial (SEC)",
}
DICAS = {
    "telefone": "Para falar sobre o pedido, se precisar.",
}


def ajustar_pessoa(pagina, cond=None):
    """Campos de uma pessoa (gestor, colaborador, responsável)."""
    for e in pagina["elements"]:
        base = e["name"].rsplit("_", 1)[0]
        if base == "cpf":
            e["validators"] = [{"type": "regex", "regex": CPF_REGEX,
                                "text": "Digite um CPF com 11 números."}]
        if base in DICAS:
            e["tooltip"] = DICAS[base]
        if e["type"] == "dropdown":
            # busca já vem ligada (padrão do SurveyJS 1.12; o Designer não grava searchEnabled)
            # digitação óbvia e item repetido idêntico (SETRAT aparecia 2x)
            fix = [CORRECOES.get(c, c) for c in e["choices"]]
            e["choices"] = list(dict.fromkeys(fix))
        # setor depende do órgão: obrigatório só quando aparece
        if base == "setor":
            e.pop("isRequired", None)
            e["requiredIf"] = e["visibleIf"]
        if cond:  # campo some quando a resposta torna o bloco desnecessário
            e["visibleIf"] = f"({e['visibleIf']}) and {cond}" if e.get("visibleIf") else cond
            if e.pop("isRequired", None):
                e["requiredIf"] = e["visibleIf"]
            elif base == "setor":
                e["requiredIf"] = e["visibleIf"]


def aviso_seus_dados(perfil):
    return {"type": "html", "name": f"aviso_seus_dados_{perfil}",
            "visibleIf": f"{{perfil_solicitante}} = '{perfil}'",
            "html": "<p><strong>Estes são os seus dados.</strong></p>"}


# Título e apresentação
v2["title"] = "Solicitar acesso ao WordPress"
v2["description"] = ("Para servidores que precisam publicar ou editar um site do Governo de MS. "
                     "Tenha em mãos os dados do gestor do setor e de quem vai usar o acesso.")

# Perfil: botões de opção no lugar de imagens (GOV.UK radios; 39 KB de SVG a menos)
perfil = pag["perfil"]["elements"][0]
perfil["type"] = "radiogroup"
for c in perfil["choices"]:
    c.pop("imageLink", None)

# Sites: o gestor pode cuidar de mais de um. Lista com uma linha por site no lugar de nome + endereço.
# Chega no webhook como answers.sites = [{nome_site, url_site}, ...]
site = pag["site"]
site["title"] = "Sobre os sites"
inicio = [i for i, e in enumerate(site["elements"]) if e["name"] in ("nome_site", "url_site")]
site["elements"][inicio[0]:inicio[-1] + 1] = [{
    "type": "matrixdynamic", "name": "sites",
    "title": "Para quais sites é o acesso?",
    # o portal não aplica validador de coluna nem mostra o erro da célula: a regra vai no texto (testado 27/10/2026)
    "description": "Uma linha para cada site, com o endereço completo (https://…). "
                   "Use \"Adicionar outro site\" se for mais de um.",
    "tooltip": "Se você é gestor de mais de um site, coloque todos aqui. O tipo de acesso escolhido abaixo "
               "vale para todos os sites da lista.",
    "isRequired": True,
    "requiredErrorText": "Preencha o nome e o endereço de cada site. Se sobrou uma linha vazia, clique em Remover.",
    "rowCount": 1, "minRowCount": 1, "maxRowCount": 10,
    "addRowText": "Adicionar outro site", "removeRowText": "Remover",
    "columns": [
        {"name": "nome_site", "title": "Nome do site", "cellType": "text", "isRequired": True,
         "requiredErrorText": "Preencha o nome do site."},
        {"name": "url_site", "title": "Endereço do site", "cellType": "text", "isRequired": True,
         "placeholder": "https://exemplo.ms.gov.br",
         "requiredErrorText": "Digite o endereço completo, começando com https://",
         "validators": [{"type": "regex", "regex": r"^https?://\S+\.\S+$",
                         "text": "Digite o endereço completo, começando com https://"}]},
    ],
}]

# Permissão: escolha única (C4) com o que cada papel faz
for e in pag["site"]["elements"]:
    if e["name"] == "permissao_acesso":
        e.update({
            "type": "radiogroup",
            "title": "Que tipo de acesso a pessoa precisa?",
            "requiredErrorText": "Escolha um tipo de acesso para continuar.",
            "choices": [
                {"value": "assinante", "text": "Assinante: só lê o conteúdo"},
                {"value": "colaborador", "text": "Colaborador: escreve, mas não publica"},
                {"value": "autor", "text": "Autor: escreve e publica os próprios textos"},
                {"value": "editor", "text": "Editor: publica e edita os textos de todos"},
            ],
        })
        e.pop("maxSelectedChoices", None)
        e.pop("minSelectedChoices", None)
        e["tooltip"] = "São os papéis do WordPress. Peça o menor acesso que resolve o trabalho."

ajustar_pessoa(pag["dados_gestor"])
ajustar_pessoa(pag["dados_colaborador"])
# O portal preenche nome e e-mail com a conta em todo campo com autocomplete.
# Só vale para quem está preenchendo: limpa o bloco da outra pessoa (testado na prévia).
for pagina, outro in (("dados_gestor", "colaborador"), ("dados_colaborador", "gestor")):
    for e in pag[pagina]["elements"]:
        if e.get("autocomplete") in ("name", "email"):
            e["resetValueIf"] = f"{{perfil_solicitante}} = '{outro}'"
v2["showQuestionNumbers"] = "off"  # pergunta condicional pula número
pag["dados_gestor"]["elements"].insert(0, aviso_seus_dados("gestor"))
pag["dados_colaborador"]["elements"].insert(0, aviso_seus_dados("colaborador"))
for e in pag["dados_colaborador"]["elements"]:
    if e["name"] == "email_colaborador":
        e["tooltip"] = "É o e-mail de quem vai usar o acesso."

# Responsável: não repetir quando é o próprio gestor (C3)
resp = pag["dados_responsavel"]
resp["description"] = "Quem responde pelo conteúdo do site no órgão."
ajustar_pessoa(resp, cond="{responsavel_e_gestor} = false")
for e in resp["elements"]:
    e.pop("autocomplete", None)  # é outra pessoa: não preencher com a conta
resp["elements"].insert(0, {
    "type": "boolean", "name": "responsavel_e_gestor",
    "title": "O responsável pelo site é o gestor que você informou?",
    "labelTrue": "Sim", "labelFalse": "Não",
    "tooltip": "Se for, não precisa digitar os dados de novo.",
})
# O que acontece depois (B6): completedHtml não aparece no portal
resp["elements"].append({
    "type": "html", "name": "aviso_proximos_passos",
    "html": ("<p><strong>Depois do envio:</strong> a SETDIG analisa o pedido "
             "e a resposta chega no e-mail informado.</p>"),
})

(PASTA / "xforms-v2.json").write_text(json.dumps(v2, ensure_ascii=False, indent=2), encoding="utf-8")

# Checagem mínima
nomes = [e["name"] for p in v2["pages"] for e in p["elements"]]
assert len(nomes) == len(set(nomes)), "name repetido"
assert not any(e.get("isRequired") and e.get("visibleIf") for p in v2["pages"] for e in p["elements"]), \
    "obrigatório em campo que pode ficar escondido"
print(f"ok: {len(v2['pages'])} páginas, {len(nomes)} elementos")
