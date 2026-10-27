"""Gera fluxo.json (X-Flows) do certificado de destruição de soqueira de algodão (IAGRO): webhook → CODE → Tables (pedidos_certificado_soqueira).

CPF e celular ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const areas = {
    ate_50_hectares: 'Até 50 hectares',
    acima_50_hectares: 'Mais de 50 hectares',
  };
  const nomeArquivo = (v) => (Array.isArray(v) ? v[0]?.name : '') ?? '';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    areaPlantio: areas[a.area_plantio] ?? '',
    relatorioFiscalizacao: nomeArquivo(a.arquivo_relatorio_fiscalizacao),
    guiaDaems: nomeArquivo(a.arquivo_guia_daems),
    comprovantePagamento: nomeArquivo(a.arquivo_comprovante_pagamento),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "area_plantio": "areaPlantio",
    "relatorio_fiscalizacao": "relatorioFiscalizacao", "guia_daems": "guiaDaems",
    "comprovante_pagamento": "comprovantePagamento",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: certificado de destruição de soqueira de algodão IAGRO", "SOQ", "pedidos_certificado_soqueira", CORPO, COLUNAS)
