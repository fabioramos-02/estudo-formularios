# Pendências do estudo

O que ainda falta preencher, decidir ou corrigir antes de apresentar o padrão à SGD.
Levantamento de 30/09/2026. Quando um item for resolvido, marque o quadrado e anote o commit.

**Prioridade:** 🔴 bloqueia a apresentação · 🟡 importante · ⚪ pode esperar

---

## 1. Conteúdo a preencher

### [2. Aprendizados](02-aprendizados.md) — Antonio · 🔴

- [ ] 2.1 Por que as pessoas abandonam um formulário
- [ ] 2.2 Erros que se repetem em formulário de governo. Já existe material em
      [achados-repetem.md](andamento/achados-repetem.md), é só trazer.
- [ ] 2.3 Mensagem de erro que ajuda
- [ ] 2.4 Dado que o governo já tem (Lei 14.129/2021 e LGPD art. 6º III). Achado presente em 14 de 14.
- [ ] 2.5 Linguagem simples no formulário (Lei 15.263/2025 e Decreto 16.744/2026)
- [ ] 2.6 Acessibilidade (WCAG 2.2, critérios 3.3.x)
- [ ] 2.7 Anexos
- [ ] Tabela-resumo "Manter e evitar". A seção 2 de [recomendacoes.md](andamento/recomendacoes.md) já
      serve de base para a coluna "Manter".

### [3. Nomenclatura](03-nomenclatura.md) — Antonio · 🔴

- [ ] 3.1 Desenvolver por que separar rótulo de nome técnico
- [ ] 3.2 Convenção do nome técnico. A skill `nomenclatura-campos` já usa `snake_case`, o prefixo
      `arquivo_` e sufixos como `_gestor`. Falta levar isso para a página.
- [ ] 3.3 Como escrever o rótulo
- [ ] 3.4 Consistência entre serviços: quem mantém o dicionário
- [ ] 3.5 Coluna **Validação** vazia em 9 linhas: `nome_completo`, `email`, `telefone_celular`, `cep`,
      `logradouro`, `numero`, `bairro`, `municipio`, `uf`
- [ ] 3.5 Faltam no dicionário campos que já aparecem nos 14: `matricula`, `orgao`, `setor`, `cargo` e
      `arquivo_*`
- [ ] Resumo — o padrão proposto

### [1. Diagramação](01-diagramacao.md) — Fabio escreveu, Antonio valida · 🟡

- [ ] Revisar o rascunho e confirmar os exemplos dos 14
- [ ] Validar no X-Forms: `pageNextText`, `pagePrevText`, `completeText`, `showPreviewBeforeComplete`
- [ ] Confirmar se o X-Forms tem "salvar rascunho". Se não tiver, vira limite para a SGD.
- [ ] Levantar o texto do botão final nos 14 (item B5). Não está no mapeamento.

### [Fontes](fontes.md) — Antonio · 🟡

- [ ] Link e data de acesso das 5 normas: Lei 14.129/2021, LGPD, Lei 15.263/2025, Decreto 16.744/2026 e
      Lei 13.460/2017
- [ ] Design System gov.br (o site gov.br/ds não abre sem JavaScript; registrar a página de cada
      componente usado)
- [ ] WCAG 2.2
- [ ] Baymard Institute
- [ ] Fontes de [recomendacoesGOVUK.md](andamento/recomendacoesGOVUK.md) (datas, e-mail, nome, telefone)

### [4. Checklist](04-checklist.md) — Fabio + Antonio · ⚪

- [ ] Revisar depois das páginas 1, 2 e 3, como pede a nota no fim do checklist. Candidatos a item
      novo vindos da página 1: "pergunta de elegibilidade vem primeiro", "indicador de etapa" e
      "revisão antes do envio".

---

## 2. Inconsistências para decidir

- [ ] 🔴 **Contagens de recorrência divergem.**
    - [recomendacoes.md](andamento/recomendacoes.md) e [05-auditoria.md](05-auditoria.md) dizem "2",
      "3", "3+".
    - [achados-repetem.md](andamento/achados-repetem.md) diz "6", "mais de 8", "todos".
    - Exemplos: o RG aparece em "3+" ou em 6 formulários? O formulário longo numa página só aparece em
      2 ou em "mais de 8"?
    - Decidir qual número vale, com a lista de formulários, e alinhar os três arquivos.
