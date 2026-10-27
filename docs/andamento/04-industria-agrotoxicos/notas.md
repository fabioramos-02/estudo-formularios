# IAGRO — Cadastrar indústria de agrotóxicos no e-Saniagro

**Origem:** Designer antigo (demo-aws), slug `cadastrar-industria-produtos-agrotoxicos-no-e-saniagro`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [04. Indústria agrotóxicos](../mapeamento/04-industria-agrotoxicos.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`543520244c7c`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, importada no X-Forms de DEV (`/app/x-forms/forms/cadastrar-industria-agrotoxicos-e-saniagro`). Hash `08f1ca3abdeb`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`IVFwOtnIldDz2I2pNoZYI`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 13 campos ficavam numa página só, todos obrigatórios.
- `[FATO]` A procuração era obrigatória para todos, mas a descrição dizia que só vale quando a
  indústria é representada por consultoria ou empresa de registros.
- `[FATO]` "Representante legal" dizia "se for o caso", mas era obrigatório.
- `[FATO]` CNPJ sem máscara e sem validação.
- `[FATO]` Não havia e-mail: a IAGRO não tinha por onde responder (B6).
- `[FATO]` Estado em minúsculas ("mato grosso do sul") e com `choicesMin`/`choicesMax`, que não fazem
  nada em lista suspensa.
- `[FATO]` Dois campos com o mesmo título "CNPJ": um de texto, outro de anexo.
- `[FATO]` "e-saniagro" sem explicação; anexos sem tipo nem tamanho aceito.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Pergunta nova "Você é": própria indústria ou consultoria. A procuração só aparece e só é obrigatória para consultoria (`visibleIf` + `requiredIf`) | C1, C9 |
| Quatro páginas: quem pede → indústria → endereço → documentos | A2, A3, A4 |
| Nome e e-mail de quem preenche, pré-preenchidos com a conta; e-mail com validação | C2, B6, D2 |
| `[INTERPRETAÇÃO]` "Contato" da v1 virou quem preenche: a IAGRO fala com essa pessoa | C1, C2 |
| CNPJ com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| Estado com valor em sigla (`MS`) e nome por extenso; busca na lista | C4 |
| Endereço com "Rua, número e complemento" na descrição | B3 |
| "e-Saniagro" e "IAGRO" explicados na descrição do formulário | B2 |
| Anexo de CNPJ renomeado para "Comprovante de inscrição no CNPJ" | B1 |
| Anexos em PDF até 5 MB, dito na descrição da página | C8 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `perfil_solicitante`, `nome_completo`, `nome_representante_legal`, `logradouro`, `municipio`, `uf`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 4 |
| Campos | 13 | 16 (entrou "Você é", e-mail e o nome de quem preenche no lugar de "contato") |
| Obrigatórios, indústria | 13 | 15 (2 já vêm da conta) |
| Obrigatórios, consultoria | 13 | 16 (2 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `AGI-AAAAMMDD-XXXXXX`) → Tables `cadastros_industria_agrotoxicos`.
A tabela não guarda celular nem endereço completo, só município e UF (LGPD art. 6º III). Os anexos
entram pelo nome do arquivo.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Nome e e-mail vindos da conta | `[FATO]` preenchidos |
| CNPJ incompleto | bloqueou com "Digite o CNPJ com 14 números." |
| Estado | a busca na lista funciona ("Mato Grosso do" → Mato Grosso do Sul) |
| Consultoria → procuração | apareceu; sem ela, bloqueou com "Anexe a procuração para continuar." |
| Envio, caminho consultoria | "Resposta enviada!" → `SUCCEEDED` → linha `AGI-20261027-GMMSE2`, UF `MS`, CNPJ sem máscara |
| Envio, caminho própria indústria | outro envio da mesma conta, feito à mão em paralelo → `SUCCEEDED` → linha `AGI-20261027-OV3YG1`, sem procuração |

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Cadastrar indústria de produtos agrotóxicos no e-saniagro (ID [2310](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/2310)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/cadastrar-industria-produtos-agrotoxicos-no-e-saniagro176> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/cadastrar-industria-agrotoxicos-e-saniagro?serviceSlug=cadastrar-industria-produtos-agrotoxicos-no-e-saniagro176> |

## Pendências

- `[RECOMENDAÇÃO]` O comprovante de inscrição no CNPJ é público na Receita Federal. Pela Lei
  14.129/2021, a IAGRO não deveria pedir o anexo. Confirmar com a IAGRO se pode sair.
- Confirmar com a IAGRO: "Contato" da v1 era quem preenche ou outra pessoa da indústria?
- ~~O serviço não existe no catálogo de DEV. O teste usou o `serviceSlug` do exemplo do Leonardo.~~ Vinculado em 27/10/2026.
- Destino do pedido e conexão Gmail, como nos anteriores.
