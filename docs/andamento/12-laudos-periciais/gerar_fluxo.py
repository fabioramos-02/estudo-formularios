"""Gera fluxo.json (X-Flows) do pedido de cópia de laudo pericial (CGP/SEJUSP): webhook → CODE → Tables (pedidos_copia_laudos).

CPF, data de nascimento, celular, endereço completo e o relato do fato ficam só nas respostas do X-Forms
(LGPD art. 6º III). A tabela guarda o que serve para achar o laudo e acompanhar o pedido. Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const perfis = {
    envolvido: 'Pessoa envolvida no fato',
    procurador: 'Procurador',
    familiar: 'Familiar de 1º grau de vítima que faleceu',
  };
  const tipos = {
    analises_laboratoriais: 'Análises laboratoriais',
    criminalistica: 'Criminalística',
    identificacao: 'Identificação',
    medicina_legal: 'Medicina legal',
  };
  // aceita vários arquivos por anexo (frente e verso)
  const nomeArquivo = (v) => (Array.isArray(v) ? v.map((f) => f?.name).filter(Boolean).join('; ') : '');
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo ?? '',
    email: a.email ?? '',
    perfil: perfis[a.perfil_solicitante] ?? '',
    municipio: a.municipio ?? '',
    uf: a.uf ?? '',
    nomeVitima: a.nome_vitima ?? '',
    nomeOutorgante: a.nome_outorgante ?? '',
    dataFato: a.data_fato ?? '',
    numeroOcorrencia: a.numero_ocorrencia ?? '',
    tipoLaudo: (a.tipo_laudo ?? []).map((t) => tipos[t] ?? t).join('; '),
    documentoEnvolvido: nomeArquivo(a.arquivo_documento_identificacao_envolvido),
    documentoSolicitante: nomeArquivo(a.arquivo_documento_identificacao_solicitante),
    procuracao: nomeArquivo(a.arquivo_procuracao),
    comprovanteParentesco: nomeArquivo(a.arquivo_comprovante_parentesco),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "perfil": "perfil", "municipio": "municipio", "uf": "uf",
    "nome_vitima": "nomeVitima", "nome_outorgante": "nomeOutorgante", "data_fato": "dataFato",
    "numero_ocorrencia": "numeroOcorrencia", "tipo_laudo": "tipoLaudo",
    "documento_envolvido": "documentoEnvolvido", "documento_solicitante": "documentoSolicitante",
    "procuracao": "procuracao", "comprovante_parentesco": "comprovanteParentesco",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cópia de laudo pericial CGP", "LAU", "pedidos_copia_laudos", CORPO, COLUNAS)
