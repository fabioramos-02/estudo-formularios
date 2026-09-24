# Formulários em andamento

Diário da refatoração dos **14 formulários** que sairão do FormFlow e entrarão no X-Forms.

Cada formulário ganha uma pasta numerada (`01-<slug>/`, `02-<slug>/`…) com três arquivos:

| Arquivo | O que é |
|---|---|
| `entrada.json` | JSON exportado do X-Forms atual (ou FormFlow) — a foto do formulário antes da refatoração. |
| `saida.json` | JSON após passar pelo orquestrador `/melhorar-formulario`. Este vira o import final. |
| `notas.md` | Diário da refatoração — snapshots antes/depois, mudanças de nomenclatura, diagramação e linguagem simples, com marcadores `[FATO]` / `[RECOMENDAÇÃO]` / `[HIPÓTESE]`. |

Além disso, esta seção guarda:

- [Mapeamento dos 14](mapeamento.md) — levantamento campo-a-campo do Antonio para todos os formulários (páginas, campos, tipos, obrigatoriedade).
- [Recomendações comuns](recomendacoes.md) — padrões que valem para mais de um formulário. Fonte para engrossar `03-nomenclatura.md` e `04-checklist.md`.
- Uma página por formulário com as **notas iniciais do Antonio** (levantamento manual), separada das notas da refatoração automática.

---

## Formulários

### 1. SETDIG — Solicitação de Acesso ao WordPress ✅

- [Notas do Antonio](wordpress.md)
- [Diário da refatoração](01-wordpress/notas.md)

*Redução: 51 → 32 campos (`name` únicos); 7 → 5 páginas visíveis por vez.*

### 2–14. A fazer

Ver a tabela em [Auditoria dos 14](../05-auditoria.md).

---

## Como usar as skills

1. Exportar o JSON do formulário no X-Forms.
2. Copiar para `docs/andamento/<NN>-<slug>/entrada.json`.
3. No Claude Code: `/melhorar-formulario docs/andamento/<NN>-<slug>/entrada.json`.
4. Revisar `saida.json` + `notas.md` gerados na mesma pasta.

Ver detalhe das 5 skills em `.claude/skills/` do repositório.
