"""Gera fluxo.json (X-Flows) da certidão de atendimento de emergência 190/193 (SEJUSP): webhook → CODE → Tables (pedidos_certidao_emergencia).

CPF, data de nascimento, celular, endereços e o relato ficam só nas respostas do X-Forms (LGPD art. 6º III).
A tabela guarda a cidade do fato, que serve para achar a ligação. Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const perfis = {
    proprio: 'Quem fez a ligação',
    representante_legal: 'Representante legal',
    procurador: 'Procurador',
  };
  const numeros = { '190': '190 (Polícia Militar)', '193': '193 (Corpo de Bombeiros)' };
  const nomeArquivo = (v) => (Array.isArray(v) ? v[0]?.name : '') ?? '';
  const nomeArquivos = (v) => (Array.isArray(v) ? v.map((f) => f?.name).filter(Boolean).join('; ') : '');
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    nome: a.nome_completo || a.nome_completo_ligou || '',
    email: a.email ?? '',
    perfil: perfis[a.perfil_solicitante] ?? '',
    nomeLigou: a.nome_completo_ligou ?? '',
    numeroEmergencia: numeros[a.numero_emergencia] ?? '',
    municipioOcorrencia: a.municipio_ocorrencia ?? '',
    dataFato: a.data_fato ?? '',
    horaFato: a.hora_fato ?? '',
    finalidade: a.finalidade_certidao ?? '',
    documentoIdentificacao: nomeArquivo(a.arquivo_documento_identificacao),
    documentoRepresentante: nomeArquivo(a.arquivo_documento_representante),
    procuracao: nomeArquivo(a.arquivo_procuracao),
    outrosDocumentos: nomeArquivos(a.arquivo_outros_documentos),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "nome": "nome", "email": "email", "perfil": "perfil", "nome_ligou": "nomeLigou",
    "numero_emergencia": "numeroEmergencia", "municipio_ocorrencia": "municipioOcorrencia",
    "data_fato": "dataFato", "hora_fato": "horaFato", "finalidade": "finalidade",
    "documento_identificacao": "documentoIdentificacao", "documento_representante": "documentoRepresentante",
    "procuracao": "procuracao", "outros_documentos": "outrosDocumentos",
    "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: certidão de atendimento 190/193 SEJUSP", "CER", "pedidos_certidao_emergencia", CORPO, COLUNAS)
