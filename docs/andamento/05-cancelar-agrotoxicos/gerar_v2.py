"""Gera xforms-v2.json do cancelamento de registro de estabelecimento de agrotóxicos (IAGRO). Rodar: python gerar_v2.py"""
import json
from pathlib import Path

UFS = [("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
       ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
       ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
       ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
       ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
       ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
       ("SE", "Sergipe"), ("TO", "Tocantins")]
CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CNPJ_RE = r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg):
    return {"type": "file", **obrig(nome, msg), "title": titulo, "description": descricao,
            "acceptedTypes": ".pdf", "maxSize": 5242880, "storeDataAsText": True,
            "allowMultiple": False, "waitForUpload": True}


form = {
    "title": "Cancelar registro de empresa de agrotóxicos na IAGRO",
    "description": "Para empresas que vendem, transportam ou aplicam agrotóxicos e querem encerrar o registro na "
                   "IAGRO (Agência Estadual de Defesa Sanitária Animal e Vegetal).",
    "pages": [
        {"name": "responsavel", "title": "Responsável pela empresa", "elements": [
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
             "description": "Quem responde pela empresa e assina este pedido.",
             "tooltip": "Vem da sua conta. Corrija se estiver diferente do documento."},
            {"type": "text", **obrig("cpf", "Digite um CPF válido, com 11 números."),
             "title": "CPF", "description": "Cadastro de Pessoa Física.", "autocomplete": "cpf",
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"},
             "placeholder": "000.000.000-00",
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite um CPF com 11 números."}],
             "tooltip": "Vem da sua conta."},
            {"type": "text", **obrig("email", "Preencha o e-mail para continuar."),
             "title": "E-mail", "inputType": "email", "autocomplete": "email",
             "placeholder": "nome@empresa.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do pedido chega neste e-mail."},
        ]},
        {"name": "empresa", "title": "Sobre a empresa", "elements": [
            {"type": "text", **obrig("razao_social", "Preencha o nome da empresa para continuar."),
             "title": "Nome da empresa", "description": "Como está no CNPJ (razão social)."},
            {"type": "text", **obrig("cnpj", "Digite o CNPJ com 14 números."),
             "title": "CNPJ", "description": "Cadastro Nacional da Pessoa Jurídica.",
             "maskType": "pattern", "maskSettings": {"pattern": "99.999.999/9999-99"},
             "placeholder": "00.000.000/0000-00",
             "validators": [{"type": "regex", "regex": CNPJ_RE, "text": "Digite o CNPJ com 14 números."}]},
            {"type": "text", **obrig("inscricao_estadual", "Preencha a inscrição estadual para continuar."),
             "title": "Inscrição estadual", "startWithNewLine": False},
            {"type": "text", **obrig("logradouro", "Preencha o endereço para continuar."),
             "title": "Endereço", "description": "Rua, número e complemento.",
             "autocomplete": "street-address"},
            {"type": "text", **obrig("municipio", "Preencha o município para continuar."),
             "title": "Município"},
            {"type": "dropdown", **obrig("uf", "Escolha o estado para continuar."),
             "title": "Estado", "startWithNewLine": False, "placeholder": "Selecione",
             "choices": [{"value": s, "text": n} for s, n in UFS]},
        ]},
        {"name": "motivo", "title": "Motivo do cancelamento", "elements": [
            {"type": "radiogroup", **obrig("motivo_cancelamento", "Escolha o motivo para continuar."),
             "title": "Por que a empresa quer cancelar o registro?",
             "description": "Escolha a frase que vale para a sua empresa.",
             "choices": [
                 {"value": "nao_comercializa", "text": "Não vendemos agrotóxicos, seus componentes e afins."},
                 {"value": "lei_2951", "text": "Não vamos continuar vendendo agrotóxicos, seus componentes e afins, "
                                                "por causa das exigências da Lei Estadual nº 2.951, de 17/12/2004."},
                 {"value": "nao_transporta", "text": "Não transportamos agrotóxicos, seus componentes e afins."},
                 {"value": "nao_aplica", "text": "Não prestamos serviço de aplicação de agrotóxicos, seus componentes e afins."},
             ]},
        ]},
        {"name": "documentos", "title": "Documentos", "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_cartao_cnpj", "Comprovante de inscrição no CNPJ",
                  "O cartão CNPJ, emitido no site da Receita Federal.",
                  "Anexe o comprovante do CNPJ para continuar."),
            anexo("arquivo_guia_recolhimento", "Guia de recolhimento",
                  "A guia paga.", "Anexe a guia de recolhimento para continuar."),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o pedido e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
