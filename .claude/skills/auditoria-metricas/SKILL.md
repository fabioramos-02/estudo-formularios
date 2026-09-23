---
name: auditoria-metricas
description: Snapshot read-only de um JSON X-Forms — conta páginas, campos totais, campos por página, tipos usados, condicionais (`visibleIf`), e sinaliza campos herdáveis do gov.br (CPF, nome, e-mail — Lei 14.129/2021 + LGPD art. 6º III). Output = tabela markdown pronta para `notas.md`. Dispara em "métricas do formulário", "auditoria de formulário", "quantos campos tem", "análise quantitativa", ou quando `/melhorar-formulario` chama (antes e depois da refatoração).
---

# auditoria-metricas

Entrega: bloco markdown com métricas do formulário. Não altera JSON.

## O que mede

1. **Estrutura:** nº páginas, nº campos totais, campos por página, tipos únicos.
2. **Condicionais:** quantos `visibleIf` (bom sinal de fluxo cognitivo).
3. **Obrigatoriedade:** obrigatórios vs opcionais.
4. **Uploads:** contagem de campos `file`.
5. **Herdáveis do gov.br:** flag para `cpf`, `nome_completo`, `email` (e variações com sufixo). Aponta que podem vir do login (Lei 14.129/2021 art. 5º I; LGPD art. 6º III — minimização).
6. **Alertas de limite:**
   - Página com >8 campos → `[RECOMENDAÇÃO]` de dividir.
   - >7 páginas → `[RECOMENDAÇÃO]` de consolidar.
   - >40 campos totais → `[RECOMENDAÇÃO]` de rever necessidade.
   - Blocos duplicados por sufixo (`_2`, `_alternativo`) → `[FATO]` de duplicação estrutural.

## Script de referência

```python
import json, sys, collections
d = json.load(open(sys.argv[1], encoding='utf-8'))
pages = d['pages']
elems = [e for p in pages for e in p['elements']]
tipos = collections.Counter(e['type'] for e in elems)
obrig = sum(1 for e in elems if e.get('isRequired'))
cond = sum(1 for e in elems if e.get('visibleIf'))
herdaveis = [e['name'] for e in elems if e['name'].split('_')[0] in ('cpf','nome','email','telefone','rg')]
dup = [e['name'] for e in elems if e['name'].endswith('2') or e['name'].endswith('_alternativo')]
print(f"páginas={len(pages)} campos={len(elems)} obrig={obrig} cond={cond}")
print("tipos:", dict(tipos))
print("herdáveis:", herdaveis)
print("duplicados:", dup)
for p in pages:
    n = len(p['elements'])
    tag = " ⚠ >8" if n > 8 else ""
    print(f"  {p.get('name')}: {n} campos{tag}")
```

## Saída (formato)

```md
## Métricas — snapshot inicial

| Métrica | Valor |
|---|---|
| Páginas | 7 |
| Campos | 51 |
| Obrigatórios | 50 |
| Condicionais (`visibleIf`) | 3 |
| Tipos | text (39), dropdown (10), checkbox (1), imagepicker (1) |
| Uploads | 0 |

### Campos por página
| Página | Campos | Alerta |
|---|---|---|
| pagina_seleciona_usuario | 1 | ok |
| pagina_permissao | 3 | ok |
| pagina_gestor1 | 9 | ⚠ >8 |
| pagina_colaborador_1 | 10 | ⚠ >8 |
| ... | ... | ... |

### Achados
- [FATO] Duplicação estrutural: `nome_gestor` + `nome_gestor2`, `nome_colaborador` + `nome_colaborador2`.
- [RECOMENDAÇÃO] Total 51 campos > 40. Rever necessidade de cada campo.
- [RECOMENDAÇÃO] Campos herdáveis do gov.br: `cpf_gestor`, `nome_gestor`, `email_gestor` — considerar pré-preencher do login (Lei 14.129/2021, LGPD art. 6º III).
```

## Uso

Chamado direto (audita form) ou pelo `melhorar-formulario` (snapshot antes/depois).

## Fora de escopo

- Não muda o JSON.
- Não avalia texto (`title`) — é `linguagem-simples-rotulos`.

## Como o Antonio edita esta skill

- Se a pesquisa revalidar os limites (7 páginas, 8 campos/página, 40 totais), ajustar os alertas aqui.
- Se aparecer um padrão novo de duplicação (`_alternativo`, `_bkp`), acrescentar em "Alertas de limite".
- A lista de "herdáveis do gov.br" cresce conforme o gov.br oferecer mais campos no login — atualizar com base em `docs/fontes.md`.
