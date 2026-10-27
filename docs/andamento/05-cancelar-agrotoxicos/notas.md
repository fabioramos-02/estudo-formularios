# IAGRO — Cancelar registro de empresa de agrotóxicos

**Origem:** Designer antigo (demo-aws), slug `cancelar-o-registro-de-estabelecimento-comercial-e-prestador-de-servico-de-agrotoxico`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [05. Cancelar agrotóxicos](../mapeamento/05-cancelar-agrotoxicos.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`4b821a12ad70`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, importada no X-Forms de DEV (`/app/x-forms/forms/cancelar-registro-empresa-agrotoxicos`). Hash `a4e8d54b07c4`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`yZq69hlAb9H9bkEJ1YT5M`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 14 campos ficavam numa página só, com o título "TERMO DE COMPROMISSO" em maiúsculas.
- `[FATO]` Pedia RG, órgão expedidor e UF do órgão junto com o CPF (C1).
- `[FATO]` "Município" tinha a descrição "Selecione os motivos", copiada de outro campo.
- `[FATO]` O motivo era lista suspensa com 4 frases longas, uma delas com erro de digitação
  ("agrotóxicosm"). A descrição dizia "os motivos", mas só aceitava um.
- `[FATO]` CNPJ sem máscara e sem validação.
- `[FATO]` Não havia e-mail para a resposta (B6).
- `[FATO]` Anexos sem tipo nem tamanho aceito.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Quatro páginas: responsável → empresa → motivo → documentos | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta | C2, B6 |
| RG, órgão expedidor e UF do órgão removidos: o CPF identifica a pessoa | C1 |
| Motivo em botões de opção, com valores curtos (`nao_comercializa`, `lei_2951`…) e erro de digitação corrigido | C4, B1 |
| CNPJ com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| Estado com valor em sigla e nome por extenso | C4 |
| Anexos em PDF até 5 MB, dito na descrição da página | C8 |
| "IAGRO" explicada na descrição do formulário | B2 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `razao_social`, `logradouro`, `motivo_cancelamento`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 4 |
| Campos | 14 | 12 (saíram RG, órgão e UF do órgão; entrou e-mail) |
| Obrigatórios | 14 | 12 (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `CAG-AAAAMMDD-XXXXXX`) → Tables `cancelamentos_registro_agrotoxicos`.
A tabela não guarda CPF nem endereço completo, só município e UF (LGPD art. 6º III). O motivo é gravado
em texto curto.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Nome, CPF e e-mail vindos da conta | `[FATO]` os três preenchidos |
| Estado sem escolher (Enter na busca não seleciona) | bloqueou com "Escolha o estado para continuar." |
| Envio | "Resposta enviada!" → `SUCCEEDED` → linha `CAG-20261027-0CFFPK`, motivo "Não vai continuar vendendo (Lei Estadual 2.951/2004)" |

## Pendências

- Confirmar com a IAGRO: pode tirar o RG? Na v2 ele saiu.
- Confirmar com a IAGRO: que guia de recolhimento é essa, onde se emite e qual o valor. Hoje o
  formulário só diz "A guia paga".
- `[RECOMENDAÇÃO]` O comprovante de inscrição no CNPJ é público na Receita Federal (Lei 14.129/2021).
  Mesmo caso do formulário 04.
- O serviço não existe no catálogo de DEV. O teste usou o `serviceSlug` do exemplo do Leonardo.
- Destino do pedido e conexão Gmail, como nos anteriores.
