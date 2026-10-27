"""Gera fluxo.json (X-Flows) do cadastro de laboratório de sanidade avícola (IAGRO): webhook → CODE → Tables (cadastros_laboratorio_avicola).

Telefone, CEP e endereço completo ficam só nas respostas do X-Forms (LGPD art. 6º III).
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const tipos = { cadastro: 'Cadastro novo', atualizacao: 'Atualização' };
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    tipoPedido: tipos[a.tipo_pedido] ?? '',
    nome: a.nome_completo ?? '',
    razaoSocial: a.razao_social ?? '',
    nomeFantasia: a.nome_fantasia ?? '',
    cnpj: a.cnpj ?? '',
    inscricaoEstadual: a.inscricao_estadual ?? '',
    emailLaboratorio: a.email_laboratorio ?? '',
    escopo: a.escopo_analises ?? '',
    credenciadoMapa: a.credenciado_mapa === 'sim' ? 'Sim' : 'Não',
    portariaCredenciamento: a.numero_portaria_credenciamento ?? '',
    crl: a.numero_crl ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "tipo_pedido": "tipoPedido", "nome": "nome", "razao_social": "razaoSocial", "nome_fantasia": "nomeFantasia",
    "cnpj": "cnpj", "inscricao_estadual": "inscricaoEstadual", "email_laboratorio": "emailLaboratorio",
    "escopo": "escopo", "credenciado_mapa": "credenciadoMapa", "portaria_credenciamento": "portariaCredenciamento",
    "crl": "crl", "municipio": "municipio", "uf": "uf", "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastrar laboratório de sanidade avícola IAGRO", "LAB", "cadastros_laboratorio_avicola", CORPO, COLUNAS)
