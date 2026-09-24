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

---

## Cadastrar ou atualizar empresa integradora de ave ou suíno

!!! tip "[RECOMENDAÇÃO] — remoção dos campos via de acesso e coordenadas geográficas"
    Campos dispensáveis para a localização e cadastro da empresa:
    - **Via de acesso**: com as ferramentas atuais de navegação e mapas, apenas o endereço
      completo da empresa já é suficiente para localizá-la, tornando desnecessária a inserção
      manual de pontos de referência.
    - **Coordenadas Geográficas**: dado excessivamente técnico que a maioria das empresas não sabe
      informar de imediato.

    Além disso, ambos os campos atualmente não são obrigatórios. Na prática, a grande maioria dos
    usuários, mesmo tendo esses dados, prefere não preenchê-los para poupar tempo. Mantê-los no
    formulário gera atrito e poluição visual desnecessários.

---

## Solicitar cópia de laudos periciais

!!! tip "[RECOMENDAÇÃO] — remoção dos campos RG e Órgão expedidor"
    Com a nova carteira de identidade nacional que adota o CPF como número único do registro geral,
    os campos **RG** e **Órgão expedidor** tornam-se redundantes. Apenas o campo **CPF** é
    suficiente para a identificação do usuário, simplificando o preenchimento.

!!! tip "[RECOMENDAÇÃO] — divisão do formulário em 3 etapas"
    Atualmente o formulário concentra todos os campos em uma única página, prejudicando a
    legibilidade e o fluxo do usuário. Recomenda-se dividi-lo em 3 etapas lógicas:
    1. **Dados do Solicitante**: informações da pessoa que está requerendo a cópia do laudo pericial;
    2. **Dados da Vítima**: identificação da vítima do evento;
    3. **Dados do Evento**: dados específicos da ocorrência, como informações sobre o inquérito
       policial ou boletim de ocorrência (B.O.).

---

## Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola

!!! tip "[RECOMENDAÇÃO] — campos de endereço condicionais ao CEP"
    Os campos relacionados a endereço (como logradouro, bairro e município) poderiam iniciar
    invisíveis e ser exibidos apenas após o usuário preencher o **CEP**. Como o CEP é um campo
    sempre obrigatório e comum a formulários com endereço, essa lógica condicional diminui a
    poluição visual inicial da tela.

!!! tip "[RECOMENDAÇÃO] — alinhamento lado a lado de Telefone e E-mail"
    Organizar os campos **Telefone** e **E-mail** em duas colunas (lado a lado). Como ambos
    tratam de meios de contato e contêm textos curtos, a leitura e a digitação ficam mais práticas,
    sem risco de quebra de layout, além de economizar espaço vertical no formulário.

!!! tip "[RECOMENDAÇÃO] — alinhamento lado a lado de Estado (UF) e Município"
    Os campos **Estado (UF)** e **Município** também devem ficar alinhados lado a lado, pois
    possuem relação direta de dependência e ocupam pouco espaço horizontal (especialmente a UF
    com apenas 2 dígitos), otimizando a leitura e a disposição dos dados de localização.

!!! tip "[RECOMENDAÇÃO] — uso de campos de seleção para dados padronizados"
    Campos que possuem valores universais ou tabelados (como **Estado/UF** ou **Cor/Raça**) devem
    ser estruturados como listas de seleção (`select`/`dropdown`) ou botões de escolha, em vez de
    campos de texto aberto. Isso elimina o risco de erros de digitação ou divergências de grafia,
    garantindo a integridade dos dados coletados.

!!! tip "[RECOMENDAÇÃO] — sintetizar a descrição do serviço"
    Manter a descrição do serviço no cabeçalho do formulário sempre enxuta para não empurrar os
    campos para baixo e aumentar desnecessariamente o tamanho da página. A descrição pode ser
    sintetizada (inclusive com auxílio de IA) para focar apenas nas informações essenciais ao cidadão.

!!! tip "[RECOMENDAÇÃO] — máscaras de entrada em campos com tamanho fixo"
    Adicionar máscaras nos campos que possuem formato e quantidade de caracteres pré-determinados:
    - **CPF**: `999.999.999-99`
    - **CEP**: `99999-999`
    - **Telefone**: `(99) 99999-9999`

    *Nota técnica X-Forms:* o X-Forms lê o dígito `9` como máscara numérica (renderizando `_` para o
    usuário, por exemplo `___.___.___-__`). Isso impede que o cidadão preencha o dado incorretamente
    ou com quantidade incompleta de caracteres, garantindo a validação antes do envio.

---

## Solicitar emissão de certidão de atendimento de emergência

!!! tip "[RECOMENDAÇÃO] — unificação dos campos de endereço em campo único"
    Os campos **Endereço (rua ou avenida)**, **Bairro** e **Número do imóvel** podem ser
    mesclados em um único campo de texto, evitando a fragmentação excessiva de campos e a poluição
    visual no formulário.

    *Orientação no campo:* a descrição ou texto de ajuda deve orientar o cidadão a preencher no
    formato preferencial: `Bairro / Rua ou Avenida / Número do imóvel`.





