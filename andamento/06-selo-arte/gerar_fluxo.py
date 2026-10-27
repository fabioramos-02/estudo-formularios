"""Gera fluxo.json (X-Flows) do pedido de Selo Arte (IAGRO): webhook → CODE → Tables (pedidos_selo_arte).

CPF e endereço completo ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexo entra pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const nomeArquivo = (v) => (Array.isArray(v) ? v[0]?.name : '') ?? '';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    estabelecimento: a.nome_estabelecimento ?? '',
    servicoInspecao: a.registro_servico_inspecao ?? '',
    numeroRegistro: a.numero_registro ?? '',
    municipio: a.municipio ?? '',
    produtos: a.produtos ?? '',
    declaracao: (a.declaracao_ciencia ?? []).includes('ciente') ? 'Aceita' : '',
    logomarca: nomeArquivo(a.arquivo_logomarca),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "estabelecimento": "estabelecimento",
    "servico_inspecao": "servicoInspecao", "numero_registro": "numeroRegistro",
    "municipio": "municipio", "produtos": "produtos", "declaracao": "declaracao",
    "logomarca": "logomarca", "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: pedido de Selo Arte IAGRO", "ART", "pedidos_selo_arte", CORPO, COLUNAS)
