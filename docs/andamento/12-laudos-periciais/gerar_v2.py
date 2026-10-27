"""Gera xforms-v2.json do pedido de cópia de laudo pericial (CGP/SEJUSP). Rodar: python gerar_v2.py

Slug proposto para DEV: pedir-copia-laudo-pericial
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
CEL_RE = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
CEP_RE = r"^\d{5}-?\d{3}$"
PROCURADOR = "{perfil_solicitante} = 'procurador'"
FAMILIAR = "{perfil_solicitante} = 'familiar'"
PROC_OU_FAM = f"{PROCURADOR} or {FAMILIAR}"


def obrig(nome, msg, **kw):
    return {"name": nome, "isRequired": True, "requiredErrorText": msg, **kw}


def anexo(nome, titulo, descricao, msg, se=None):
    """se: condição para aparecer e ser obrigatório. Sem ela, o anexo é obrigatório para todos."""
    d = {"type": "file", "name": nome, "title": titulo, "description": descricao,
         "requiredErrorText": msg, "acceptedTypes": ".pdf,.jpg,.jpeg,.png", "maxSize": 5242880,
         "storeDataAsText": True, "allowMultiple": True, "waitForUpload": True}
    if se:
        d.update(visibleIf=se, requiredIf=se)
    else:
        d["isRequired"] = True
    return d


CONDICOES = (
    "<p><strong>Antes de enviar, leia as condições:</strong></p><ul>"
    "<li>A cópia do laudo só é entregue depois de confirmado que o inquérito policial ou o processo penal "
    "não está em segredo de justiça.</li>"
    "<li>Você vai receber um e-mail com as orientações para continuar o pedido e para pagar a guia DAEMS "
    "(Documento de Arrecadação do Estado de Mato Grosso do Sul).</li>"
    "<li>A cópia é cobrada por folha: 0,5 (meia) UFERMS por folha. UFERMS é a Unidade Fiscal Estadual de "
    "Referência de Mato Grosso do Sul.</li></ul>"
)

form = {
    "title": "Pedir cópia de laudo pericial",
    "description": "Para pedir cópia de laudo emitido pela Coordenadoria-Geral de Perícias (CGP), da Secretaria "
                   "de Estado de Justiça e Segurança Pública (SEJUSP). Serve para processo na Justiça, seguro "
                   "ou outra finalidade oficial.",
    "pages": [
        {"name": "perfil", "title": "Quem está fazendo o pedido", "elements": [
            {"type": "radiogroup", **obrig("perfil_solicitante", "Escolha uma opção para continuar."),
             "title": "Você é",
             "choices": [{"value": "envolvido", "text": "A pessoa envolvida no fato"},
                         {"value": "procurador", "text": "Procurador, com procuração da pessoa envolvida"},
                         {"value": "familiar", "text": "Familiar de 1º grau de vítima que faleceu"}]},
        ]},
        {"name": "seus_dados", "title": "Seus dados", "elements": [
            {"type": "text", **obrig("nome_completo", "Preencha o nome completo para continuar."),
             "title": "Seu nome completo", "autocomplete": "name",
             "tooltip": "Vem da sua conta. Corrija se estiver diferente do documento."},
            {"type": "text", **obrig("cpf", "Digite um CPF válido, com 11 números."),
             "title": "CPF", "description": "Cadastro de Pessoa Física.", "autocomplete": "cpf",
             "maskType": "pattern", "maskSettings": {"pattern": "999.999.999-99"},
             "placeholder": "000.000.000-00",
             "validators": [{"type": "regex", "regex": CPF_RE, "text": "Digite um CPF com 11 números."}]},
            {"type": "text", **obrig("data_nascimento", "Informe a data de nascimento para continuar."),
             "title": "Data de nascimento", "inputType": "date", "startWithNewLine": False,
             "maxValueExpression": "today()"},
            {"type": "text", **obrig("email", "Preencha o e-mail para continuar."),
             "title": "E-mail", "inputType": "email", "autocomplete": "email",
             "placeholder": "nome@exemplo.com.br",
             "validators": [{"type": "email", "text": "Digite um e-mail no formato nome@dominio."}],
             "tooltip": "As orientações para continuar o pedido chegam neste e-mail."},
            {"type": "text", **obrig("telefone_celular", "Digite o celular com DDD, 11 números."),
             "title": "Celular", "startWithNewLine": False, "inputType": "tel", "autocomplete": "tel",
             "maskType": "pattern", "maskSettings": {"pattern": "(99) 99999-9999"},
             "placeholder": "(00) 00000-0000",
             "validators": [{"type": "regex", "regex": CEL_RE, "text": "Digite o celular com DDD, 11 números."}]},
        ]},
        {"name": "endereco", "title": "Seu endereço", "elements": [
            {"type": "text", **obrig("cep", "Digite o CEP com 8 números."),
             "title": "CEP", "autocomplete": "postal-code",
             "maskType": "pattern", "maskSettings": {"pattern": "99999-999"}, "placeholder": "00000-000",
             "validators": [{"type": "regex", "regex": CEP_RE, "text": "Digite o CEP com 8 números."}]},
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
        {"name": "fato", "title": "Sobre o fato e o laudo", "elements": [
            {"type": "text", **obrig("nome_vitima", "Preencha o nome da vítima para continuar."),
             "title": "Nome completo da vítima", "description": "Se a vítima é você, repita o seu nome."},
            {"type": "text", "name": "nome_outorgante", "visibleIf": PROCURADOR, "requiredIf": PROCURADOR,
             "requiredErrorText": "Preencha o nome de quem deu a procuração para continuar.",
             "title": "Nome de quem deu a procuração",
             "description": "A pessoa que você representa (outorgante)."},
            {"type": "text", **obrig("data_fato", "Informe a data do fato para continuar."),
             "title": "Data do fato", "inputType": "date", "maxValueExpression": "today()"},
            {"type": "text", "name": "numero_ocorrencia",
             "title": "Número do boletim de ocorrência, do inquérito ou do processo penal",
             "description": "Se tiver. Ajuda a encontrar o laudo."},
            {"type": "text", "name": "local_fato", "title": "Onde o fato aconteceu",
             "description": "Rua, bairro, cidade e CEP, se souber."},
            {"type": "checkbox", "name": "tipo_laudo", "title": "Tipo de laudo",
             "description": "Pode marcar mais de um. Se não souber, deixe em branco.",
             "choices": [{"value": "analises_laboratoriais", "text": "Análises laboratoriais"},
                         {"value": "criminalistica", "text": "Criminalística"},
                         {"value": "identificacao", "text": "Identificação"},
                         {"value": "medicina_legal", "text": "Medicina legal"}]},
            {"type": "comment", **obrig("descricao_fato", "Conte o que aconteceu para continuar."),
             "title": "O que aconteceu", "description": "Conte em poucas linhas."},
            {"type": "comment", "name": "informacoes_adicionais", "title": "Informações adicionais",
             "description": "Se quiser, acrescente algo que ajude no pedido."},
        ]},
        {"name": "documentos", "title": "Documentos",
         "description": "Arquivos em PDF, JPG ou PNG, até 5 MB cada. Pode anexar mais de um arquivo, como a frente e o verso do documento.",
         "elements": [
             anexo("arquivo_documento_identificacao_envolvido", "Documento de identificação da pessoa envolvida no fato",
                   "Se a pessoa envolvida é você, anexe o seu documento.",
                   "Anexe o documento de identificação da pessoa envolvida para continuar."),
             anexo("arquivo_documento_identificacao_solicitante", "Seu documento de identificação",
                   "Documento de quem está fazendo o pedido.",
                   "Anexe o seu documento de identificação para continuar.", se=PROC_OU_FAM),
             anexo("arquivo_procuracao", "Procuração", "A procuração dada pela pessoa que você representa.",
                   "Anexe a procuração para continuar.", se=PROCURADOR),
             anexo("arquivo_comprovante_parentesco", "Comprovante de parentesco",
                   "Documento que mostra o seu parentesco com a vítima.",
                   "Anexe o comprovante de parentesco para continuar.", se=FAMILIAR),
         ]},
        {"name": "condicoes", "title": "Condições do pedido", "elements": [
            {"type": "html", "name": "texto_condicoes", "html": CONDICOES},
            {"type": "checkbox", **obrig("aceite_condicoes", "Marque que está ciente das condições para enviar."),
             "title": "Confirmação",
             "choices": [{"value": "ciente", "text": "Li e estou ciente das condições acima."}]},
            {"type": "html", "name": "aviso_proximos_passos",
             "html": "<p><strong>Depois do envio:</strong> a CGP manda para o e-mail informado as orientações para "
                     "continuar o pedido e para pagar a guia DAEMS.</p>"},
        ]},
    ],
    "showProgressBar": "top",
    "showQuestionNumbers": "off",
}

Path(__file__).with_name("xforms-v2.json").write_text(json.dumps(form, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
