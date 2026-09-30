# 1. Diagramação de formulários

> **Status:** rascunho — Fabio, a validar com Antonio
> **Pergunta desta página:** como dispor os campos na tela para a pessoa preencher rápido e sem errar?

Leia antes o [Guia do Antonio](guia-do-antonio.md). Use os marcadores `[FATO]`, `[INTERPRETAÇÃO]` e
`[RECOMENDAÇÃO]` e registre cada fonte em [fontes.md](fontes.md).

!!! warning "Filtro aplicado nesta página"
    Uma regra do GOV.UK ou do gov.br só entrou aqui se passou em três perguntas:

    1. Resolve um problema visto em pelo menos um dos [14 formulários](andamento/mapeamento/index.md)?
    2. Faz sentido no Portal MS: login gov.br, CPF/CNPJ, municípios de MS, servidor e empresa como público?
    3. O X-Forms consegue fazer? Se não, a regra vira limite a levar à SGD.

    Ficou de fora o que só existe no Reino Unido: passaporte, visto, *postcode*, *National Insurance*.
    Cada seção termina com **Onde aparece nos 14**.

---

## 1.1. Uma pergunta por tela ou tudo de uma vez?

*Quando vale quebrar o formulário em etapas? Quando a quebra atrapalha? O que muda em formulário
curto e em formulário longo com anexo?*

- **[FATO]** O GOV.UK orienta a começar com uma coisa por página. Juntar perguntas só quando a
  pesquisa com usuários mostrar que ajuda (GOV.UK — Form structure).
- **[FATO]** O guia federal manda quebrar formulário longo em etapas menores, com indicador de
  progresso. Também manda retirar o que pode vir de outra base (gov.br — Simplificação de formulários,
  prática 2).
- **[FATO]** O GOV.UK põe as perguntas de elegibilidade primeiro, para ninguém perder tempo com um
  pedido que não vai ser aceito (GOV.UK — Form structure).
- **[INTERPRETAÇÃO]** No Portal MS, "uma por página" ao pé da letra geraria 20 ou 30 cliques em
  formulário de empresa ou de servidor. A âncora federal fala em **etapas**, não em uma pergunta por
  tela. Adotamos a leitura federal, com uma exceção: a pergunta que **muda o caminho** fica sozinha.
- **[RECOMENDAÇÃO]**
    - Pergunta que muda o fluxo fica sozinha na página: perfil, tipo de pedido, "é para você ou para
      outra pessoa?".
    - A pergunta de elegibilidade vem primeiro. Exemplo: a Certidão 190/193 só atende 4 cidades, então
      a cidade é perguntada antes de tudo.
    - O resto é agrupado por assunto em etapas (ver 1.2).
    - Formulário de até ~8 campos do mesmo assunto pode ficar numa página só.
    - Anexo ganha etapa própria quando há mais de um arquivo.

**Onde aparece nos 14:** 7 de 14 formulários estão numa página só. Quatro deles passam de 10 campos:
Indústria de agrotóxicos (13), Cancelar registro (14), Laboratório avícola (14) e Negativa de
tombamento (10). O perfil do [WordPress](andamento/01-wordpress/notas.md) já virou página própria.
O modelo a replicar é o **Diárias Fundect**, com 3 etapas: servidor → viagem → dados bancários.

## 1.2. Agrupamento dos campos

*O que justifica agrupar: o assunto, a origem do dado, quem responde? Quantos campos por grupo?
Grupo precisa de título?*

- **[FATO]** O guia federal manda agrupar informações relacionadas perto umas das outras (gov.br —
  prática 4).
- **[FATO]** O mesmo guia manda perguntar se a pessoa quer **reaproveitar** o que já digitou,
  como dados do requerente e do interessado, ou endereço (gov.br — prática 6).
- **[FATO]** O GOV.UK pede título de página específico ao que se pergunta, não o nome genérico do
  setor (GOV.UK — Question pages).
- **[RECOMENDAÇÃO]**
    - Agrupar por **quem responde** primeiro e por **assunto** depois. Dados do gestor numa etapa, do
      colaborador em outra. Não misturar.
    - Toda etapa tem título que diz o que se pede: "Dados do servidor", "Dados da viagem". Nada de
      "Página 1".
    - Quando duas pessoas têm o mesmo dado (requerente e interessado, gestor e colaborador), perguntar
      "É a mesma pessoa?" antes de repetir o bloco.
    - Limite de trabalho: ~8 campos por etapa. Até 10 se forem todos do mesmo assunto (endereço).
      **[HIPÓTESE]** Número herdado da skill `regras-diagramacao`, ainda sem pesquisa que o confirme.

**Onde aparece nos 14:** o WordPress duplicava o bloco inteiro de gestor e colaborador (19 campos
repetidos). Laudos periciais tem requerente e interessado. Achados C3 (campos espalhados) e C9
(campos ligados sem dependência) em [achados-repetem.md](andamento/achados-repetem.md).

