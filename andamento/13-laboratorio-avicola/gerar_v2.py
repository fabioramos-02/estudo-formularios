"""Gera xforms-v2.json do cadastro de laboratório de diagnóstico em sanidade avícola (IAGRO). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: cadastrar-laboratorio-sanidade-avicola
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
# ponytail: sem máscara porque laboratório costuma ter fixo (10 números) e a máscara do X-Forms é de tamanho fixo
TEL_RE = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
CREDENCIADO = "{credenciado_mapa} = 'sim'"
TEM_CEP = "{cep} notempty"  # mantido da v1: endereço aparece depois do CEP


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def cond(nome, msg, regra, **kw):
    return {"name": nome, "visibleIf": regra, "requiredIf": regra, "requiredErrorText": msg, **kw}


form = {
    "title": "Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola",
    "description": "Para laboratórios que fazem análises de saúde das aves para os programas oficiais de "
                   "monitoramento sanitário. O cadastro é feito na IAGRO (Agência Estadual de Defesa Sanitária "
                   "Animal e Vegetal).",
    "pages": [
        {"name": "pedido", "title": "O que você quer fazer", "elements": [
            {"type": "radiogroup", **obrig("tipo_pedido", "Escolha uma opção para continuar."),
             "title": "Você quer",
             "choices": [{"value": "cadastro", "text": "Fazer o cadastro do laboratório pela primeira vez"},
                         {"value": "atualizacao", "text": "Atualizar um cadastro que já existe"}]},
        ]},
        {"name": "solicitante", "title": "Quem está fazendo o pedido", "elements": [
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
             "tooltip": "Vem da sua conta. Corrija se estiver diferente do documento."},
        ]},
        {"name": "laboratorio", "title": "Sobre o laboratório", "elements": [
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
            {"type": "text", **obrig("telefone_laboratorio", "Digite o telefone com DDD."),
             "title": "Telefone do laboratório", "inputType": "tel", "placeholder": "(00) 0000-0000",
             "validators": [{"type": "regex", "regex": TEL_RE,
                             "text": "Digite o telefone com DDD, 10 ou 11 números."}]},
            {"type": "text", **obrig("email_laboratorio", "Preencha o e-mail para continuar."),
             "title": "E-mail do laboratório", "startWithNewLine": False, "inputType": "email",
             "placeholder": "nome@laboratorio.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do cadastro chega neste e-mail."},
        ]},
        {"name": "analises", "title": "Análises e credenciamento", "elements": [
            {"type": "comment", "name": "escopo_analises", "title": "Que análises o laboratório faz em aves? (opcional)",
             "description": "Por exemplo: Salmonela, Micoplasma. Escreva também outros tipos de teste.",
             "maxLength": 1000},
            {"type": "radiogroup", **obrig("credenciado_mapa", "Escolha Sim ou Não para continuar."),
             "title": "O laboratório é credenciado no MAPA?",
             "description": "MAPA é o Ministério da Agricultura e Pecuária.",
             "choices": [{"value": "sim", "text": "Sim"}, {"value": "nao", "text": "Não"}]},
            {"type": "text", **cond("numero_portaria_credenciamento",
                                    "Preencha o número da portaria para continuar.", CREDENCIADO),
             "title": "Número da portaria de credenciamento no MAPA"},
            {"type": "text", "name": "numero_crl", "title": "Número do CRL (opcional)",
             "description": "Se o laboratório tiver."},
        ]},
        {"name": "endereco", "title": "Onde fica o laboratório", "elements": [
            {"type": "text", **obrig("cep", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000",
             "validators": [{"type": "regex", "regex": CEP_RE, "text": "Digite o CEP com 8 números."}]},
            {"type": "text", **cond("logradouro", "Preencha o endereço para continuar.", TEM_CEP),
             "title": "Endereço", "description": "Rua, número e bairro.", "autocomplete": "street-address"},
            {"type": "text", **cond("municipio", "Preencha o município para continuar.", TEM_CEP),
             "title": "Município"},
            {"type": "dropdown", **cond("uf", "Escolha o estado para continuar.", TEM_CEP),
             "title": "Estado", "startWithNewLine": False, "placeholder": "Selecione",
             "choices": [{"value": s, "text": n} for s, n in UFS]},
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a IAGRO analisa o cadastro e a resposta chega no "
                     "e-mail do laboratório.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
