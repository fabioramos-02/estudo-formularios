# CLAUDE.md — Estudo de Formulários (X-Forms)

Contexto para futuras sessões do Claude Code neste repositório.

## O que é

Estudo da **SETDIG — Secretaria-Executiva de Transformação Digital**, pela Superintendência de
Governo Digital (SGD), sobre diagramação, boas práticas e nomenclatura de campos em formulários de
serviços digitais do Estado de MS.

Pauta pedida pela SGD: (1) diagramação de formulários, (2) aprendizados sobre formulários,
(3) padrão de nomenclatura dos campos.

## Regra número 1 — a experiência de preenchimento decide

Toda recomendação responde a: **isso deixa o formulário mais fácil de preencher?** Recomendação que
serve só ao processamento interno, à estética ou à preferência técnica não entra.

## Regra número 2 — as âncoras de referência

1. **GOV.UK Design System** — padrões de formulário, *one thing per page*.
2. **Design System gov.br / Padrão Digital de Governo** — referência federal.

Secundárias: Nielsen Norman Group, Baymard Institute.
Divergir de uma âncora exige justificativa explícita no texto.

## FormFlow x X-Forms — não confundir

- **FormFlow**: módulo atual da Plataforma de Governo Digital. Cria fluxos e formulários, coleta os
  dados do cidadão no Portal Único e os encaminha ao Integrador em JSON. Regras em
  `../xvia-1/modulos/formflow/Modulo FormFlow - v1.md`.
- **X-Forms**: ferramenta de formulário dinâmico da Xvia que vai substituí-lo.

Este repo define **o padrão**, não especifica implementação.

## Recursos do X-Forms (exemplo de out/2026)

Formato: JSON SurveyJS. Exemplo completo em `.claude/referencia/xforms-precadastro-familiar.json`
e o fluxo Activepieces que o recebe em `.claude/referencia/activepieces-precadastro-familiar.json`.

| Recurso | JSON | Uso no padrão |
|---|---|---|
| Dica no ícone | `tooltip` | Informação **complementar** (por que pedimos, exemplo). O que é preciso para preencher vai em `description`, visível (B3, D1). |
| Pré-preenchimento da conta | `autocomplete`: `name`, `cpf`, `email`, `celular`, `cidade` | Resolve C2 (dado que o governo já tem). `[HIPÓTESE]` a confirmar: lista completa de chaves e se `celular`/`cidade` vêm do cadastro. |
| Obrigatório condicional | `requiredIf` junto com `visibleIf` | Campo que só aparece em um caso só é obrigatório nesse caso (C9). |
| Validação | `validators`: `regex`, `email`, `numeric` (`minValue`/`maxValue`), `expression` | `text` é a mensagem de erro: diz como corrigir (D2). `expression` dá erro quando é falsa. |
| Máscara | `maskType: "pattern"` + `maskSettings.pattern` | C5. Valor chega sem máscara. |
| Lista de pessoas | `matrixdynamic` (`columns`, `rowCount`, `maxRowCount`, `addRowText`, `totalType`) | Substitui blocos copiados (`_2`, `_3`) para N pessoas. Chega como lista: `answers.membros[i].nome`. |
| Cálculo na tela | `expression` (com `displayStyle: "currency"`), `calculatedValues`, `countInArray`, `sumInArray` | Mostra o resultado enquanto a pessoa preenche. O fluxo recalcula: o valor do formulário não é a fonte oficial. |
| Aviso condicional | `html` + `visibleIf` | Avisa sem bloquear o envio. |
| Sim/Não | `boolean` + `labelTrue`/`labelFalse` | Pergunta de duas respostas. |
| Texto longo | `comment` + `maxLength` | A6. |
| Tela final | `completedHtml` | B6: o que acontece depois do envio. |
| Numeração | `showQuestionNumbers: "off"` | Sem número nas perguntas. |

`[HIPÓTESE]` Comparar dois campos (`{a} > {b}`) funciona em `visibleIf` e `validators.expression`.
Isso pode tirar "comparação entre dois campos" da lista de limites em `docs/pendencias.md`. Testar
na plataforma antes.

Webhook (Activepieces): `{ answers, formName, serviceSlug, submittedAt, userId }`. `userId` é o `sub`
da conta do portal.

## Como escrever

- Marcadores obrigatórios: `[FATO]`, `[INTERPRETAÇÃO]`, `[HIPÓTESE]`, `[RECOMENDAÇÃO]`,
  `**Não identificado**`.
- Todo `[FATO]` tem fonte em `docs/fontes.md` com link e data de acesso.
- Nunca copiar mais que 25 palavras seguidas de uma fonte.
- pt-BR, frase curta, linguagem simples (Lei 15.263/2025). Termo técnico se explica na primeira
  aparição.
