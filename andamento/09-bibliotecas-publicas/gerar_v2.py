"""Gera xforms-v2.json do cadastro no Sistema Estadual de Bibliotecas Públicas (FCMS). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: `cadastrar-biblioteca-publica`.
"""
import json
from pathlib import Path

PASTA = Path(__file__).resolve().parent
CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CNPJ_RE = r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"
CEP_RE = r"^\d{5}-?\d{3}$"
TEL_RE = r"^\(?\d{2}\)?\s?\d{5}-?\d{4}$"
# ponytail: os 79 municípios de MS vêm da v1, para não repetir a lista aqui
MUNICIPIOS_MS = next(e["choices"] for p in json.loads((PASTA / "xforms-v1-demo.json").read_text(encoding="utf-8-sig"))["pages"]
                     for e in p["elements"] if e["name"] == "municipio")
PUBLICA = "{tipo_biblioteca} = 'publica'"
FUNCIONA = "{em_funcionamento} = 'sim'"
SIM_NAO = [{"value": "sim", "text": "Sim"}, {"value": "nao", "text": "Não"}]


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def condicional(nome, msg, cond, **kw):
    """Aparece e é obrigatório só quando `cond` vale (C9)."""
    return {"name": nome, "visibleIf": cond, "requiredIf": cond, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, tipos=".pdf", multiplos=False, **kw):
    return {"type": "file", "name": nome, "title": titulo, "description": descricao,
            "acceptedTypes": tipos, "maxSize": 5242880, "storeDataAsText": True,
            "allowMultiple": multiplos, "waitForUpload": True, **kw}


