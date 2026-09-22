---
name: nomenclatura-campos
description: Normaliza o atributo `name` dos campos de um JSON X-Forms (SurveyJS) contra dicionário canônico do estudo SETDIG. Aplica snake_case sem acento, prefixo `arquivo_` para upload e sufixo semântico (ex.: `_gestor`, `_colaborador`) para blocos repetidos. Cruza com `docs/03-nomenclatura.md` do repo estudo-formularios. Dispara em "normalizar nomes", "aplicar dicionário", "nomenclatura dos campos", "renomear campos do formulário", ou quando `/melhorar-formulario` chama.
---

# nomenclatura-campos

Entrega: JSON X-Forms com `name` normalizado + diff markdown das renomeações.

## Regras

1. **Formato:** `snake_case` minúsculo, sem acento, sem espaço, sem `CamelCase`.
2. **Dicionário canônico** (fonte: `docs/03-nomenclatura.md` §3.5). Termos comuns:

| Rótulo do formulário | `name` canônico |
|---|---|
| CPF | `cpf` |
| CNPJ | `cnpj` |
| Nome / Nome completo | `nome_completo` |
| E-mail | `email` |
| Telefone / Celular | `telefone` |
| Data de nascimento | `data_nascimento` |
| RG | `rg` (marcar `[RECOMENDAÇÃO]` de remoção — nova identidade usa CPF) |
| Órgão expedidor | `orgao_expedidor` |
| CEP | `cep` |
| Endereço / Logradouro | `logradouro` |
| Número | `numero` |
| Complemento | `complemento` |
| Bairro | `bairro` |
| Município / Cidade | `municipio` |
| UF / Estado | `uf` |
| Secretaria / Órgão | `orgao` |
| Setor / Unidade Gestora | `setor` |
| Cargo | `cargo` |
| Matrícula | `matricula` |
| Login de rede | `login_rede` |

3. **Blocos repetidos** (mesmo dado para pessoas diferentes no mesmo form): sufixo `_gestor`, `_colaborador`, `_responsavel`. Nunca `_2` — se aparece número, é sinal de duplicação estrutural que o passo `regras-diagramacao` resolve.
4. **Upload:** prefixo `arquivo_` (`arquivo_procuracao`, `arquivo_comprovante`).
5. **Contrato Activepieces:** o fluxo lê `step_1['answers'][name]`. Rename só antes de gerar o fluxo. Se fluxo já existe, avisar antes de renomear.

## Entrada e saída

Entrada: caminho do JSON X-Forms.
Saída:
- `<mesmo-arquivo>` com `name` reescrito (in-place se orquestrador manda, senão `<arquivo>.nom.json`).
- Bloco markdown pronto para colar em `notas.md`:

```md
## Nomenclatura

| Antes | Depois | Motivo |
|---|---|---|
| `cpf_gestor` | `cpf_gestor` | ok, já canônico |
| `secretaria_orgao_gestor` | `orgao_gestor` | dicionário: `orgao` |
| `nome_colaborador2` | `nome_colaborador` | duplicação estrutural — passo diagramação resolve |
```

## Uso

Chamada direta: leia o JSON, aplique regras, escreva JSON de saída, imprima o bloco markdown.

Chamada pelo orquestrador `melhorar-formulario`: recebe `caminho_json` e diretório de saída, devolve o bloco markdown para consolidar em `notas.md`.

## Fora de escopo

- Não altera `title`, `placeholder`, ordem de campos ou estrutura de páginas.
- Não valida se máscara/type está correto (isso é `xforms-formulario` na geração).

## Como o Antonio edita esta skill

Quando um formulário novo trouxer um termo comum que **não** está no dicionário:
1. Escolher o `name` canônico (`snake_case`, sem acento, sem prefixo desnecessário).
2. Acrescentar linha na tabela de dicionário acima **e** em `docs/03-nomenclatura.md` §3.5.
3. Rodar `/melhorar-formulario` num piloto para confirmar que o termo pega.
