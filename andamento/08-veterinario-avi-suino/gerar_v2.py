"""Gera xforms-v2.json do cadastro de médico veterinário de avicultura e suinocultura (IAGRO). Rodar: python gerar_v2.py

Slug proposto no X-Forms de DEV: cadastrar-veterinario-aves-suinos
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
CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CNPJ_RE = r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$"
CEP_RE = r"^\d{5}-?\d{3}$"
CEL_RE = r"^\(?\d{2}\)?\s?\d{5}-?\d{4}$"
VINCULADO = "{empresa_vinculada} = 'sim'"


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


def celular(nome, titulo, msg=None):
    d = {"name": nome, "title": titulo, "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
         "placeholder": "(00) 00000-0000",
         "validators": [{"type": "regex", "regex": CEL_RE, "text": "Digite o celular com DDD, 11 números."}]}
    if msg:
        d.update(isRequired=True, requiredErrorText=msg)
    return d


DEPOIS = ("<p><strong>Depois do envio:</strong> a IAGRO analisa o cadastro e a resposta chega no "
          "e-mail informado.</p>")

form = {
    "title": "Cadastrar ou atualizar médico veterinário de aves ou suínos",
    "description": "Para médicos veterinários do setor privado que atuam na criação de aves (avicultura) ou de "
                   "suínos (suinocultura) em Mato Grosso do Sul. O cadastro é feito na IAGRO (Agência Estadual "
                   "de Defesa Sanitária Animal e Vegetal).",
    "pages": [
        {"name": "pedido", "title": "O que você quer fazer", "elements": [
            {"type": "radiogroup", **obrig("tipo_pedido", "Escolha uma opção para continuar."),
             "title": "Você quer",
             "choices": [{"value": "cadastro", "text": "Fazer o cadastro pela primeira vez"},
                         {"value": "atualizacao", "text": "Atualizar um cadastro que já existe"}]},
        ]},
        {"name": "veterinario", "title": "Seus dados", "elements": [
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
             "placeholder": "nome@dominio.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do cadastro chega neste e-mail."},
            {"type": "multipletext", **obrig("telefones", "Digite o celular principal com DDD, 11 números."),
             "title": "Telefones para contato",
             "items": [celular("telefone_celular", "Celular principal", "Digite o celular principal com DDD, 11 números."),
                       celular("telefone_adicional", "Outro celular (opcional)")]},
            {"type": "text", "name": "numero_crmv", "title": "Número de inscrição no CRMV-MS (opcional)",
             "description": "Conselho Regional de Medicina Veterinária de Mato Grosso do Sul."},
        ]},
        {"name": "endereco", "title": "Seu endereço", "elements": [
            {"type": "text", **obrig("cep", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000",
             "validators": [{"type": "regex", "regex": CEP_RE, "text": "Digite o CEP com 8 números."}]},
            {"type": "text", **obrig("logradouro", "Preencha o endereço para continuar."),
             "title": "Endereço", "description": "Rua, número e bairro.", "autocomplete": "street-address"},
            {"type": "text", **obrig("municipio", "Preencha o município para continuar."), "title": "Município"},
            {"type": "dropdown", **obrig("uf", "Escolha o estado para continuar."),
             "title": "Estado", "startWithNewLine": False, "placeholder": "Selecione",
             "choices": [{"value": s, "text": n} for s, n in UFS]},
        ]},
        {"name": "vinculo", "title": "Vínculo com empresa", "elements": [
            {"type": "radiogroup", **obrig("empresa_vinculada", "Escolha Sim ou Não para continuar."),
             "title": "Você tem vínculo com alguma empresa integradora ou cooperativa?",
             "choices": [{"value": "sim", "text": "Sim"}, {"value": "nao", "text": "Não"}]},
            {"type": "html", "name": "aviso_proximos_passos_sem_vinculo", "visibleIf": "{empresa_vinculada} = 'nao'",
             "html": DEPOIS},
        ]},
        {"name": "empresa", "title": "Empresa integradora ou cooperativa", "visibleIf": VINCULADO, "elements": [
            {"type": "text", "name": "cnpj_empresa", "title": "CNPJ da empresa ou cooperativa",
             "description": "Cadastro Nacional da Pessoa Jurídica.", "requiredIf": VINCULADO,
             "requiredErrorText": "Digite o CNPJ com 14 números.",
             "maskType": "pattern", "maskSettings": {"pattern": "99.999.999/9999-99"},
             "placeholder": "00.000.000/0000-00",
             "validators": [{"type": "regex", "regex": CNPJ_RE, "text": "Digite o CNPJ com 14 números."}]},
            {"type": "text", "name": "razao_social_empresa", "title": "Razão social e nome fantasia",
             "description": "Da empresa integradora ou cooperativa.", "requiredIf": VINCULADO,
             "requiredErrorText": "Preencha o nome da empresa para continuar."},
            {"type": "text", "name": "numero_portaria_mapa",
             "title": "Número da portaria de habilitação no MAPA",
             "description": "MAPA é o Ministério da Agricultura e Pecuária. O número é usado para emitir a GTA "
                            "(Guia de Trânsito Animal) de aves e suínos.",
             "requiredIf": VINCULADO, "requiredErrorText": "Preencha o número da portaria para continuar."},
        ]},
        {"name": "documentos", "title": "Documentos", "visibleIf": VINCULADO,
         "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_vinculo_empresa", "Comprovante de vínculo com a empresa ou cooperativa",
                  "Documento que mostra o seu vínculo com a empresa integradora ou cooperativa.",
                  "Anexe o comprovante de vínculo para continuar.", isRequired=False, requiredIf=VINCULADO),
            anexo("arquivo_portaria_mapa", "Portaria de habilitação no MAPA",
                  "Pode anexar mais de um arquivo.", "Anexe a portaria de habilitação para continuar.",
                  isRequired=False, requiredIf=VINCULADO, allowMultiple=True),
            {"type": "html", "name": "aviso_proximos_passos", "html": DEPOIS},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
