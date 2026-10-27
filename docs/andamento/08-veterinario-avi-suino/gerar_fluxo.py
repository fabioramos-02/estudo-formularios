"""Gera fluxo.json (X-Flows) do cadastro de médico veterinário de aves e suínos (IAGRO): webhook → CODE → Tables (cadastros_veterinario_avi_suino).

CPF, telefones e endereço completo ficam só nas respostas do X-Forms (LGPD art. 6º III). Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const tipos = { cadastro: 'Cadastro novo', atualizacao: 'Atualização' };
  const nomesArquivos = (v) => (Array.isArray(v) ? v.map((f) => f?.name).filter(Boolean).join('; ') : '');
  const vinculada = a.empresa_vinculada === 'sim';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    tipoPedido: tipos[a.tipo_pedido] ?? '',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    crmv: a.numero_crmv ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    empresaVinculada: vinculada ? 'Sim' : 'Não',
    cnpjEmpresa: a.cnpj_empresa ?? '',
    empresa: a.razao_social_empresa ?? '',
    portariaMapa: a.numero_portaria_mapa ?? '',
    comprovanteVinculo: nomesArquivos(a.arquivo_vinculo_empresa),
    arquivoPortariaMapa: nomesArquivos(a.arquivo_portaria_mapa),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "tipo_pedido": "tipoPedido", "nome": "nome", "email": "email", "crmv": "crmv",
    "municipio": "municipio", "uf": "uf", "empresa_vinculada": "empresaVinculada",
    "cnpj_empresa": "cnpjEmpresa", "empresa": "empresa", "portaria_mapa": "portariaMapa",
    "comprovante_vinculo": "comprovanteVinculo", "arquivo_portaria_mapa": "arquivoPortariaMapa",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastrar veterinário de aves e suínos IAGRO", "VET", "cadastros_veterinario_avi_suino", CORPO, COLUNAS)
