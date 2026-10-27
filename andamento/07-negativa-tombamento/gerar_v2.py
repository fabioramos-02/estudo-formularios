"""Gera xforms-v2.json do pedido de certidão negativa de tombamento (FCMS). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: `pedir-certidao-negativa-tombamento`.
"""
import json
from pathlib import Path

CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
REPRESENTANTE = "{perfil_solicitante} = 'representante'"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg, multiplos=False, **kw):
    d = {"type": "file", **obrig(nome, msg), "title": titulo, "description": descricao,
         "acceptedTypes": ".pdf", "maxSize": 5242880, "storeDataAsText": True,
         "allowMultiple": multiplos, "waitForUpload": True, **kw}
    if "requiredIf" in kw:
        del d["isRequired"]  # campo condicional: obrigatório só pelo requiredIf
    return d


form = {
    "title": "Pedir certidão negativa de tombamento",
    "description": "A certidão atesta que um imóvel não é tombado, ou seja, não está protegido como patrimônio "
                   "cultural pelo município, pelo Estado ou pela União. O pedido vai para a FCMS (Fundação de "
                   "Cultura de Mato Grosso do Sul).",
    "pages": [
        {"name": "solicitante", "title": "Quem está fazendo o pedido", "elements": [
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
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
            {"type": "radiogroup", **obrig("perfil_solicitante", "Escolha uma opção para continuar."),
             "title": "Você é o proprietário do imóvel?",
             "tooltip": "Quem pede em nome do proprietário anexa uma procuração no fim do formulário.",
             "choices": [{"value": "proprietario", "text": "Sim, sou o proprietário"},
                         {"value": "representante", "text": "Não, peço em nome do proprietário"}]},
        ]},
        {"name": "imovel", "title": "Sobre o imóvel", "elements": [
            {"type": "comment", **obrig("identificacao_imovel", "Escreva o nome e a localização do imóvel para continuar."),
             "title": "Nome e localização do imóvel",
             "description": "Como o imóvel é conhecido e onde fica: endereço e município."},
            {"type": "text", "name": "cpf_proprietario", "requiredErrorText": "Digite o CPF do proprietário, com 11 números.",
             "title": "CPF do proprietário", "visibleIf": REPRESENTANTE, "requiredIf": REPRESENTANTE,
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"},
             "placeholder": "000.000.000-00",
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite um CPF com 11 números."}]},
        ]},
        {"name": "documentos", "title": "Documentos", "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_certidao_matricula", "Certidão de matrícula do imóvel",
                  "A certidão atualizada, emitida pelo cartório de registro de imóveis.",
                  "Anexe a certidão de matrícula para continuar."),
            anexo("arquivo_documento_requerente", "Seu RG e CPF",
                  "Pode enviar mais de um arquivo, por exemplo frente e verso.",
                  "Anexe o seu RG e CPF para continuar.", multiplos=True),
            anexo("arquivo_documento_proprietario", "RG e CPF do proprietário",
                  "Pode enviar mais de um arquivo, por exemplo frente e verso.",
                  "Anexe o RG e o CPF do proprietário para continuar.", multiplos=True,
                  visibleIf=REPRESENTANTE, requiredIf=REPRESENTANTE),
            anexo("arquivo_procuracao", "Procuração",
                  "Dada pelo proprietário a você, assinada pelo gov.br ou com certificado digital.",
                  "Anexe a procuração para continuar.",
                  visibleIf=REPRESENTANTE, requiredIf=REPRESENTANTE),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a FCMS analisa o pedido e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
