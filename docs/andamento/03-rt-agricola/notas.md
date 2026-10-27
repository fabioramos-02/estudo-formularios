# IAGRO — Cadastro de responsável técnico agrícola

**Origem:** Designer antigo (demo-aws), slug `cadastrar-profissional-habilitado-para-cultivos-e-estabelecimentos-de-insumos-agricolas`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [02. RT agrícola](../mapeamento/02-rt-agricola.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`68468c34357a`). |
| `xforms-v2.json` | Versão 2, importada no X-Forms de DEV (`/app/x-forms/forms/cadastrar-responsavel-tecnico-agricola`). Hash `17c162b34cca`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`6yj6BxStZ295rnGGmkAE9`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Tudo numa página só: dados pessoais, três anexos e o objetivo, nessa ordem. O objetivo do
  cadastro, que define o pedido, vinha por último.
- `[FATO]` "RT" sem explicação, no título da página e na pergunta.
- `[FATO]` E-mail sem validação de formato e sem `inputType: "email"`.
- `[FATO]` Anexos sem tipo nem tamanho aceito.
- `[FATO]` Caixa de seleção com "máximo 2" em uma lista de 2 opções: a regra não fazia nada.
- `[FATO]` `name` sem sentido (`pergunta1`) e anexos sem o prefixo `arquivo_` (C7).
- `[FATO]` Nenhuma mensagem de erro própria; nenhuma orientação sobre o que acontece depois.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Três páginas: seus dados → para que é o cadastro → documentos, com barra de progresso | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta (`autocomplete`) | C2 |
| "RT" e "IAGRO" escritos por extenso na primeira vez; `tooltip` explica o que é responsável técnico | B2, B3 |
| CREA e CFTA por extenso no `tooltip` da carteira do conselho | B2, B3 |
| E-mail com validação e mensagem que diz como corrigir | D2 |
| Anexos: PDF, JPG ou PNG até 5 MB, dito na descrição da página | C8 |
| Objetivo com valores estáveis (`estabelecimento_insumos`, `cultivo_soja_algodao`); tirado o "máximo 2" | C4 |
| Mensagem de erro própria em todo campo obrigatório | D2 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `telefone_celular`, `objetivo_cadastro`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 3 |
| Campos | 8 | 8 |
| Obrigatórios | 8 | 8 (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `RTA-AAAAMMDD-XXXXXX`) → Tables `cadastros_rt_agricola`.
A tabela não guarda CPF nem celular, que ficam só nas respostas do X-Forms (LGPD art. 6º III). Os anexos
entram pelo nome do arquivo.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Nome, e-mail e CPF vindos da conta | `[FATO]` os três preenchidos |
| Celular com `autocomplete: "tel"` | `[FATO]` **não** preenche: o campo veio só com a máscara vazia |
| Celular vazio | bloqueou com "Digite o celular com DDD, 11 números." |
| Anexo | o seletor só aceita `.pdf,.jpg,.jpeg,.png` |
| Envio com os três anexos | "Resposta enviada!" → `SUCCEEDED` → linha `RTA-20261027-UK4EA4`, objetivo "Estabelecimentos de insumos; Cultivos de soja ou algodão" |

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Cadastrar profissional habilitado para cultivos e estabelecimentos insumos agrícolas (ID [2272](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/2272)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/cadastro-de-responsavel-tecnico-para-cultivos-agricolas70> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/cadastrar-responsavel-tecnico-agricola?serviceSlug=cadastro-de-responsavel-tecnico-para-cultivos-agricolas70> |

## Pendências

- ~~O serviço não existe no catálogo de DEV. O teste usou o `serviceSlug` do exemplo do Leonardo.~~ Vinculado em 27/10/2026.
- Confirmar com a IAGRO: o tamanho de 5 MB por anexo serve? Foto do documento (JPG/PNG) é aceita?
- Destino do pedido e conexão Gmail, como no WordPress.
