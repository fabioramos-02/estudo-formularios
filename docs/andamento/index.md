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

### 4. IAGRO — Cadastrar indústria de agrotóxicos no e-Saniagro ✅

- [Notas do Antonio](mapeamento/04-industria-agrotoxicos.md)
- [Diário da refatoração](04-industria-agrotoxicos/notas.md)

*No X-Forms e X-Flows de DEV desde 27/10/2026. Corrigido: a procuração era obrigatória para todos; agora só para consultoria.*

### 5. IAGRO — Cancelar registro de empresa de agrotóxicos ✅

- [Notas do Antonio](mapeamento/05-cancelar-agrotoxicos.md)
- [Diário da refatoração](05-cancelar-agrotoxicos/notas.md)

*No X-Forms e X-Flows de DEV desde 27/10/2026. Saíram RG, órgão expedidor e UF do órgão; entrou e-mail para a resposta.*

### 6. IAGRO — Pedir o Selo Arte — rascunho

- [Notas do Antonio](mapeamento/06-selo-arte.md)
- [Rascunho da refatoração](06-selo-arte/notas.md)

### 7. FCMS — Pedir certidão negativa de tombamento — rascunho

- [Notas do Antonio](mapeamento/07-negativa-tombamento.md)
- [Rascunho da refatoração](07-negativa-tombamento/notas.md)

### 8. IAGRO — Cadastrar ou atualizar médico veterinário de aves ou suínos — rascunho

- [Notas do Antonio](mapeamento/08-veterinario-avi-suino.md)
- [Rascunho da refatoração](08-veterinario-avi-suino/notas.md)

### 9. FCMS — Cadastrar biblioteca no Sistema Estadual de Bibliotecas Públicas — rascunho

- [Notas do Antonio](mapeamento/09-bibliotecas-publicas.md)
- [Rascunho da refatoração](09-bibliotecas-publicas/notas.md)

### 10. IAGRO — Cadastrar ou atualizar empresa integradora de aves ou suínos — rascunho

- [Notas do Antonio](mapeamento/10-empresa-integradora.md)
- [Rascunho da refatoração](10-empresa-integradora/notas.md)

### 11. IAGRO — Pedir certificado de destruição de soqueira de algodão — rascunho

- [Notas do Antonio](mapeamento/11-soqueira-algodao.md)
- [Rascunho da refatoração](11-soqueira-algodao/notas.md)

### 12. CGP/SEJUSP — Pedir cópia de laudo pericial — rascunho

- [Notas do Antonio](mapeamento/12-laudos-periciais.md)
- [Rascunho da refatoração](12-laudos-periciais/notas.md)

### 13. IAGRO — Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola — rascunho

- [Notas do Antonio](mapeamento/13-laboratorio-avicola.md)
- [Rascunho da refatoração](13-laboratorio-avicola/notas.md)

### 14. SEJUSP — Pedir certidão de atendimento de emergência (190 ou 193) — rascunho

- [Notas do Antonio](mapeamento/14-certidao-190-193.md)
- [Rascunho da refatoração](14-certidao-190-193/notas.md)

*Rascunhos de 27/10/2026, em revisão. Ainda não estão no X-Forms nem no X-Flows de DEV.*

---

## Como usar as skills

1. Exportar o JSON do formulário no X-Forms.
2. Copiar para `docs/andamento/<NN>-<slug>/entrada.json`.
3. No Claude Code: `/melhorar-formulario docs/andamento/<NN>-<slug>/entrada.json`.
4. Revisar `saida.json` + `notas.md` gerados na mesma pasta.

Ver detalhe das 5 skills em `.claude/skills/` do repositório.
