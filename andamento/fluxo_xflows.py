"""Monta fluxo do X-Flows (webhook → CODE → Tables) a partir do fluxo de exemplo do Leonardo.

Usado pelo gerar_fluxo.py de cada formulário em docs/andamento/<NN>-<slug>/.
"""
import copy
import json
import re
from pathlib import Path

MOLDE = Path(__file__).resolve().parents[2] / ".claude/referencia/activepieces-precadastro-familiar.json"

# Protocolo com a data de MS (UTC-4), para não virar o dia depois das 20h.
# ponytail: aleatório como no exemplo; trocar pelo protocolo da API de Tramitação quando houver
CABECALHO = """export const code = async (inputs) => {
  const { answers = {}, serviceSlug, submittedAt, userId } = inputs.dados ?? {};
  const a = answers;
  const recebidoEm = submittedAt ?? new Date().toISOString();
  const dataMS = new Date(new Date(recebidoEm).getTime() - 4 * 3600 * 1000).toISOString().slice(0, 10).replace(/-/g, '');
  const protocolo = '%s-' + dataMS + '-' + Math.random().toString(36).slice(2, 8).toUpperCase();
"""


ROTULOS = {
    "protocolo": "Protocolo", "recebido_em": "Recebido em", "situacao": "Situação", "nome": "Nome",
    "email": "E-mail", "cnpj": "CNPJ", "razao_social": "Razão social", "municipio": "Município", "uf": "UF",
    "servico": "Serviço (serviceSlug)", "usuario": "Usuário (sub)",
}


def montar(pasta, nome, prefixo, tabela, corpo, colunas, tipos=None, rotulos=None):
    """corpo: JS que termina em `return {...}` usando `a` (answers) e protocolo/recebidoEm/serviceSlug/userId.
    colunas: {externalId da coluna: chave do return}. Grava fluxo.json e tabela.json (para criar a tabela
    no X-Flows) e confere o contrato com xforms-v2.json."""
    pasta = Path(pasta)
    codigo = CABECALHO % prefixo + corpo + "\n};"
    tipos = {"recebido_em": "DATE_TIME", **(tipos or {})}

    molde = json.loads(MOLDE.read_text(encoding="utf-8-sig"))["flows"][0]
    trigger = copy.deepcopy(molde["trigger"])
    trigger["displayName"] = "Recebe a resposta do X-Forms"
    code = trigger["nextAction"]
    code["displayName"] = "Gera protocolo e organiza o pedido"
    code["settings"]["sourceCode"]["code"] = codigo
    tab = code["nextAction"]
    tab["displayName"] = "Registra o pedido na tabela"
    tab["settings"]["input"] = {
        "table_id": tabela,
        "values": {"values": [{c: f"{{{{step_1.{s}}}}}" for c, s in colunas.items()}]},
    }
    tab["settings"]["propertySettings"]["values"]["schema"]["values"]["properties"] = {
        c: {"type": tipos.get(c, "SHORT_TEXT"), "required": False, "displayName": c} for c in colunas
    }
    for passo in (trigger, code, tab):
        passo.pop("lastUpdatedDate", None)
    fluxo = {"displayName": nome, "trigger": trigger, "schemaVersion": molde["schemaVersion"]}
    (pasta / "fluxo.json").write_text(json.dumps(fluxo, ensure_ascii=False, indent=2), encoding="utf-8")
    # ponytail: rótulo padrão sem acento para colunas fora de ROTULOS; passe `rotulos` para corrigir
    rot = {**ROTULOS, **(rotulos or {})}
    campos = [[c, rot.get(c, c.replace("_", " ").capitalize()), "DATE" if tipos.get(c) == "DATE_TIME" else "TEXT"]
              for c in colunas]
    titulo = nome.removeprefix("X-Forms: ")
    (pasta / "tabela.json").write_text(json.dumps({"externalId": tabela, "nome": titulo[:1].upper() + titulo[1:],
                                                   "campos": campos}, ensure_ascii=False, indent=2), encoding="utf-8")

    # Contrato: todo campo lido em `a.` existe no formulário; toda coluna sai do return
    form = json.loads((pasta / "xforms-v2.json").read_text(encoding="utf-8"))
    nomes = {e["name"] for p in form["pages"] for e in p["elements"]}
    lidos = set(re.findall(r"\ba\.(\w+)", corpo))
    assert lidos <= nomes, f"campos fora do formulário: {lidos - nomes}"
    faltam = [s for s in colunas.values() if not re.search(rf"\b{s}\b", codigo)]
    assert not faltam, f"colunas sem valor no CODE: {faltam}"
    print(f"ok: {len(colunas)} colunas, {len(lidos)} campos do formulário lidos")
    return codigo
