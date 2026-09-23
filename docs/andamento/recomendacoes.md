# Recomendações comuns aos 14 formulários

> **Autor:** Antonio (estagiário)
> **Propósito:** padrões observados durante a auditoria de um formulário que valem para os outros. Alimenta `03-nomenclatura.md` e `04-checklist.md`.

---

## SETDIG — Solicitação de Acesso ao WordPress

!!! info "[FATO] + [RECOMENDAÇÃO] — pré-preencher com dados do gov.br"
    Na primeira etapa estão sendo pedidos os dados dos gestores, mas como o gestor é quem faz a
    solicitação, dados como **CPF, nome completo, RG, órgão expedidor e telefone** podem ser
    retirados do gov.br, seguindo o princípio da **Lei nº 13.709/2018 — LGPD**, art. 6º III
    (minimização): o governo, neste caso o gov.br, já possui esses dados.

!!! tip "[RECOMENDAÇÃO] — Setor depende de Secretaria/Órgão"
    O campo **Setor / Unidade Gestora** poderia estar ligado ao campo **Secretaria / Órgãos**.
    Assim, quando um valor é selecionado em **Secretaria / Órgãos**, o campo **Setor / Unidade
    Gestora** aparece.

    *Aplicado no `saida.json` do piloto WordPress via `visibleIf: {orgao_gestor} notempty`.*

!!! tip "[RECOMENDAÇÃO] — remoção do campo RG"
    O campo RG realmente será necessário? Com a nova carteira de identidade que utiliza o CPF
    como número do registro geral, o campo CPF já é suficiente.

!!! note "[INTERPRETAÇÃO] + [RECOMENDAÇÃO] — ordem lógica dos campos"
    Os campos estão mal distribuídos: **Secretaria / Órgãos** é o primeiro, enquanto
    **Setor / Unidade Gestora** é o penúltimo.

    **Recomendação:** dados pessoais primeiro, dados sobre o trabalho logo em seguida.

---

## Cancelar o registro de estabelecimento comercial e prestador de serviço de agrotóxico

!!! tip "[RECOMENDAÇÃO] — UF redundante"
    O campo UF realmente será necessário? O campo **município** já está preenchido com as cidades
    de MS, então o usuário só pode selecionar cidades daqui.

!!! warning "[RECOMENDAÇÃO] — lógicas não suportadas no X-Forms"
    - **Comparação entre campos**: por exemplo `cidade_origem != cidade_destino`.
    - **Data dinâmica**: os campos **data/saída** ou **data/retorno** teriam que ser maiores que
      o dia atual da solicitação, mas não há como selecionar o dia dinamicamente.

---

## Obter Selo ARTE

!!! tip "[RECOMENDAÇÃO] — campo produtos precisa ser múltiplo"
    O campo **produtos** deverá ser múltiplo para o usuário poder adicionar todos os seus
    produtos a serem vendidos.

---

## Cadastrar ou atualizar médico veterinário — avicultura ou suinocultura

!!! tip "[RECOMENDAÇÃO] — unificação de telefones em campo múltiplo"
    Foi feita a junção dos campos **Telefone** e **Telefone Adicional** em apenas um campo
    (**Telefone Contato**), onde esse campo é texto múltiplo: o **Telefone** está configurado
    como "Telefone Principal" e o **Telefone Adicional** como secundário, ambos como obrigatórios.

---

## Cadastro no Sistema Estadual de Bibliotecas Públicas

!!! tip "[RECOMENDAÇÃO] — remoção de campos desnecessários"
    Campos com baixa utilidade operacional ou complexidade desnecessária para o usuário:
    - **Descreva sua biblioteca em uma frase**: campo subjetivo e de pouco valor cadastral para o
      registro no sistema.
    - **Coordenadas Geográficas**: dado complexo para o usuário obter e preencher manualmente,
      sendo redundante quando endereço completo, CEP e município já são coletados.

!!! note "[INTERPRETAÇÃO] — obrigatoriedade do horário de funcionamento"
    O campo **Horário de funcionamento** deveria ser obrigatório? Uma biblioteca que não está em
    funcionamento (por exemplo, inativa ou temporariamente fechada) não possui horário de
    atendimento. A obrigatoriedade deveria ser revista ou condicionada à confirmação de que a
    unidade está ativa.

!!! note "[INTERPRETAÇÃO] + [RECOMENDAÇÃO] — campo Região redundante"
    O campo **Região** não faz sentido no formulário. Como o serviço é exclusivo para bibliotecas do
    estado de Mato Grosso do Sul (MS) e no campo **Município** só é possível selecionar cidades de
    MS, a resposta sempre será invariavelmente "Centro-Oeste". Mantê-lo gera etapa e atrito
    desnecessários.

!!! tip "[RECOMENDAÇÃO] — divisão da primeira etapa em duas etapas"
    A primeira etapa atual concentra o cadastro dos dados da biblioteca com 23 campos (mesmo
    removendo **Coordenadas Geográficas** e **Região**). Para evitar sobrecarga cognitiva e que o
    formulário fique excessivamente longo, recomenda-se dividi-la em duas:
    1. **Cadastro de Dados da Biblioteca** (dados principais de identificação, localização e contato);
    2. **Informações adicionais e anexos de arquivos** (dados complementares e envio de documentos).

    *Observação: avaliar a distribuição exata dos campos entre as etapas para garantir um fluxo equilibrado.*
