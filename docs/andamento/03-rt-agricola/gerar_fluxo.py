"""Gera fluxo.json (X-Flows) do cadastro de RT agrícola (IAGRO): webhook → CODE → Tables (cadastros_rt_agricola).

CPF e celular ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const objetivos = { estabelecimento_insumos: 'Estabelecimentos de insumos', cultivo_soja_algodao: 'Cultivos de soja ou algodão' };
  const nomeArquivo = (v) => (Array.isArray(v) ? v[0]?.name : '') ?? '';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    objetivo: (a.objetivo_cadastro ?? []).map((o) => objetivos[o] ?? o).join('; '),
    docIdentidade: nomeArquivo(a.arquivo_documento_identidade),
    carteiraConselho: nomeArquivo(a.arquivo_carteira_conselho),
    comprovanteResidencia: nomeArquivo(a.arquivo_comprovante_residencia),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "objetivo": "objetivo",
    "doc_identidade": "docIdentidade", "carteira_conselho": "carteiraConselho",
    "comprovante_residencia": "comprovanteResidencia",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastro de RT agrícola IAGRO", "RTA", "cadastros_rt_agricola", CORPO, COLUNAS)
