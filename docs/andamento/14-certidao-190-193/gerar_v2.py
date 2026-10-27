"""Gera xforms-v2.json do pedido de certidão de atendimento de emergência 190/193 (SEJUSP). Rodar: python gerar_v2.py

Slug proposto para DEV: pedir-certidao-atendimento-190-193
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
# ponytail: os 79 municípios de MS vêm da v1, que já tinha a lista conferida
_v1 = json.loads((AQUI / "xforms-v1-demo.json").read_text(encoding="utf-8"))
MUNICIPIOS_MS = next(e["choices"] for p in _v1["pages"] for e in p["elements"] if e["name"] == "cidade_ligou")
CIDADES_ATENDIDAS = ["Campo Grande", "Dourados", "Corumbá", "Ponta Porã"]

CPF_RE = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
CEL_RE = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
OUTRA_PESSOA = "{perfil_solicitante} = 'representante_legal' or {perfil_solicitante} = 'procurador'"
PROCURADOR = "{perfil_solicitante} = 'procurador'"
CIDADE_FORA = "{municipio_ocorrencia} notempty and " + " and ".join(
    f"{{municipio_ocorrencia}} <> '{c}'" for c in CIDADES_ATENDIDAS)


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg=None, se=None, multiplos=False):
    """msg sem se: obrigatório para todos. se: aparece e é obrigatório só nesse caso. Sem msg: opcional."""
    d = {"type": "file", "name": nome, "title": titulo, "description": descricao,
         "acceptedTypes": ".pdf", "maxSize": 5242880, "storeDataAsText": True,
         "allowMultiple": multiplos, "waitForUpload": True}
    if msg:
        d["requiredErrorText"] = msg
        if se:
            d.update(visibleIf=se, requiredIf=se)
        else:
            d["isRequired"] = True
    return d


form = {
    "title": "Pedir certidão de atendimento de emergência (190 ou 193)",
    "description": "Para quem precisa de uma certidão oficial que comprove a ligação para o 190 (Polícia Militar) "
                   "ou para o 193 (Corpo de Bombeiros). Vale para ligações feitas nas cidades de Campo Grande, "
                   "Dourados, Corumbá e Ponta Porã. Serve para uso pessoal, administrativo ou na Justiça.",
    "pages": [
        {"name": "chamada", "title": "Sobre a ligação", "elements": [
            {"type": "radiogroup", **obrig("numero_emergencia", "Escolha o número para continuar."),
             "title": "Para qual número foi feita a ligação?",
             "choices": [{"value": "190", "text": "190 — Polícia Militar"},
                         {"value": "193", "text": "193 — Corpo de Bombeiros"}]},
            {"type": "dropdown", **obrig("municipio_ocorrencia", "Escolha a cidade para continuar."),
             "title": "Em que cidade aconteceu o fato?", "placeholder": "Selecione",
             "choices": MUNICIPIOS_MS},
            {"type": "html", "name": "aviso_cidade", "visibleIf": CIDADE_FORA,
             "html": "<p><strong>Atenção:</strong> este serviço vale para ligações feitas em Campo Grande, "
                     "Dourados, Corumbá e Ponta Porã. Para outra cidade, o pedido pode não ser atendido.</p>"},
        ]},
        {"name": "perfil", "title": "Quem está fazendo o pedido", "elements": [
            {"type": "radiogroup", **obrig("perfil_solicitante", "Escolha uma opção para continuar."),
             "title": "Você é",
             "choices": [{"value": "proprio", "text": "A pessoa que fez a ligação"},
                         {"value": "representante_legal", "text": "Representante legal de quem fez a ligação"},
                         {"value": "procurador", "text": "Procurador, com procuração de quem fez a ligação"}]},
        ]},
        {"name": "seus_dados", "title": "Seus dados para contato", "elements": [
            {"type": "text", "name": "nome_completo", "visibleIf": OUTRA_PESSOA, "requiredIf": OUTRA_PESSOA,
             "requiredErrorText": "Preencha o seu nome completo para continuar.",
             "title": "Seu nome completo", "autocomplete": "name",
             "tooltip": "Vem da sua conta. Corrija se estiver diferente do documento."},
            {"type": "text", **obrig("email", "Preencha o e-mail para continuar."),
             "title": "Seu e-mail", "inputType": "email", "autocomplete": "email",
             "placeholder": "nome@exemplo.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "A resposta do pedido chega neste e-mail."},
            {"type": "text", **obrig("telefone_celular", "Digite o celular com DDD, 11 números."),
             "title": "Seu celular", "description": "De preferência com WhatsApp.",
             "inputType": "tel", "autocomplete": "tel",
             "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
             "placeholder": "(00) 00000-0000",
             "validators": [{"type": "regex", "regex": CEL_RE, "text": "Digite o celular com DDD, 11 números."}]},
        ]},
        {"name": "quem_ligou", "title": "Quem fez a ligação", "elements": [
            {"type": "text", **obrig("nome_completo_ligou", "Preencha o nome de quem ligou para continuar."),
             "title": "Nome completo de quem ligou", "autocomplete": "name",
             "resetValueIf": OUTRA_PESSOA},
            {"type": "text", **obrig("cpf_ligou", "Digite um CPF válido, com 11 números."),
             "title": "CPF de quem ligou", "description": "Cadastro de Pessoa Física.", "autocomplete": "cpf",
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"},
             "placeholder": "000.000.000-00", "resetValueIf": OUTRA_PESSOA,
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite um CPF com 11 números."}]},
            {"type": "text", **obrig("data_nascimento_ligou", "Informe a data de nascimento para continuar."),
             "title": "Data de nascimento de quem ligou", "inputType": "date", "startWithNewLine": False,
             "maxValueExpression": "today()"},
            {"type": "text", **obrig("logradouro_ligou", "Preencha o endereço para continuar."),
             "title": "Endereço de quem ligou", "description": "Rua ou avenida, número e bairro.",
             "autocomplete": "street-address"},
            {"type": "text", "name": "complemento_ligou", "title": "Complemento",
             "description": "Se tiver. Ex.: casa, apartamento, perto de mercado ou escola."},
            {"type": "dropdown", **obrig("municipio_ligou", "Escolha a cidade para continuar."),
             "title": "Cidade", "placeholder": "Selecione", "choices": MUNICIPIOS_MS},
        ]},
        {"name": "ocorrencia", "title": "O que aconteceu", "elements": [
            {"type": "text", **obrig("endereco_ocorrencia", "Preencha o endereço do fato para continuar."),
             "title": "Onde aconteceu o fato",
             "description": "Rua ou avenida, número e bairro. Se não houver número, escreva \"sem número\"."},
            {"type": "text", **obrig("data_fato", "Informe a data do fato para continuar."),
             "title": "Data do fato", "inputType": "date", "maxValueExpression": "today()"},
            {"type": "text", "name": "hora_fato", "title": "Hora aproximada",
             "description": "Se não souber, deixe em branco.", "inputType": "time", "startWithNewLine": False},
            {"type": "comment", **obrig("descricao_ocorrencia", "Conte o que aconteceu para continuar."),
             "title": "Conte o que aconteceu",
             "description": "Em poucas linhas: o que aconteceu e por que você ligou para a emergência."},
            {"type": "text", **obrig("finalidade_certidao", "Diga para que precisa da certidão para continuar."),
             "title": "Para que você precisa da certidão?", "description": "Ex.: processo na Justiça."},
            {"type": "comment", "name": "informacoes_adicionais", "title": "Informações adicionais",
             "description": "Se quiser, acrescente algo que ajude na análise."},
        ]},
        {"name": "documentos", "title": "Documentos", "description": "Arquivos em PDF, até 5 MB cada.", "elements": [
            anexo("arquivo_documento_identificacao", "Documento de identificação de quem ligou",
                  "Um documento com o número do CPF, como RG ou CNH.",
                  "Anexe o documento de identificação para continuar."),
            anexo("arquivo_documento_representante", "Seu documento de identificação",
                  "Documento do representante legal ou do procurador.",
                  "Anexe o seu documento de identificação para continuar.", se=OUTRA_PESSOA),
            anexo("arquivo_procuracao", "Procuração", "A procuração dada por quem fez a ligação.",
                  "Anexe a procuração para continuar.", se=PROCURADOR),
            anexo("arquivo_outros_documentos", "Outros documentos",
                  "Se tiver, anexe documentos que ajudem na análise. Pode anexar mais de um.", multiplos=True),
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a SEJUSP analisa o pedido e a resposta chega no e-mail informado.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

(AQUI / "xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
