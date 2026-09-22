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

!!! tip "[RECOMENDAÇÃO] — unificação de telefones"
    Foi feita a junção dos campos **Telefone** e **Telefone Adicional** em um único campo
    **Telefone Contato**, do tipo texto múltiplo:

    - **Telefone Principal** — Telefone
    - **Telefone Adicional** — Telefone Adicional

    Ambos obrigatórios.
