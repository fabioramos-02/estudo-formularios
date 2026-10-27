"""Gera fluxo.json (X-Flows) do pedido de certidão negativa de tombamento (FCMS): webhook → CODE → Tables (pedidos_negativa_tombamento).

CPF do solicitante e do proprietário ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const nomeArquivo = (v) => (Array.isArray(v) ? v.map((f) => f?.name).filter(Boolean).join(', ') : '');
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    perfil: a.perfil_solicitante === 'representante' ? 'Representante do proprietário' : 'Proprietário',
    imovel: a.identificacao_imovel ?? '',
    certidaoMatricula: nomeArquivo(a.arquivo_certidao_matricula),
    documentoRequerente: nomeArquivo(a.arquivo_documento_requerente),
    documentoProprietario: nomeArquivo(a.arquivo_documento_proprietario),
    procuracao: nomeArquivo(a.arquivo_procuracao),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "perfil": "perfil", "imovel": "imovel",
    "certidao_matricula": "certidaoMatricula", "documento_requerente": "documentoRequerente",
    "documento_proprietario": "documentoProprietario", "procuracao": "procuracao",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: certidão negativa de tombamento FCMS", "TOM", "pedidos_negativa_tombamento", CORPO, COLUNAS)
