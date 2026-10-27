"""Gera fluxo.json (X-Flows) do cadastro no Sistema Estadual de Bibliotecas Públicas (FCMS): webhook → CODE → Tables (cadastros_bibliotecas_publicas).

CPF, telefone e endereços completos ficam só nas respostas do X-Forms (LGPD art. 6º III); a tabela guarda o município.
Anexos entram pelo nome do arquivo.
Rodar: python gerar_fluxo.py
"""
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA.parent))
from fluxo_xflows import montar  # noqa: E402

CORPO = """  const tipos = { publica: 'Pública', comunitaria: 'Comunitária', associada: 'Associada' };
  const simNao = (v) => (v === 'sim' ? 'Sim' : v === 'nao' ? 'Não' : '');
  const nomeArquivo = (v) => (Array.isArray(v) ? v.map((f) => f?.name).filter(Boolean).join(', ') : '');
  return {
    protocolo,
    recebidoEm,
    situacao: 'Recebido',
    biblioteca: a.nome_biblioteca ?? '',
    tipo: tipos[a.tipo_biblioteca] ?? '',
    legislacao: a.legislacao_criacao ?? '',
    emFuncionamento: simNao(a.em_funcionamento),
    diagnostico: simNao(a.respondeu_diagnostico),
    responsavel: a.nome_responsavel_biblioteca ?? '',
    pessoas: String(a.numero_pessoas_trabalham ?? ''),
    acessibilidade: simNao(a.possui_acessibilidade),
    municipio: a.municipio ?? '',
    instituicao: a.nome_instituicao_vinculada ?? '',
    cnpj: a.tipo_documento_instituicao === 'cnpj' ? (a.cnpj_instituicao ?? '') : '',
    emailInstituicao: a.email_instituicao ?? '',
    arquivoLegislacao: nomeArquivo(a.arquivo_legislacao_criacao),
    fotoCapa: nomeArquivo(a.arquivo_foto_capa),
    fotoDivulgacao: nomeArquivo(a.arquivo_foto_divulgacao),
    cadastrosAnteriores: nomeArquivo(a.arquivo_cadastros_anteriores),
    servico: serviceSlug ?? '',
    usuario: userId ?? 'não informado',
  };"""

COLUNAS = {
    "protocolo": "protocolo", "recebido_em": "recebidoEm", "situacao": "situacao",
    "biblioteca": "biblioteca", "tipo": "tipo", "legislacao_criacao": "legislacao",
    "em_funcionamento": "emFuncionamento", "respondeu_diagnostico": "diagnostico",
    "responsavel": "responsavel", "pessoas_trabalham": "pessoas", "acessibilidade": "acessibilidade",
    "municipio": "municipio", "instituicao": "instituicao", "cnpj_instituicao": "cnpj",
    "email_instituicao": "emailInstituicao", "arquivo_legislacao": "arquivoLegislacao",
    "foto_capa": "fotoCapa", "foto_divulgacao": "fotoDivulgacao",
    "cadastros_anteriores": "cadastrosAnteriores", "servico": "servico", "usuario": "usuario",
}

montar(PASTA, "X-Forms: cadastro de biblioteca pública FCMS", "BIB", "cadastros_bibliotecas_publicas", CORPO, COLUNAS)
