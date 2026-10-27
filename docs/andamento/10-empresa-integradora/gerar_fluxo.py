"""Gera fluxo.json (X-Flows) do cadastro de empresa integradora de aves ou suínos (IAGRO): webhook → CODE → Tables (cadastros_empresa_integradora).

Telefones, CEP e coordenada ficam só nas respostas do X-Forms (LGPD art. 6º III).
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const tipos = { cadastro: 'Cadastro novo', atualizacao: 'Atualização' };
  const atividades = { avicultura: 'Avicultura', suinocultura: 'Suinocultura' };
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    tipoPedido: tipos[a.tipo_pedido] ?? '',
    representante: a.nome_representante_legal ?? '',
    emailRepresentante: a.email_representante ?? '',
    razaoSocial: a.razao_social ?? '',
    nomeFantasia: a.nome_fantasia ?? '',
    cnpj: a.cnpj ?? '',
    inscricaoEstadual: a.inscricao_estadual ?? '',
    atividade: atividades[a.atividade_integradora] ?? '',
    emailEmpresa: a.email_empresa ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "tipo_pedido": "tipoPedido", "representante": "representante", "email_representante": "emailRepresentante",
    "razao_social": "razaoSocial", "nome_fantasia": "nomeFantasia", "cnpj": "cnpj",
    "inscricao_estadual": "inscricaoEstadual", "atividade": "atividade", "email_empresa": "emailEmpresa",
    "municipio": "municipio", "uf": "uf", "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastrar empresa integradora de aves ou suínos IAGRO", "INT", "cadastros_empresa_integradora", CORPO, COLUNAS)
