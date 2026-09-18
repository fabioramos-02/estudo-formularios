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
    └── assets/{img,css}       Tema SEGOV
```

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