## 1.3. Ordem dos campos

*Que ordem reduz esforço? Dado fácil primeiro? Dado pessoal antes ou depois do dado do pedido?
Onde entra o anexo?*

- **[FATO]** O guia federal pede um caminho simples e rápido para quem preenche (gov.br — prática 3).
- **[FATO]** O GOV.UK usa perguntas com ramificação: a pessoa só responde o que vale para o caso dela
  (GOV.UK — Form structure).
- **[RECOMENDAÇÃO]** Ordem das etapas:
    1. **Escolha** (o que quer fazer), se houver bifurcação.
    2. **Identificação** (quem é). Vem do login gov.br sempre que possível.
    3. **Vínculo** (onde trabalha, qual empresa), se houver.
    4. **Pedido** (o que quer, especificamente).
    5. **Anexos**.
    6. **Revisão** antes de enviar (ver 1.7).
- **[RECOMENDAÇÃO]** Dentro de cada etapa:
    - O campo pai vem antes do filho e encostado nele: órgão → setor, CEP → endereço, município →
      bairro.
    - O filho só aparece depois que o pai foi preenchido (`visibleIf`).
    - Endereço segue a ordem de quem escreve um envelope no Brasil: CEP, logradouro, número,
      complemento, bairro, município.
- **[INTERPRETAÇÃO]** Pôr o dado pessoal primeiro só funciona se ele vier pronto do gov.br. Se o
  cidadão tiver que digitar tudo, a etapa 2 vira a mais cansativa logo no início.

**Onde aparece nos 14:** a ordem fora da lógica aparece em todos (achado A2). No WordPress, *Setor*
era o penúltimo campo, longe de *Órgão*. Há CEP no topo e cidade no fim. Detalhe em
[recomendacoes.md](andamento/recomendacoes.md).

## 1.4. Layout: coluna única, largura e tamanho do campo

*Uma coluna ou duas? O tamanho da caixa deve sugerir o tamanho da resposta? O que acontece no
celular?*

- **[FATO]** O guia federal manda usar coluna única, porque a pessoa preenche mais rápido (gov.br —
  prática 1) e evita layout com várias colunas (prática 3).
- **[FATO]** O GOV.UK limita a área do formulário a dois terços da tela, para a leitura ficar
  confortável (GOV.UK — Question pages).
- **[FATO]** A NN/g recomenda coluna única: várias colunas quebram o movimento de descer pelo
  formulário (NN/g — Website forms usability, 2016).
- **[RECOMENDAÇÃO]**
    - Um campo por linha, sempre. Não usar `startWithNewLine: false` para pôr dois campos lado a lado.
    - A largura da caixa sugere a resposta: CEP e número curtos, nome e e-mail longos.
    - Texto longo é caixa de várias linhas (`comment`), não campo de uma linha.
    - Todo formulário é testado no celular antes de publicar (checklist A7).