- Vocabulário: "estudo", "padrão", "recomendação". Não usar "PBI", "sprint", "epic", "backlog".
- Nome oficial sempre: **Secretaria-Executiva de Transformação Digital — SETDIG**. Nunca
  "Secretaria de Estado de Governo Digital".

## Quem escreve o quê

| Arquivo | Autor |
|---|---|
| `docs/01-diagramacao.md`, `02-aprendizados.md`, `03-nomenclatura.md` | Antonio (estagiário) |
| `docs/fichas/*.md` | Antonio |
| `docs/04-checklist.md`, `05-auditoria.md` (achados), `index.md` | Fabio |

Ao editar uma página do Antonio, preservar o que ele escreveu — complementar, não sobrescrever.

## Estrutura

```
estudo-formularios/
├── README.md, CLAUDE.md, mkdocs.yml, requirements.txt
├── .github/workflows/gh-pages.yml
├── .claude/referencia/       JSON de exemplo do X-Forms atual + fluxo Activepieces
├── .claude/skills/           5 skills project-local (autoload no Claude Code)
│   ├── nomenclatura-campos/
│   ├── regras-diagramacao/
│   ├── linguagem-simples-rotulos/
│   ├── auditoria-metricas/
│   └── melhorar-formulario/  Orquestrador — /melhorar-formulario <json>
└── docs/
    ├── index.md               O estudo em uma tela
    ├── guia-do-antonio.md     Passo a passo do estagiário
    ├── 01-diagramacao.md      Esqueleto com perguntas a responder
    ├── 02-aprendizados.md     Esqueleto com perguntas a responder
    ├── 03-nomenclatura.md     Esqueleto + dicionário de campos canônicos
    ├── 04-checklist.md        A régua (A organização, B linguagem, C campos, D erro/acessibilidade)
    ├── 05-auditoria.md        Tabela dos 14 formulários + achados consolidados
    ├── fontes.md              Bibliografia
    ├── fichas/_template.md    Ficha que se copia por formulário
    ├── andamento/             Uma pasta por formulário refatorado
    │   ├── recomendacoes.md   Padrões observados (Antonio)
    │   └── 01-wordpress/      entrada.json | saida.json | notas.md
    └── assets/{img,css}       Tema SEGOV
```

## Skills do estudo (`.claude/skills/`)

O Claude Code carrega estas 5 skills automaticamente quando o repo é aberto:

- `nomenclatura-campos` — normaliza `name` contra dicionário canônico
- `regras-diagramacao` — reordena páginas/campos (GOV.UK + gov.br)
- `linguagem-simples-rotulos` — reescreve rótulos (Lei 15.263/2025)
- `auditoria-metricas` — snapshot read-only (antes e depois)
- `melhorar-formulario` — orquestrador: `/melhorar-formulario <caminho-json>`

Fluxo padrão: exportar JSON do X-Forms → `docs/andamento/<NN>-<slug>/entrada.json` →
rodar `/melhorar-formulario` → revisar `saida.json` + `notas.md`.

Cada `SKILL.md` tem seção **"Como o Antonio edita esta skill"**. Quando a pesquisa validar um
termo canônico novo, uma regra nova ou um limite (páginas, campos), editar o SKILL.md, refletir
em `docs/03-nomenclatura.md` ou `docs/04-checklist.md` e commit. As skills viajam versionadas
junto com o estudo — não estão no `~/.claude/skills/` global.

Skills globais relacionadas (geram formulário e fluxo do zero, não seguem o estudo):
`xforms-formulario`, `activepieces-fluxo`, `demanda`. Fonte da verdade: vault Obsidian em
`conhecimento-obsidian/30-ia/skills/portal-servicos/`. Editou em `~/.claude/skills/`? Copiar de volta
para o vault.

## Base legal aplicável

- Lei 14.129/2021 — Governo Digital (vedação de exigir dado que a administração já possui).
- Lei 13.709/2018 — LGPD (minimização, art. 6º III).
- Lei 13.460/2017 — usuário de serviço público.
- Lei 15.263/2025 + Decreto Estadual 16.744/2026 — linguagem simples.
- WCAG 2.2 — critérios 3.3.x (rótulo, identificação e sugestão de erro, entrada redundante).

## Design system

Paleta SEGOV: primário `#004F9F`, dark `#003A76`, light `#1A67B5`, texto `#30302E`.
Tema light + dark em `docs/assets/css/segov.css` (copiado de `../avaliacao-de-servicos`).

## Comandos

```bash
pip install -r requirements.txt
python -m mkdocs serve -a 127.0.0.1:8000
python -m mkdocs build --strict
```

`build --strict` é obrigatório antes de publicar — falha em link quebrado ou página fora da nav.