form = {
    "title": "Cadastrar biblioteca no Sistema Estadual de Bibliotecas Públicas",
    "description": "Para bibliotecas públicas e comunitárias de Mato Grosso do Sul. O cadastro na FCMS (Fundação de "
                   "Cultura de Mato Grosso do Sul) dá reconhecimento oficial e acesso a formações, recursos, acervos, "
                   "equipamentos e parcerias. Atualize os dados todo ano ou quando mudar a gestão, o endereço ou a estrutura.",
    "pages": [
        {"name": "biblioteca", "title": "Sobre a biblioteca", "elements": [
            {"type": "text", **obrig("nome_biblioteca", "Preencha o nome da biblioteca para continuar."),
             "title": "Nome da biblioteca"},
            {"type": "radiogroup", **obrig("tipo_biblioteca", "Escolha o tipo da biblioteca para continuar."),
             "title": "Tipo de biblioteca",
             "choices": [{"value": "publica", "text": "Pública"}, {"value": "comunitaria", "text": "Comunitária"},
                         {"value": "associada", "text": "Associada"}]},
            {"type": "text", **condicional("legislacao_criacao", "Escreva a lei ou o decreto que criou a biblioteca para continuar.", PUBLICA),
             "title": "Lei ou decreto que criou a biblioteca",
             "placeholder": "Ex.: Lei Municipal nº 1.234/2001"},
            {"type": "radiogroup", **obrig("em_funcionamento", "Escolha Sim ou Não para continuar."),
             "title": "A biblioteca está funcionando?", "choices": SIM_NAO},
            {"type": "radiogroup", **obrig("respondeu_diagnostico", "Escolha Sim ou Não para continuar."),
             "title": "A biblioteca respondeu ao diagnóstico mais recente das bibliotecas?", "choices": SIM_NAO},
            {"type": "text", **obrig("descricao_biblioteca", "Descreva a biblioteca em uma frase para continuar."),
             "title": "Descreva a biblioteca em uma frase"},
            {"type": "comment", **obrig("historia_biblioteca", "Conte a história da biblioteca para continuar."),
             "title": "Conte a história da biblioteca"},
        ]},
        {"name": "responsavel_biblioteca", "title": "Responsável pela biblioteca", "elements": [
            {"type": "text", **obrig("nome_responsavel_biblioteca", "Preencha o nome do responsável para continuar."),
             "title": "Nome completo do responsável"},
            {"type": "text", **obrig("cargo_responsavel_biblioteca", "Preencha o cargo do responsável para continuar."),
             "title": "Cargo"},
            {"type": "text", **obrig("escolaridade_responsavel_biblioteca", "Preencha a escolaridade do responsável para continuar."),
             "title": "Escolaridade", "startWithNewLine": False},
        ]},
        {"name": "funcionamento", "title": "Como a biblioteca funciona", "elements": [
            {"type": "comment", **condicional("horario_funcionamento", "Escreva o horário de funcionamento para continuar.", FUNCIONA),
             "title": "Horário de funcionamento",
             "description": "Escreva o horário de cada dia, de segunda a domingo, e dos feriados. "
                            "Se muda em alguma época do ano, diga também."},
            {"type": "comment", "name": "informacoes_adicionais_horario", "visibleIf": FUNCIONA,
             "title": "Mais alguma informação sobre o horário? (opcional)"},
            {"type": "text", **obrig("numero_pessoas_trabalham", "Digite quantas pessoas trabalham na biblioteca. Use 0 se não houver."),
             "title": "Quantas pessoas trabalham na biblioteca?", "inputType": "number", "min": 0,
             "maskType": "numeric", "maskSettings": {"allowNegativeValues": False, "precision": 0},
             "validators": [{"type": "numeric", "minValue": 0, "text": "Digite um número inteiro, 0 ou mais."}]},
            {"type": "comment", "name": "nomes_pessoas_trabalham", "visibleIf": "{numero_pessoas_trabalham} > 0",
             "title": "Nome completo de quem trabalha na biblioteca (opcional)",
             "description": "Um nome por linha."},
            {"type": "radiogroup", "name": "possui_acessibilidade",
             "title": "A biblioteca tem facilidades para pessoas com deficiência ou mobilidade reduzida? (opcional)",
             "choices": SIM_NAO},
            {"type": "comment", "name": "acessibilidade_oferecida", "visibleIf": "{possui_acessibilidade} = 'sim'",
             "title": "Quais facilidades a biblioteca oferece? (opcional)"},
        ]},
        {"name": "endereco_biblioteca", "title": "Endereço e contato da biblioteca", "elements": [
            {"type": "text", **obrig("cep_biblioteca", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000",
             "validators": [{"type": "regex", "regex": CEP_RE, "text": "Digite o CEP com 8 números."}]},
            {"type": "text", **obrig("logradouro_biblioteca", "Preencha o endereço para continuar."),
             "title": "Endereço", "description": "Rua, número e complemento.", "autocomplete": "street-address"},
            {"type": "text", **obrig("bairro_biblioteca", "Preencha o bairro para continuar."), "title": "Bairro"},
            {"type": "dropdown", **obrig("municipio", "Escolha o município para continuar."),
             "title": "Município", "startWithNewLine": False, "placeholder": "Selecione", "choices": MUNICIPIOS_MS},
            {"type": "comment", "name": "contatos_redes_sociais", "title": "Contatos e redes sociais da biblioteca (opcional)",
             "description": "E-mail, telefone, WhatsApp, Instagram, Facebook, YouTube e outras redes. Um por linha."},
        ]},
        {"name": "instituicao", "title": "Instituição ligada à biblioteca", "elements": [
            {"type": "text", **obrig("nome_instituicao_vinculada", "Preencha o nome da instituição para continuar."),
             "title": "Nome da instituição", "description": "A instituição à qual a biblioteca está ligada."},
            {"type": "radiogroup", **obrig("tipo_documento_instituicao", "Escolha CNPJ ou CPF para continuar."),
             "title": "A instituição tem CNPJ ou CPF?",
             "choices": [{"value": "cnpj", "text": "CNPJ (Cadastro Nacional da Pessoa Jurídica)"},
                         {"value": "cpf", "text": "CPF (Cadastro de Pessoa Física)"}]},
            {"type": "text", **condicional("cnpj_instituicao", "Digite o CNPJ com 14 números.", "{tipo_documento_instituicao} = 'cnpj'"),
             "title": "CNPJ da instituição",
             "maskType": "pattern", "maskSettings": {"pattern": "99.999.999/9999-99"}, "placeholder": "00.000.000/0000-00",
             "validators": [{"type": "regex", "regex": CNPJ_RE, "text": "Digite o CNPJ com 14 números."}]},
            {"type": "text", **condicional("cpf_instituicao", "Digite o CPF com 11 números.", "{tipo_documento_instituicao} = 'cpf'"),
             "title": "CPF da instituição",
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"}, "placeholder": "000.000.000-00",
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite o CPF com 11 números."}]},
            {"type": "comment", **obrig("endereco_instituicao", "Preencha o endereço da instituição para continuar."),
             "title": "Endereço da instituição", "description": "CEP, rua, número, complemento, bairro e município."},
            {"type": "text", **obrig("telefone_instituicao", "Digite o telefone com DDD, 11 números."),
             "title": "Telefone da instituição", "inputType": "tel", "autocomplete": "tel",
             "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"}, "placeholder": "(00) 00000-0000",
             "validators": [{"type": "regex", "regex": TEL_RE, "text": "Digite o telefone com DDD, 11 números."}]},
            {"type": "text", **obrig("email_instituicao", "Preencha o e-mail da instituição para continuar."),
             "title": "E-mail da instituição", "startWithNewLine": False, "inputType": "email",
             "placeholder": "nome@exemplo.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do cadastro chega neste e-mail."},
        ]},
        {"name": "responsavel_instituicao", "title": "Responsável pela instituição", "elements": [
            {"type": "text", **obrig("nome_responsavel_instituicao", "Preencha o nome do responsável para continuar."),
             "title": "Nome completo do responsável"},
            {"type": "text", **obrig("cargo_responsavel_instituicao", "Preencha o cargo do responsável para continuar."),
             "title": "Cargo", "startWithNewLine": False},
        ]},
        {"name": "documentos", "title": "Documentos e fotos",
         "description": "Cada arquivo pode ter até 5 MB. Documentos em PDF; fotos em JPG ou PNG.", "elements": [
            anexo("arquivo_legislacao_criacao", "Lei ou decreto que criou a biblioteca",
                  "O documento de criação, em PDF.",
                  visibleIf=PUBLICA, requiredIf=PUBLICA, requiredErrorText="Anexe a lei ou o decreto de criação para continuar."),
            anexo("arquivo_foto_capa", "Foto da fachada (opcional)",
                  "A frente ou a entrada da biblioteca. É a foto de capa.", ".jpg,.jpeg,.png"),
            anexo("arquivo_foto_divulgacao", "Foto de divulgação (opcional)", "Em JPG ou PNG.", ".jpg,.jpeg,.png"),
            anexo("arquivo_cadastros_anteriores", "Cadastros anteriores (opcional)",
                  "Documentos que mostram cadastro anterior no Sistema Estadual ou Nacional de Bibliotecas. "
                  "Em PDF ou JPG; pode enviar mais de um.", ".pdf,.jpg,.jpeg", multiplos=True),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a FCMS analisa o cadastro e a resposta chega no e-mail da instituição.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

(PASTA / "xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
