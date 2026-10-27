"""Gera fluxo.json (X-Flows) da Fundect: webhook → CODE → Tables (solicitacoes_diarias_fundect).

Dados bancários do estagiário ficam só nas respostas do X-Forms (LGPD art. 6º III).
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const tipos = { diarias: 'Diárias', passagens: 'Passagens', ambos: 'Diárias e passagens' };
  const arquivo = Array.isArray(a.arquivo_documento_pessoal) ? a.arquivo_documento_pessoal[0]?.name : '';
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    vinculo: a.vinculo === 'estagiario' ? 'Estagiário' : 'Servidor',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    matricula: a.matricula ?? '',
    tipo: tipos[a.tipo_solicitacao] ?? '',
    origem: a.cidade_origem ?? '',
    destino: a.cidade_destino ?? '',
    dataIda: a.data_saida ?? '',
    dataVolta: a.data_retorno ?? '',
    objetivo: a.objetivo_viagem ?? '',
    veiculo: a.veiculo_utilizado ?? '',
    documento: arquivo ?? '',
    dadosBancarios: a.vinculo === 'estagiario' ? 'Nas respostas do X-Forms' : 'No sistema de RH',
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "vinculo": "vinculo", "nome": "nome", "email": "email", "matricula": "matricula",
    "tipo": "tipo", "origem": "origem", "destino": "destino",
    "data_ida": "dataIda", "data_volta": "dataVolta", "objetivo": "objetivo",
    "veiculo": "veiculo", "documento": "documento", "dados_bancarios": "dadosBancarios",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: diárias e passagens Fundect", "FUN", "solicitacoes_diarias_fundect", CORPO, COLUNAS)
