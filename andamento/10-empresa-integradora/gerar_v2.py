"""Gera xforms-v2.json do cadastro de empresa integradora de aves ou suínos (IAGRO). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: cadastrar-empresa-integradora-aves-suinos
"""
import json
from pathlib import Path

UFS = [("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
       ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
       ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
       ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
       ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
       ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
       ("SE", "Sergipe"), ("TO", "Tocantins")]
CNPJ_RE = r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"
CEP_RE = r"^\d{5}-?\d{3}$"
CEL_RE = r"^\(?\d{2}\)?\s?\d{5}-?\d{4}$"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def celular(nome, titulo, **kw):
    return {"type": "text", **obrig(nome, "Digite o telefone com DDD, 11 números."), "title": titulo,
            "inputType": "tel", "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
            "placeholder": "(00) 00000-0000",
            "validators": [{"type": "regex", "regex": CEL_RE, "text": "Digite o telefone com DDD, 11 números."}], **kw}


def email(nome, **kw):
    return {"type": "text", **obrig(nome, "Preencha o e-mail para continuar."), "title": "E-mail",
            "inputType": "email", "placeholder": "nome@empresa.com.br",
            "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}], **kw}


form = {
    "title": "Cadastrar ou atualizar empresa integradora de aves ou suínos",
    "description": "Para empresas integradoras da criação de aves (avicultura) ou de suínos (suinocultura) em "
                   "Mato Grosso do Sul. O cadastro é feito na IAGRO (Agência Estadual de Defesa Sanitária "
                   "Animal e Vegetal).",
    "pages": [
        {"name": "pedido", "title": "O que você quer fazer", "elements": [
            {"type": "radiogroup", **obrig("tipo_pedido", "Escolha uma opção para continuar."),
             "title": "Você quer",
             "choices": [{"value": "cadastro", "text": "Fazer o cadastro da empresa pela primeira vez"},
                         {"value": "atualizacao", "text": "Atualizar um cadastro que já existe"}]},
        ]},
        {"name": "representante", "title": "Representante legal da empresa",
         "description": "Quem responde pela empresa.", "elements": [
            {"type": "text", **obrig("nome_representante_legal", "Preencha o nome do representante legal para continuar."),
             "title": "Nome completo do representante legal"},
            celular("telefone_representante", "Telefone do representante"),
            email("email_representante", startWithNewLine=False,
                  tooltip="A resposta do cadastro chega neste e-mail."),
        ]},
        {"name": "empresa", "title": "Sobre a empresa", "elements": [
            {"type": "text", **obrig("razao_social", "Preencha a razão social para continuar."),
             "title": "Razão social", "description": "Como está no CNPJ."},
            {"type": "text", **obrig("nome_fantasia", "Preencha o nome fantasia para continuar."),
             "title": "Nome fantasia"},
            {"type": "text", **obrig("cnpj", "Digite o CNPJ com 14 números."),
             "title": "CNPJ", "description": "Cadastro Nacional da Pessoa Jurídica.",
             "maskType": "pattern", "maskSettings": {"pattern": "99.999.999/9999-99"},
             "placeholder": "00.000.000/0000-00",
             "validators": [{"type": "regex", "regex": CNPJ_RE, "text": "Digite o CNPJ com 14 números."}]},
            {"type": "text", **obrig("inscricao_estadual", "Preencha a inscrição estadual para continuar."),
             "title": "Inscrição estadual", "startWithNewLine": False},
            {"type": "radiogroup", **obrig("atividade_integradora", "Escolha uma opção para continuar."),
             "title": "A empresa é integradora de",
             "choices": [{"value": "avicultura", "text": "Aves (avicultura)"},
                         {"value": "suinocultura", "text": "Suínos (suinocultura)"}]},
            celular("telefone_empresa", "Telefone da empresa"),
            email("email_empresa", startWithNewLine=False),
        ]},
        {"name": "endereco", "title": "Onde fica a empresa", "elements": [
            {"type": "text", **obrig("cep", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000",
             "validators": [{"type": "regex", "regex": CEP_RE, "text": "Digite o CEP com 8 números."}]},
            {"type": "text", **obrig("municipio", "Preencha o município para continuar."), "title": "Município"},
            {"type": "dropdown", **obrig("uf", "Escolha o estado para continuar."),
             "title": "Estado", "startWithNewLine": False, "placeholder": "Selecione",
             "choices": [{"value": s, "text": n} for s, n in UFS]},
            {"type": "text", "name": "via_acesso", "title": "Via de acesso (opcional)",
             "description": "Um ponto de referência para chegar à empresa."},
            {"type": "text", "name": "coordenada_geografica", "title": "Coordenada geográfica (opcional)",
             "description": "Em graus decimais. Exemplo: S: -20.00000 -50.00000"},
        ]},
        {"name": "complemento", "title": "Mais informações", "elements": [
            {"type": "comment", "name": "informacoes_complementares", "title": "Informações complementares (opcional)",
             "description": "Escreva aqui outra informação importante sobre a empresa.", "maxLength": 1000},
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o cadastro e a resposta chega no "
                     "e-mail do representante legal.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
