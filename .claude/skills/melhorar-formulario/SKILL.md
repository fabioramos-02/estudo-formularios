---
name: melhorar-formulario
description: Orquestra a refatoração de um JSON X-Forms existente aplicando, em cadeia, as skills atômicas do estudo SETDIG — auditoria-metricas (antes) → nomenclatura-campos → regras-diagramacao → linguagem-simples-rotulos → auditoria-metricas (depois). Gera `saida.json` + `notas.md` consolidado. Dispara em "/melhorar-formulario", "refatorar formulário", "aplicar boas práticas neste form", "auditar formulário X", ou ao apontar um JSON X-Forms de um dos 14 formulários do estudo.
---

# melhorar-formulario — orquestrador

Entrega: numa pasta `docs/andamento/<slug>/`:
- `entrada.json` (cópia do original)
- `saida.json` (refatorado)
- `notas.md` (consolidado com marcadores `[FATO]`/`[RECOMENDAÇÃO]`/`[HIPÓTESE]`)

## Trigger

- `/melhorar-formulario <caminho-do-json>`
- "Refatore este formulário: `<caminho>`"
- Auto: usuário aponta JSON X-Forms e menciona "melhorar", "aplicar estudo", "boas práticas".

## Fluxo

1. **Preparar pasta:**
   - Slug do serviço a partir do `title` do JSON (kebab-case sem acento).
   - Se pasta não existe: `docs/andamento/<NN>-<slug>/` com `NN` sequencial.
   - Copiar JSON original para `entrada.json`.

2. **Snapshot inicial:** invocar `auditoria-metricas` sobre `entrada.json` → bloco markdown "Métricas — snapshot inicial".

3. **Nomenclatura:** invocar `nomenclatura-campos` → produz JSON com `name` normalizado + bloco "Nomenclatura".

4. **Diagramação:** invocar `regras-diagramacao` sobre o JSON da etapa 3 → produz JSON reordenado + bloco "Diagramação". **Aqui** eliminar duplicações estruturais (`_2`), aplicar `visibleIf`, ajustar ordem canônica.

5. **Linguagem simples:** invocar `linguagem-simples-rotulos` sobre o JSON da etapa 4 → JSON com textos reescritos + bloco "Linguagem simples". Chama subagent `linguagem-simples-revisor` para pontuação.

6. **Snapshot final:** invocar `auditoria-metricas` sobre o JSON da etapa 5 → bloco "Métricas — snapshot final". Diff antes/depois.

7. **Salvar:**
   - `saida.json` = resultado da etapa 5.
   - `notas.md` = concatenação dos blocos + seção "Limitações do X-Forms" para regras que não puderam ser aplicadas (ex.: validação cruzada e-mail×órgão).

## Estrutura de `notas.md`

```md
# <título do serviço>

**Origem:** `<caminho-do-json-original>`
**Data:** <data>
**Skills aplicadas:** auditoria-metricas → nomenclatura-campos → regras-diagramacao → linguagem-simples-rotulos → auditoria-metricas

---

## Métricas — snapshot inicial
<bloco>

## Nomenclatura
<bloco>

## Diagramação
<bloco>

## Linguagem simples
<bloco>

## Métricas — snapshot final
<bloco>

## Limitações do X-Forms observadas
- <lista de coisas que a plataforma não permite hoje e viraram [FATO] ou [HIPÓTESE]>

## Próximos passos
- Importar `saida.json` no X-Forms e conferir render.
- Gerar fluxo via `activepieces-fluxo`.
```

## Contrato com skills

- Cada skill atômica **lê** um JSON e **escreve** um JSON (arquivo intermediário em `tmp/` ou stdout).
- Cada skill **emite** um bloco markdown para consolidação.
- Orquestrador é o único que grava em `docs/andamento/`.

## Performance

- Ler o JSON uma vez por skill (não re-parse desnecessário).
- Blocos markdown são strings — concatenar em memória e escrever `notas.md` no fim.

## Depois

Sugerir ao usuário:
1. Importar `saida.json` no X-Forms (validação visual).
2. Rodar `activepieces-fluxo` sobre `saida.json` para gerar o fluxo.
3. Atualizar `docs/03-nomenclatura.md` (dicionário canônico) e `docs/05-auditoria.md` (status → feito).

## Fora de escopo

- Não gera fluxo Activepieces (é `activepieces-fluxo`).
- Não substitui `xforms-formulario` (geração from-scratch).
- Não aplica regras de negócio específicas do órgão — só padrão do estudo.

## Como o Antonio edita esta skill

Esta skill é **cola** — só encadeia as outras. Editar aqui quando:
1. Aparecer um passo novo no fluxo (ex.: `validar-acessibilidade` no futuro) — acrescentar no "Fluxo".
2. Mudar formato de saída do `notas.md` — atualizar "Estrutura de `notas.md`".
3. Se um formulário exigir passo extra (ex.: pré-processar um FormFlow legado), documentar aqui como exceção, não como regra.
