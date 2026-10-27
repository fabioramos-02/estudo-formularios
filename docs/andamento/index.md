# Formulários em andamento

Diário da refatoração dos **14 formulários** que sairão do FormFlow e entrarão no X-Forms.

Cada formulário ganha uma pasta numerada (`01-<slug>/`, `02-<slug>/`…) com três arquivos:

| Arquivo | O que é |
|---|---|
| `entrada.json` | JSON exportado do X-Forms atual (ou FormFlow) — a foto do formulário antes da refatoração. |
| `saida.json` | JSON após passar pelo orquestrador `/melhorar-formulario`. Este vira o import final. |
| `notas.md` | Diário da refatoração — snapshots antes/depois, mudanças de nomenclatura, diagramação e linguagem simples, com marcadores `[FATO]` / `[RECOMENDAÇÃO]` / `[HIPÓTESE]`. |

Além disso, esta seção guarda:

- [Mapeamento dos 14](mapeamento/index.md) — visão estratégica com tabela comparativa e link para cada formulário mapeado campo-a-campo pelo Antonio.
- [Recomendações comuns](recomendacoes.md) — padrões que valem para mais de um formulário. Fonte para engrossar `03-nomenclatura.md` e `04-checklist.md`.
- Uma página por formulário com as **notas iniciais do Antonio** (levantamento manual), separada das notas da refatoração automática.

---

## Formulários

### 1. SETDIG — Solicitação de Acesso ao WordPress ✅

- [Notas do Antonio](wordpress.md)
- [Diário da refatoração](01-wordpress/notas.md)

*Redução: 51 → 32 campos (`name` únicos); 7 → 5 páginas visíveis por vez.*
*Versão 2 no X-Forms e X-Flows de DEV desde 27/10/2026 — ver o fim do diário.*

### 2. Fundect — Pedir diárias e passagens ✅

- [Diário da refatoração](02-diarias-fundect/notas.md)

*No X-Forms e X-Flows de DEV desde 27/10/2026. Corrigido: o servidor não conseguia enviar (dados bancários obrigatórios para todos).*

### 3. IAGRO — Cadastro de responsável técnico agrícola ✅

- [Notas do Antonio](mapeamento/02-rt-agricola.md)
- [Diário da refatoração](03-rt-agricola/notas.md)

*No X-Forms e X-Flows de DEV desde 27/10/2026. Uma página com 8 campos virou três páginas curtas; nome, CPF e e-mail vêm da conta.*

### 4–14. A fazer

Ver a tabela em [Auditoria dos 14](../05-auditoria.md).

---

## Como usar as skills

1. Exportar o JSON do formulário no X-Forms.
2. Copiar para `docs/andamento/<NN>-<slug>/entrada.json`.
3. No Claude Code: `/melhorar-formulario docs/andamento/<NN>-<slug>/entrada.json`.
4. Revisar `saida.json` + `notas.md` gerados na mesma pasta.

Ver detalhe das 5 skills em `.claude/skills/` do repositório.
