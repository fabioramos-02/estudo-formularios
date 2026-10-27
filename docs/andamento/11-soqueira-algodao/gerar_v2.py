"""Gera xforms-v2.json do pedido de certificado de destruição de soqueira de algodão (IAGRO). Rodar: python gerar_v2.py

Slug proposto para DEV: pedir-certificado-destruicao-soqueira-algodao
"""
import json
from pathlib import Path

CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CEL_RE = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg):
    return {"type": "file", **obrig(nome, msg), "title": titulo, "description": descricao,
            "acceptedTypes": ".pdf", "maxSize": 5242880, "storeDataAsText": True,
            "allowMultiple": False, "waitForUpload": True}


form = {
    "title": "Pedir certificado de destruição de soqueira de algodão",
    "description": "Para produtores de algodão que destruíram a soqueira (o que sobra da planta depois da "
                   "colheita) e precisam do certificado da IAGRO (Agência Estadual de Defesa Sanitária Animal "
                   "e Vegetal).",
    "pages": [
        {"name": "responsavel", "title": "Seus dados", "elements": [
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
             "description": "Quem responde por este pedido.",
             "tooltip": "Vem da sua conta. Corrija se estiver diferente do documento."},
            {"type": "text", **obrig("cpf", "Digite um CPF válido, com 11 números."),
             "title": "CPF", "description": "Cadastro de Pessoa Física.", "autocomplete": "cpf",
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"},
             "placeholder": "000.000.000-00",
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite um CPF com 11 números."}],
             "tooltip": "Vem da sua conta."},
            {"type": "text", **obrig("email", "Preencha o e-mail para continuar."),
             "title": "E-mail", "inputType": "email", "autocomplete": "email",
             "placeholder": "nome@exemplo.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do pedido chega neste e-mail."},
            {"type": "text", **obrig("telefone_celular", "Digite o celular com DDD, 11 números."),
             "title": "Celular", "startWithNewLine": False, "inputType": "tel", "autocomplete": "tel",
             "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
             "placeholder": "(00) 00000-0000",
             "validators": [{"type": "regex", "regex": CEL_RE, "text": "Digite o celular com DDD, 11 números."}]},
        ]},
        {"name": "lavoura", "title": "Área de plantio", "elements": [
            {"type": "radiogroup", **obrig("area_plantio", "Escolha o tamanho da área para continuar."),
             "title": "Qual o tamanho da área plantada?",
             "description": "O valor da guia DAEMS depende do tamanho da área.",
             "choices": [{"value": "ate_50_hectares", "text": "Até 50 hectares"},
                         {"value": "acima_50_hectares", "text": "Mais de 50 hectares"}]},
        ]},
        {"name": "documentos", "title": "Documentos", "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_relatorio_fiscalizacao", "Relatório de Fiscalização (RF)",
                  "Emita o relatório no e-Saniagro, o sistema da IAGRO.",
                  "Anexe o Relatório de Fiscalização para continuar."),
            anexo("arquivo_guia_daems", "Guia DAEMS",
                  "Documento de Arrecadação do Estado de Mato Grosso do Sul. Emita a guia do valor que "
                  "corresponde à sua área de plantio.",
                  "Anexe a guia DAEMS para continuar."),
            anexo("arquivo_comprovante_pagamento", "Comprovante de pagamento da guia DAEMS",
                  "O comprovante do banco ou do aplicativo em que a guia foi paga.",
                  "Anexe o comprovante de pagamento para continuar."),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o pedido e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
