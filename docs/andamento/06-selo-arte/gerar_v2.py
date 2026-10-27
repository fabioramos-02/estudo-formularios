"""Gera xforms-v2.json do pedido de Selo Arte (IAGRO). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: `obter-selo-arte`.
"""
import json
from pathlib import Path

PASTA = Path(__file__).resolve().parent
CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
# ponytail: os 79 municípios de MS vêm da v1, para não repetir a lista aqui
MUNICIPIOS_MS = next(e["choices"] for p in json.loads((PASTA / "xforms-v1-demo.json").read_text(encoding="utf-8-sig"))["pages"]
                     for e in p["elements"] if e["name"] == "municipio")


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg, tipos=".pdf"):
    return {"type": "file", **obrig(nome, msg), "title": titulo, "description": descricao,
            "acceptedTypes": tipos, "maxSize": 5242880, "storeDataAsText": True,
            "allowMultiple": False, "waitForUpload": True}


DECLARACAO = (
    "<p>Ao pedir o Selo Arte, declaro que estou ciente de que:</p><ul>"
    "<li>devo seguir os procedimentos da legislação em vigor para a produção artesanal de alimentos de origem animal;</li>"
    "<li>o produto para o qual peço o selo, fabricado no meu estabelecimento, cumpre todos os requisitos das leis e normas que se aplicam a ele;</li>"
    "<li>só posso produzir e vender com o Selo Arte depois da homologação;</li>"
    "<li>devo cumprir todas as exigências do serviço de inspeção em que estou registrado, incluindo as boas práticas "
    "agropecuárias e de fabricação e as demais leis que se aplicam.</li></ul>"
)

form = {
    "title": "Pedir o Selo Arte",
    "description": "Para quem produz alimentos de origem animal de forma artesanal e quer o Selo Arte para os seus produtos.",
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
        ]},
        {"name": "estabelecimento", "title": "Sobre o estabelecimento", "elements": [
            {"type": "text", **obrig("nome_estabelecimento", "Preencha o nome do estabelecimento para continuar."),
             "title": "Nome do estabelecimento", "description": "Onde os produtos são fabricados."},
            {"type": "text", **obrig("registro_servico_inspecao", "Preencha o serviço de inspeção para continuar."),
             "title": "Serviço de inspeção em que o estabelecimento é registrado"},
            {"type": "text", **obrig("numero_registro", "Preencha o número do registro para continuar."),
             "title": "Número do registro", "description": "O número no serviço de inspeção."},
        ]},
        {"name": "endereco", "title": "Endereço do estabelecimento", "elements": [
            {"type": "text", **obrig("logradouro", "Preencha o endereço para continuar."),
             "title": "Endereço", "description": "Rua, número, complemento e bairro.",
             "autocomplete": "street-address"},
            {"type": "dropdown", **obrig("municipio", "Escolha o município para continuar."),
             "title": "Município", "placeholder": "Selecione", "choices": MUNICIPIOS_MS},
        ]},
        {"name": "pedido", "title": "Produtos e declaração", "elements": [
            {"type": "comment", **obrig("produtos", "Escreva os produtos para continuar."),
             "title": "Para quais produtos você pede o selo?",
             "description": "Escreva um produto por linha."},
            {"type": "html", "name": "texto_declaracao", "html": DECLARACAO},
            {"type": "checkbox", **obrig("declaracao_ciencia", "Marque a declaração para enviar o pedido."),
             "title": "Declaração", "choices": [{"value": "ciente", "text": "Li e estou ciente do que está escrito acima."}]},
        ]},
        {"name": "documentos", "title": "Documentos",
         "description": "Arquivo em PDF, JPG ou PNG, até 5 MB.", "elements": [
            anexo("arquivo_logomarca", "Logomarca do estabelecimento",
                  "A identidade visual usada nos produtos.",
                  "Anexe a logomarca para continuar.", ".pdf,.jpg,.jpeg,.png"),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o pedido e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

(PASTA / "xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
