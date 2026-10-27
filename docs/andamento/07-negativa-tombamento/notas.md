# FCMS — Pedir certidão negativa de tombamento

**Origem:** Designer antigo (demo-aws), slug `solicitacao-da-negativa-de-tombamento`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [07. Negativa de tombamento](../mapeamento/07-negativa-tombamento.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`90173274ea7b`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, para importar no X-Forms de DEV (`/app/x-forms/forms/pedir-certidao-negativa-tombamento`). Hash `4956e23b23ac`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`H6sT6cLKqpBx5ZcBcvjpR`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 10 campos ficavam numa página só: dados pessoais, imóvel e quatro anexos.
- `[FATO]` Pedia RG do requerente e RG do proprietário junto com o CPF (C1).
- `[FATO]` A procuração era obrigatória para todos, mas a própria descrição dizia que só vale
  "não sendo o requerente o proprietário" (C9).
- `[FATO]` Quando o requerente é o proprietário, o CPF e os documentos eram pedidos duas vezes (C3).
- `[FATO]` "CFP" no lugar de "CPF" em duas descrições.
- `[FATO]` CPF do proprietário sem máscara; nenhum CPF com validação.
- `[FATO]` Não havia e-mail para a resposta (B6) e o formulário não dizia quem analisa o pedido.
- `[FATO]` Anexos sem tamanho aceito; só a certidão de matrícula dizia o formato (PDF). Nomes sem o
  prefixo `arquivo_`.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Três páginas: quem pede → imóvel → documentos | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta; e-mail novo para a resposta | C2, B6 |
| Pergunta "Você é o proprietário do imóvel?" decide o que aparece | C9 |
| CPF do proprietário, RG/CPF do proprietário e procuração só aparecem (e só são obrigatórios) para quem pede em nome do proprietário | C9, C3 |
| RG do requerente e RG do proprietário removidos: o CPF identifica a pessoa (Lei 14.534/2023) | C1 |
| CPFs com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| "Nome e localização do imóvel" em caixa de texto longo | A6 |
| "Tombamento" e "FCMS" explicados na descrição do formulário | B1, B2 |
| Anexos em PDF até 5 MB, dito na descrição da página; RG e CPF aceitam mais de um arquivo | C8 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `cpf`, `perfil_solicitante`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 3 |
| Campos | 10 | 10 (saíram os 2 RGs; entraram e-mail e "Você é o proprietário?") |
| Obrigatórios | 10 | 7 sempre + 3 só para representante (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `TOM-AAAAMMDD-XXXXXX`) → Tables `pedidos_negativa_tombamento`.
A tabela não guarda CPF de ninguém (LGPD art. 6º III). Guarda a identificação do imóvel, que é o
objeto do pedido. Anexos pelo nome do arquivo; quando há mais de um, os nomes vêm separados por vírgula.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `4956e23b23ac`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro; nome, CPF e e-mail vindos da conta |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `TOM-20261027-LG05H7` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Orientações para solicitação de certidão negativa de tombamento (ID [2312](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/2312)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/orientacoes-para-solicitacao-de-certidao-negativa-de-tombamento142> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/pedir-certidao-negativa-tombamento?serviceSlug=orientacoes-para-solicitacao-de-certidao-negativa-de-tombamento142> |

## Pendências

- Confirmar com a FCMS: pode tirar o RG do requerente e do proprietário? Na v2 eles saíram.
- Confirmar com a FCMS: a cópia do RG e CPF de quem pede é necessária? A pessoa já entra com a conta
  gov.br, que confirma o CPF (Lei 14.129/2021). Na v2 a cópia continua.
- Perguntar à FCMS: aceitar foto (JPG, PNG) nos documentos de identidade? Hoje só PDF.
- Perguntar à FCMS: a certidão de matrícula precisa ter data máxima de emissão ("atualizada" há quanto
  tempo)?
- Perguntar à FCMS: qual o prazo de resposta e como a certidão é entregue. A v2 não informa prazo.
- A v1 falava em "imóvel ou bem", mas o formulário só trata de imóvel. Confirmar se bem móvel entra.
- ~~O serviço não existe no catálogo de DEV. O teste vai usar o `serviceSlug` do exemplo do Leonardo.~~ Vinculado em 27/10/2026.
- Destino do pedido e conexão Gmail, como nos anteriores.
