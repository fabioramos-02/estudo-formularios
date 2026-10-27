"""Gera xforms-v2.json do cadastro de indústria de agrotóxicos (IAGRO). Rodar: python gerar_v2.py"""
import json
from pathlib import Path

UFS = [("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
       ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
       ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
       ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
       ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
       ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
       ("SE", "Sergipe"), ("TO", "Tocantins")]
CONSULTORIA = "{perfil_solicitante} = 'consultoria'"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg, **kw):
    d = {"type": "file", "name": nome, "title": titulo, "description": descricao,
         "isRequired": True, "requiredErrorText": msg,
         "acceptedTypes": ".pdf", "maxSize": 5242880, "storeDataAsText": True,
         "allowMultiple": False, "waitForUpload": True, **kw}
    if not d["isRequired"]:
        del d["isRequired"]  # o Designer apaga o valor padrão; sem isso o hash não confere
    return d


form = {
    "title": "Cadastrar indústria de agrotóxicos no e-Saniagro",
    "description": "Para indústrias de agrotóxicos que precisam de cadastro no e-Saniagro, o sistema da IAGRO "
                   "(Agência Estadual de Defesa Sanitária Animal e Vegetal). Pode ser feito pela própria "
                   "empresa ou por uma consultoria que a represente.",
    "pages": [
        {"name": "solicitante", "title": "Quem está fazendo o pedido", "elements": [
            {"type": "radiogroup", **obrig("perfil_solicitante", "Escolha uma opção para continuar."),
             "title": "Você é",
             "tooltip": "Quem representa a indústria anexa uma procuração no fim do formulário.",
             "choices": [{"value": "empresa", "text": "Da própria indústria"},
                         {"value": "consultoria", "text": "De consultoria ou empresa de registros que representa a indústria"}]},
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
             "tooltip": "Vem da sua conta. A IAGRO fala com você sobre este cadastro."},
            {"type": "text", **obrig("email", "Preencha o e-mail para continuar."),
             "title": "E-mail", "inputType": "email", "autocomplete": "email",
             "placeholder": "nome@empresa.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do cadastro chega neste e-mail."},
            {"type": "text", **obrig("telefone_celular", "Digite o celular com DDD, 11 números."),
             "title": "Celular", "startWithNewLine": False, "inputType": "tel", "autocomplete": "tel",
             "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
             "placeholder": "(00) 00000-0000"},
        ]},
        {"name": "industria", "title": "Sobre a indústria", "elements": [
            {"type": "text", **obrig("cnpj", "Digite o CNPJ com 14 números."),
             "title": "CNPJ", "description": "Cadastro Nacional da Pessoa Jurídica da indústria.",
             "maskType": "pattern", "maskSettings": {"pattern": "99.999.999/9999-99"},
             "placeholder": "00.000.000/0000-00",
             "validators": [{"type": "regex", "regex": r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$",
                             "text": "Digite o CNPJ com 14 números."}]},
            {"type": "text", **obrig("razao_social", "Preencha a razão social para continuar."),
             "title": "Razão social", "description": "O nome da empresa no CNPJ."},
            {"type": "text", **obrig("nome_representante_legal", "Preencha o nome do representante legal para continuar."),
             "title": "Nome do representante legal",
             "description": "Quem responde pela indústria, como consta no contrato social."},
        ]},
        {"name": "endereco", "title": "Endereço para correspondência", "elements": [
            {"type": "text", **obrig("cep", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000"},
            {"type": "text", **obrig("logradouro", "Preencha o endereço para continuar."),
             "title": "Endereço", "description": "Rua, número e complemento.",
             "autocomplete": "street-address"},
            {"type": "text", **obrig("bairro", "Preencha o bairro para continuar."), "title": "Bairro"},
            {"type": "text", **obrig("municipio", "Preencha o município para continuar."),
             "title": "Município", "startWithNewLine": False},
            {"type": "dropdown", **obrig("uf", "Escolha o estado para continuar."),
             "title": "Estado", "placeholder": "Selecione",
             "choices": [{"value": s, "text": n} for s, n in UFS]},
        ]},
        {"name": "documentos", "title": "Documentos", "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_cartao_cnpj", "Comprovante de inscrição no CNPJ",
                  "O cartão CNPJ, emitido no site da Receita Federal.",
                  "Anexe o comprovante do CNPJ para continuar."),
            anexo("arquivo_contrato_social", "Contrato social",
                  "A versão atual, com as alterações.", "Anexe o contrato social para continuar."),
            anexo("arquivo_procuracao", "Procuração",
                  "Dada pela indústria à consultoria ou empresa de registros, para este cadastro.",
                  "Anexe a procuração para continuar.",
                  isRequired=False, visibleIf=CONSULTORIA, requiredIf=CONSULTORIA),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o cadastro e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
