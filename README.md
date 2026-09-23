# Estudo de Formulários — X-Forms

Estudo da **SETDIG — Secretaria-Executiva de Transformação Digital**, pela Superintendência de
Governo Digital (SGD), sobre como formulários de serviços digitais devem ser diagramados, escritos
e nomeados.

Motivo: os formulários que hoje rodam no **FormFlow** serão reconstruídos no **X-Forms**, a
ferramenta de formulário dinâmico da Xvia. O padrão precisa estar definido antes da reconstrução.

**Fio condutor:** toda recomendação responde a uma única pergunta — *isso deixa o formulário mais
fácil de preencher?*

## Como rodar

```bash
pip install -r requirements.txt
python -m mkdocs serve -a 127.0.0.1:8000
```

Antes de entregar qualquer coisa:

```bash
python -m mkdocs build --strict
```

## Quem faz o quê

| Pessoa | Papel |
|---|---|
| **Antonio** (estagiário) | Pesquisa (`docs/01`, `02`, `03`) e auditoria dos 14 formulários (`docs/fichas/`) |
| **Fabio Ramos** | Consolida os achados, fecha o padrão e apresenta à SGD |

Antonio começa por `docs/guia-do-antonio.md`.

## Estrutura

```
.claude/skills/           5 skills que rodam dentro do Claude Code (ver seção abaixo)
docs/
├── index.md              O estudo em uma tela
├── guia-do-antonio.md    Passo a passo do trabalho
├── 01-diagramacao.md     Como organizar os campos     [Antonio]
├── 02-aprendizados.md    O que funciona e o que atrapalha  [Antonio]
├── 03-nomenclatura.md    Rótulo x nome técnico + dicionário  [Antonio]
├── 04-checklist.md       A régua da auditoria
├── 05-auditoria.md       Os 14 formulários + achados
├── fontes.md             Bibliografia
├── fichas/               Uma ficha por formulário     [Antonio]
└── andamento/            Uma pasta por formulário refatorado
    └── 01-wordpress/     entrada.json | saida.json | notas.md
```

As páginas 01, 02 e 03 nascem como esqueleto, com as perguntas dentro. Quem preenche responde e
apaga a pergunta.

## Skills (automação do estudo)

O repo traz 5 skills em `.claude/skills/` que rodam dentro do Claude Code. Elas aplicam o padrão
do estudo sobre um JSON de formulário X-Forms exportado, sem sair do repositório.

| Skill | Função |
|---|---|
| `nomenclatura-campos` | Normaliza `name` dos campos contra dicionário canônico (`docs/03-nomenclatura.md`) |
| `regras-diagramacao` | Reordena páginas e campos (GOV.UK Design System + gov.br) |
| `linguagem-simples-rotulos` | Reescreve rótulos, ajuda e mensagens de erro (Lei 15.263/2025) |
| `auditoria-metricas` | Conta páginas, campos, condicionais — antes e depois |
| `melhorar-formulario` | Orquestrador: chama as 4 acima em cadeia |

Como usar:

1. Exportar o JSON do formulário no X-Forms.
2. Copiar para `docs/andamento/<NN>-<slug>/entrada.json`.
3. No Claude Code: `/melhorar-formulario docs/andamento/<NN>-<slug>/entrada.json`.
4. Revisar `saida.json` + `notas.md` gerados na mesma pasta.

Piloto pronto: `docs/andamento/01-wordpress/`.

Cada `SKILL.md` tem uma seção **"Como o Antonio edita esta skill"** — quando a pesquisa validar
um novo termo canônico ou uma regra nova, edita o SKILL.md, o `docs/03` ou `docs/04` e faz um
commit.

## Fases

| Fase | Quem | Entrega |
|---|---|---|
| 0 | Fabio | Repo montado ✅ |
| 1 | Antonio | Páginas 01, 02, 03 + fontes + dicionário de campos |
| 2 | Antonio | 14 fichas + prints + tabela de `05` atualizada |
| 3 | Dupla | Achados consolidados + checklist revisado |
| 4 | Fabio | Site publicado + conversa com a SGD |

## Pendências

- [ ] Confirmar URL de cada um dos 14 serviços no Portal e preencher a coluna **Órgão** em `docs/05-auditoria.md`.
- [ ] Confirmar se o Antonio tem acesso/login para abrir todos os 14 formulários.
- [ ] **Segundo ponto a levar à SGD** — pauta ainda não definida, preencher antes da conversa.

## Contexto que vive fora deste repo

| Onde | O que tem |
|---|---|
| `../xvia-1/modulos/formflow/` | Regras de negócio, manual e requisitos do FormFlow atual |
| `../avaliacao-de-servicos/` | Repo de referência: mesmo padrão MkDocs + tema SEGOV |
