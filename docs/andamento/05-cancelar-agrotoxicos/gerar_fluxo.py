"""Gera fluxo.json (X-Flows) do cancelamento de registro de agrotóxicos (IAGRO): webhook → CODE → Tables (cancelamentos_registro_agrotoxicos).

CPF e endereço completo ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const motivos = {
    nao_comercializa: 'Não vende agrotóxicos',
    lei_2951: 'Não vai continuar vendendo (Lei Estadual 2.951/2004)',
    nao_transporta: 'Não transporta agrotóxicos',
    nao_aplica: 'Não presta serviço de aplicação',
  };
  const nomeArquivo = (v) => (Array.isArray(v) ? v[0]?.name : '') ?? '';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    razaoSocial: a.razao_social ?? '',
    cnpj: a.cnpj ?? '',
    inscricaoEstadual: a.inscricao_estadual ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    motivo: motivos[a.motivo_cancelamento] ?? '',
    cartaoCnpj: nomeArquivo(a.arquivo_cartao_cnpj),
    guiaRecolhimento: nomeArquivo(a.arquivo_guia_recolhimento),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "razao_social": "razaoSocial", "cnpj": "cnpj",
    "inscricao_estadual": "inscricaoEstadual", "municipio": "municipio", "uf": "uf",
    "motivo": "motivo", "cartao_cnpj": "cartaoCnpj", "guia_recolhimento": "guiaRecolhimento",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cancelar registro de agrotóxicos IAGRO", "CAG", "cancelamentos_registro_agrotoxicos", CORPO, COLUNAS)