**Onde aparece nos 14:** o `entrada.json` do WordPress tem 11 campos com `startWithNewLine: false`,
ou seja, lado a lado. Itens A1, A6 e A7 do [checklist](04-checklist.md#a-organizacao).

## 1.5. Obrigatório x opcional

*Marca-se o obrigatório ou o opcional? Com qual símbolo ou palavra? Onde a regra fica explicada?*

- **[FATO]** O GOV.UK marca só o opcional, com a palavra "(opcional)", e não usa asterisco (GOV.UK —
  Question pages).
- **[FATO]** A NN/g recomenda o contrário: marcar todo campo obrigatório, com asterisco antes do rótulo
  (NN/g — Marking required fields, 2019).
- **[FATO]** O guia federal só pede para deixar claro o que é pedido, sem fixar símbolo (gov.br —
  práticas 7 e 8).
- **[FATO]** Nos 14 formulários, 187 de 223 campos são obrigatórios (84%)
  ([mapeamento](andamento/mapeamento/index.md)).
- **[RECOMENDAÇÃO]** Divergência resolvida pela nossa realidade:
    - Manter o asterisco que o X-Forms já põe no campo obrigatório (`isRequired`). É o que o cidadão
      já vê no Portal, e trocar exigiria mudar a ferramenta.
    - Escrever **"(opcional)"** no rótulo dos poucos campos opcionais. Com 84% obrigatórios, o
      opcional é a exceção, e a exceção é o que precisa de destaque. Essa parte segue o GOV.UK.
    - Explicar o asterisco uma vez, no topo do formulário: "Campos com * são obrigatórios."
    - Antes de marcar um campo como obrigatório, perguntar se o serviço anda sem ele. Se anda, o
      campo sai (checklist C1).

**Onde aparece nos 14:** 7 formulários têm 100% dos campos obrigatórios (WordPress, RT agrícola,
Indústria de agrotóxicos, Cancelar registro, Selo Arte, Negativa de tombamento, Soqueira). Isso
mostra que a marcação não está sendo usada para decidir se o campo é necessário.

## 1.6. Botões e ação principal

*Onde fica o botão de enviar? Quantos botões por tela? Como escrever o texto do botão? Existe
"voltar" e "salvar rascunho"?*

- **[FATO]** O GOV.UK recomenda um só botão principal por página. Mais de uma ação principal confunde
  o próximo passo (GOV.UK — Button).
- **[FATO]** O texto do botão diz a ação: "Continuar", "Enviar solicitação". O GOV.UK prefere
  "Continuar" a "Próximo" e mantém um link "Voltar" em toda página de pergunta (GOV.UK — Button e
  Question pages).
- **[FATO]** O guia federal pede botão com texto que revele o que acontece depois do clique (gov.br —
  prática 5).
- **[RECOMENDAÇÃO]**
    - Um botão principal por etapa, no fim da etapa.
    - Nas etapas intermediárias o botão diz "Continuar". Na última, "Enviar solicitação" ou o nome do
      pedido ("Solicitar certidão"). Nunca "OK" ou "Concluir".
    - Toda etapa depois da primeira tem "Voltar", e o que foi preenchido não se perde (checklist A5).
    - No X-Forms (SurveyJS), os textos saem de `pageNextText`, `pagePrevText` e `completeText`.
      **[HIPÓTESE]** Validar se o X-Forms expõe esses campos no editor.
    - **Salvar rascunho:** **Não identificado** no X-Forms. Levar à SGD como limite, porque pesa nos
      formulários com anexo que a pessoa precisa ir buscar (Soqueira, Bibliotecas).

**Onde aparece nos 14:** item B5 do [checklist](04-checklist.md#b-linguagem). O texto do botão final
não aparece no mapeamento. **Não identificado** para os 14; conferir na próxima rodada.

## 1.7. Progresso em fluxo de várias etapas

*Como mostrar em que ponto a pessoa está? Barra, "etapa 2 de 5", lista lateral? Dá para voltar e
corrigir?*

- **[FATO]** O guia federal manda informar em que etapa a pessoa está (gov.br — prática 12).
- **[FATO]** O GOV.UK sugere um indicador simples, do tipo "Pergunta 3 de 9". Recomenda testar primeiro
  sem ele e evitar indicador que mostre todas as perguntas de uma vez (GOV.UK — Question pages).
- **[FATO]** O GOV.UK usa uma página de revisão antes do envio. Ela mostra cada resposta com um link
  "Alterar" e, depois da correção, volta direto para a revisão (GOV.UK — Check answers).
- **[RECOMENDAÇÃO]**
    - Com 2 etapas ou mais, mostrar "Etapa X de Y" com o título da etapa. No X-Forms:
      `showProgressBar: "top"` e `progressBarType: "pages"`, como no `saida.json` do WordPress.
    - Com 3 etapas ou mais, ativar a revisão antes do envio (`showPreviewBeforeComplete`).
      **[HIPÓTESE]** Validar se o X-Forms suporta.
    - Contar só as etapas que a pessoa vai ver. Página escondida por `visibleIf` não entra no "de Y".
    - Depois do envio, dizer o que acontece: protocolo, prazo, por onde vem a resposta (gov.br —
      prática 13; checklist B6).

**Onde aparece nos 14:** 7 formulários têm 2 páginas ou mais e nenhum tem revisão antes do envio
mapeada. O WordPress refatorado já usa a barra de progresso por páginas.

---

## Resumo — o que recomendamos

Regras de diagramação para o X-Forms, na ordem em que o cidadão as sente:

1. **Pergunta que muda o caminho fica sozinha na página.** A de elegibilidade vem primeiro. (1.1)
2. **O resto vai em etapas por assunto**, com ~8 campos cada e título que diz o que se pede. (1.1, 1.2)
3. **Ordem das etapas:** escolha → identificação → vínculo → pedido → anexos → revisão. (1.3)
4. **Campo pai antes do filho**, encostados, e o filho só aparece depois do pai (`visibleIf`). (1.3)
5. **Dado do gov.br vem pronto.** Se duas pessoas repetem dados, perguntar "é a mesma pessoa?". (1.2, 1.3)
6. **Uma coluna só.** Nada de `startWithNewLine: false`. A caixa tem o tamanho da resposta. (1.4)
7. **Asterisco no obrigatório** (padrão do X-Forms) **e "(opcional)" no rótulo do opcional.** (1.5)
8. **Um botão principal por etapa**, com verbo: "Continuar" e, no fim, "Enviar solicitação". (1.6)
9. **"Etapa X de Y"** a partir de 2 etapas e **revisão antes do envio** a partir de 3. (1.7)
10. **Limites a levar à SGD:** salvar rascunho e confirmação das propriedades do SurveyJS no X-Forms. (1.6, 1.7)

Estas regras alimentam a seção A do [checklist](04-checklist.md#a-organizacao) e a skill
`regras-diagramacao` (`.claude/skills/regras-diagramacao/SKILL.md`).
