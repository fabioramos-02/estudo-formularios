"""Gera fluxo-wordpress.json (X-Flows) a partir do fluxo de exemplo do Leonardo.

Webhook → CODE (protocolo e campos para a equipe) → Tables (solicitacoes_wordpress).
Sem e-mail: o X-Flows de DEV ainda não tem conexão Gmail.
Rodar: python gerar_fluxo.py
"""
import copy
import json
import re
from pathlib import Path

PASTA = Path(__file__).resolve().parent
MOLDE = PASTA.parents[2] / ".claude/referencia/activepieces-precadastro-familiar.json"

CODIGO = r"""export const code = async (inputs) => {
  const { answers = {}, serviceSlug, submittedAt, userId } = inputs.dados ?? {};
  const a = answers;
  const recebidoEm = submittedAt ?? new Date().toISOString();
  // Data de MS (UTC-4) no protocolo, para não virar o dia depois das 20h
  const dataMS = new Date(new Date(recebidoEm).getTime() - 4 * 3600 * 1000).toISOString().slice(0, 10).replace(/-/g, '');
  // ponytail: aleatório como no exemplo; trocar pelo protocolo da API de Tramitação quando houver
  const protocolo = 'WP-' + dataMS + '-' + Math.random().toString(36).slice(2, 8).toUpperCase();
  const mesmoGestor = a.responsavel_e_gestor === true;
  // sites chega como lista [{nome_site, url_site}]; a tabela guarda um site por item, separados por '; '
  const sites = Array.isArray(a.sites) ? a.sites : [];
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    perfil: a.perfil_solicitante ?? '',
    nomeSite: sites.map((s) => s.nome_site ?? '').join('; '),
    urlSite: sites.map((s) => s.url_site ?? '').join('; '),
    permissao: a.permissao_acesso ?? '',
    colaboradorNome: a.nome_colaborador ?? '',
    colaboradorEmail: a.email_colaborador ?? '',
    colaboradorLogin: a.login_rede_colaborador ?? '',
    colaboradorOrgao: a.orgao_colaborador ?? '',
    gestorNome: a.nome_gestor ?? '',
    gestorEmail: a.email_gestor ?? '',
    responsavelNome: (mesmoGestor ? a.nome_gestor : a.nome_responsavel) ?? '',
    responsavelEmail: (mesmoGestor ? a.email_gestor : a.email_responsavel) ?? '',
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };
};"""

# coluna da tabela -> saída do CODE
COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "perfil": "perfil", "nome_site": "nomeSite", "url_site": "urlSite", "permissao": "permissao",
    "colaborador_nome": "colaboradorNome", "colaborador_email": "colaboradorEmail",
    "colaborador_login": "colaboradorLogin", "colaborador_orgao": "colaboradorOrgao",
    "gestor_nome": "gestorNome", "gestor_email": "gestorEmail",
    "responsavel_nome": "responsavelNome", "responsavel_email": "responsavelEmail",
    "servico": "servico", "usuario": "usuario",
}
TIPOS = {"recebido_em": "DATE_TIME"}

molde = json.loads(MOLDE.read_text(encoding="utf-8-sig"))["flows"][0]
trigger = copy.deepcopy(molde["trigger"])
trigger["displayName"] = "Recebe a resposta do X-Forms"
code = trigger["nextAction"]
code["displayName"] = "Gera protocolo e organiza o pedido"
code["settings"]["sourceCode"]["code"] = CODIGO
tabela = code["nextAction"]
tabela["displayName"] = "Registra a solicitação na tabela"
tabela["settings"]["input"] = {
    "table_id": "solicitacoes_wordpress",
    "values": {"values": [{col: f"{{{{step_1.{saida}}}}}" for col, saida in COLUNAS.items()}]},
}
tabela["settings"]["propertySettings"]["values"]["schema"]["values"]["properties"] = {
    col: {"type": TIPOS.get(col, "SHORT_TEXT"), "required": False, "displayName": col}
    for col in COLUNAS
}
for passo in (trigger, code, tabela):
    passo.pop("lastUpdatedDate", None)

fluxo = {"displayName": "X-Forms: solicitar acesso ao WordPress", "trigger": trigger,
         "schemaVersion": molde["schemaVersion"]}
(PASTA / "fluxo-wordpress.json").write_text(json.dumps(fluxo, ensure_ascii=False, indent=2), encoding="utf-8")

# Contrato: todo answers lido no CODE existe no formulário
form = json.loads((PASTA / "xforms-v2.json").read_text(encoding="utf-8"))
nomes = {e["name"] for p in form["pages"] for e in p["elements"]}
lidos = set(re.findall(r"a\.(\w+)", CODIGO))
assert lidos <= nomes, f"campos fora do formulário: {lidos - nomes}"
print(f"ok: {len(COLUNAS)} colunas, {len(lidos)} campos do formulário lidos")
