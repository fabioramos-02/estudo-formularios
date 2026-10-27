"""Gera fluxo.json (X-Flows) do cadastro de indústria de agrotóxicos (IAGRO): webhook → CODE → Tables (cadastros_industria_agrotoxicos).

Celular e endereço completo ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
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
    perfil: a.perfil_solicitante === 'consultoria' ? 'Consultoria' : 'Própria indústria',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    cnpj: a.cnpj ?? '',
    razaoSocial: a.razao_social ?? '',
    representante: a.nome_representante_legal ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    cartaoCnpj: nomeArquivo(a.arquivo_cartao_cnpj),
    contratoSocial: nomeArquivo(a.arquivo_contrato_social),
    procuracao: nomeArquivo(a.arquivo_procuracao),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "perfil": "perfil", "nome": "nome", "email": "email", "cnpj": "cnpj",
    "razao_social": "razaoSocial", "representante_legal": "representante",
    "municipio": "municipio", "uf": "uf", "cartao_cnpj": "cartaoCnpj",
    "contrato_social": "contratoSocial", "procuracao": "procuracao",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastro de indústria de agrotóxicos IAGRO", "AGI", "cadastros_industria_agrotoxicos", CORPO, COLUNAS)
