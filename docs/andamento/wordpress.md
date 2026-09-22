# Notas do Antonio — SETDIG — Solicitação de Acesso ao WordPress

> Levantamento de regras, recomendações, validações e páginas feito pelo Antonio durante a
> primeira análise do formulário. Base para a refatoração automática registrada em
> [`01-wordpress/notas.md`](01-wordpress/notas.md).

---

## O que o X-Forms **não** tem hoje

!!! warning "Ferramentas ausentes na plataforma"
    - Campos multivalorados
    - Tooltip
    - Posicionamento das páginas (reordenação dinâmica)

## Estado atual do trabalho

- Foi feito o levantamento de regras, recomendação, validação e as páginas.
- Falta finalizar o questionário.

## Nome do formulário

**SETDIG — Solicitação de Acesso ao WordPress**

## Lógica de ordem das páginas

!!! info "Reordenação por perfil"
    Foi realizada a lógica da ordem das páginas:

    - Se o usuário selecionar **gestor**, a primeira página será do gestor e a segunda do
      colaborador.
    - Se o usuário selecionar **colaborador**, a ordem será inversa.

    *Como o X-Forms não suporta reordenar páginas dinamicamente, o `saida.json` refatorado
    declara as duas ordens e usa `visibleIf` por página — só a dupla correta aparece.*

## Teste de validação cruzada e-mail × órgão

!!! example "Como testar"
    Para testar a validação do e-mail, como o e-mail está ligado à secretaria/órgão:

    1. Selecionar **AGEMS — Agência Estadual de Regulação de Serviços Públicos de Mato Grosso do
       Sul (SEGOV)**.
    2. No campo e-mail, informar valor terminando em `@segov.ms.gov.br`.

    *Regra cruzada entre campos ainda não é expressável no X-Forms declarativo — anotado como
    limitação em `01-wordpress/notas.md`.*

---

## Artefatos derivados

- **JSON original:** [`01-wordpress/entrada.json`](01-wordpress/entrada.json) — export do X-Forms atual (7 páginas, 51 campos).
- **JSON refatorado:** [`01-wordpress/saida.json`](01-wordpress/saida.json) — após aplicar `/melhorar-formulario` (5 páginas visíveis, 32 nomes únicos).
- **Diário da refatoração:** [`01-wordpress/notas.md`](01-wordpress/notas.md) — snapshot antes/depois, nomenclatura, diagramação, linguagem simples.
