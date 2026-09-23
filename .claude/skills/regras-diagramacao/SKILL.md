---
name: regras-diagramacao
description: Reordena páginas e campos de um JSON X-Forms aplicando regras de diagramação derivadas do GOV.UK Design System (form-structure), gov.br e checklist do estudo SETDIG. Elimina duplicação estrutural (blocos `_2`) via `visibleIf`, aplica proximidade lógica (órgão antes de setor; identificação → vínculo → pedido → anexos → confirmação), respeita limites (≤7 páginas, ~8 campos/página). Dispara em "reorganizar formulário", "reordenar campos", "aplicar diagramação", "one thing per page", ou quando `/melhorar-formulario` chama.
---

# regras-diagramacao

Entrega: JSON X-Forms com páginas/campos reordenados + bloco markdown justificando cada mudança.

## Âncoras

- **GOV.UK Design System — Form structure**: https://www.gov.uk/service-manual/design/form-structure
- **Padrão Digital gov.br**
- `docs/04-checklist.md` seção A (Organização) do repo estudo-formularios

Divergir de uma âncora exige registrar `[HIPÓTESE]` em `notas.md`.

## Regras

### 1. One thing per page (GOV.UK)
Uma pergunta por página quando:
- A resposta muda o fluxo (bifurcação, condicional).
- O campo é decisão principal do serviço.
Caso contrário, agrupar por proximidade (regra 2).

### 2. Proximidade lógica
Campos do mesmo assunto ficam juntos. Ordem canônica **dentro de uma página**:
1. Chave (ex.: `orgao` antes de `setor` — setor depende do órgão)
2. Identificação da pessoa (`nome_completo`, `cpf`, `email`, `telefone`)
3. Vínculo institucional (`matricula`, `cargo`, `orgao`, `setor`)
4. Localização (`municipio`, `uf`, endereço agrupado)

**Anti-pattern:** `orgao` primeiro, `setor` último. Sempre encostados.

### 3. Ordem canônica das páginas
1. **Escolha** (o que quer fazer) — se houver bifurcação
2. **Identificação** (quem é)
3. **Vínculo institucional** (onde trabalha, se aplicável)
4. **Detalhe do pedido** (o que quer especificamente)
5. **Anexos**
6. **Confirmação** (revisar antes de enviar)

### 4. Limites
- **Páginas:** máximo 7 (heurística NNG/Baymard, `[HIPÓTESE]` a validar).
- **Campos por página:** ~8 sem cansar; até 10 se todos do mesmo assunto (endereço).
- **Total do formulário:** se >40 campos após otimização, marcar `[RECOMENDAÇÃO]` no `notas.md` para revisar necessidade (checklist C1).

### 5. Eliminar duplicação estrutural
**Anti-pattern comum:** bloco duplicado (`_gestor` + `_gestor2`, `_colaborador` + `_colaborador2`) só para inverter ordem de páginas conforme escolha inicial.

**Correção:** um bloco de cada perfil. Reordenação vira `visibleIf` na página + controle do fluxo condicional no X-Forms (se suportado) ou aviso `[FATO]` de limitação em `notas.md`.

### 6. Substituir reordenação dinâmica por `visibleIf`
Se o X-Forms não suporta reordenar páginas por escolha, usar `visibleIf` para mostrar/esconder páginas — cidadão vê ordem lógica sem ver blocos vazios.

### 7. Dependências (fluxo cognitivo)
Campo B depende do campo A → A vem primeiro **e** `B.visibleIf = "{A} notempty"` para não confundir.

Exemplo:
```json
{"type":"text","name":"setor","visibleIf":"{orgao} notempty"}
```

## Entrada e saída

Entrada: caminho do JSON X-Forms.
Saída:
- JSON reordenado.
- Bloco markdown:

```md
## Diagramação

### Estrutura antes
- 7 páginas, 51 campos.
- Duplicação: `_gestor` + `_gestor2`, `_colaborador` + `_colaborador2` (ordem invertida por escolha inicial).

### Estrutura depois
- 5 páginas, 28 campos.
- [FATO] blocos duplicados unificados. Ordem controlada por `visibleIf`.
- [RECOMENDAÇÃO GOV.UK] "Escolher perfil" isolada como página 1 (one thing per page).
- [RECOMENDAÇÃO checklist A3] `orgao` antes de `setor`.

### Mudanças página a página
| Antes | Depois | Motivo |
|---|---|---|
| `pagina_gestor1` + `pagina_gestor_2` | `dados_gestor` (um bloco) | duplicação estrutural |
| `secretaria_orgao_gestor` posição 7 | posição 3 | proximidade com `setor_gestor` |
```

## Uso

Chamado direto ou por `melhorar-formulario`. Roda **depois** de `nomenclatura-campos` (assume `name` já normalizado).

## Fora de escopo

- Não reescreve `title` (é `linguagem-simples-rotulos`).
- Não altera tipo/validação/máscara.

## Como o Antonio edita esta skill

Quando a pesquisa validar (ou contradizer) um limite:
1. Ajustar o número em "Limites" (ex.: se estudo mostrar que 6 campos por página cansa menos, trocar 8 → 6).
2. Refletir a mudança em `docs/04-checklist.md` seção A.
3. Se descobrir nova regra de proximidade (ex.: `data_inicio` sempre antes de `data_fim`), acrescentar em "Ordem canônica dentro de uma página".