- [ ] 🔴 **Códigos do checklist trocados** em `recomendacoes.md` e `05-auditoria.md`:

    | Achado | Código usado | Código certo no checklist |
    |---|---|---|
    | RG, UF, coordenadas (campo desnecessário) | C.3 | C1 |
    | Pré-preenchimento gov.br | C.1 | C2 |
    | Ordem dos campos | B.1 | A3 |
    | Formulário numa página só | A.1 | A4 / A2 |
    | Campo duplicado | C.4 | C3 |
    | Dependência entre campos | B.3 | C9 |
    | Falta de máscara | D.2 | C5 |
    | Texto livre em vez de lista | C.5 | C4 |

    [achados-repetem.md](andamento/achados-repetem.md) usa os códigos certos.
- [ ] 🔴 **Evidência errada no achado 6** ("formulário longo em 1 página"). Cita Laudos periciais e
      Bibliotecas, mas os dois têm 3 páginas no [mapeamento](andamento/mapeamento/index.md). Pelo
      mapeamento, os casos reais são: Indústria de agrotóxicos (13 campos), Cancelar registro (14),
      Laboratório avícola (14) e Negativa de tombamento (10).
- [ ] 🟡 **Anexos contados como zero.** O [mapeamento](andamento/mapeamento/index.md) mostra 0 campos
      `file` nos 14 e "Mais anexos: WordPress — 0". Mas a ficha da Soqueira tem 3 e a de Bibliotecas
      tem 5. Recontar e corrigir a coluna "Anexos" e o bloco "Extremos".
- [ ] 🟡 **Campo de data diverge da âncora.**
    - [recomendacoesGOVUK.md](andamento/recomendacoesGOVUK.md) prefere o calendário (datepicker).
    - O dicionário em [03-nomenclatura.md](03-nomenclatura.md) usa 3 campos (dia/mês/ano), que é o
      padrão GOV.UK.
    - Divergir da âncora exige justificativa escrita (regra nº 2). Decidir e alinhar.
- [ ] 🟡 **Exemplos fora da nossa realidade** em [recomendacoesGOVUK.md](andamento/recomendacoesGOVUK.md).
    - Passaporte e cartão de crédito não aparecem nos 14. Trocar por exemplos daqui: CNH, data da viagem
      (Diárias Fundect), data do atendimento (Certidão 190/193).
    - Trocar também o telefone de exemplo por um fictício.
- [ ] 🟡 **Dois sentidos de "pronto".** [05-auditoria.md](05-auditoria.md) marca os 14 como `pronto`,
      mas [andamento/index.md](andamento/index.md) diz que 2–14 estão "a fazer". Separar em duas
      colunas: **mapeado** e **refatorado**.
- [ ] ⚪ **Fichas x mapeamento.** Só existe [fichas/_template.md](fichas/_template.md). O
      [Guia do Antonio](guia-do-antonio.md) manda criar uma ficha por formulário, mas o trabalho foi
      feito em `andamento/mapeamento/`. Decidir se o mapeamento substitui as fichas e ajustar o guia e a
      nav.

---

## 3. Refatoração no X-Forms

- [ ] 🟡 Formulários 02 a 14: criar `andamento/NN-slug/` com `entrada.json` e rodar
      `/melhorar-formulario`. Só o [01 WordPress](andamento/01-wordpress/notas.md) foi feito.
- [ ] 🟡 Validar na plataforma a `[HIPÓTESE]` do WordPress: o mesmo `name` em páginas exclusivas por
      `visibleIf` grava certo?
- [ ] 🟡 Levar à SGD os limites do X-Forms: comparação entre dois campos, data dinâmica
      ("depois de hoje"), reordenação de páginas e salvar rascunho.

---

## 4. Antes de publicar

- [ ] `python -m mkdocs build --strict` sem aviso
- [ ] Atualizar a [apresentação](apresentacao/index.html) com os números corrigidos da seção 2
