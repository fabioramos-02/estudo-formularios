# Fundect — Pedir diárias e passagens

**Origem:** Designer antigo (demo-aws), slug `solicitacao-de-diarias-para-servidores-da-fundect`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [03. Diárias Fundect](../mapeamento/03-diarias-fundect.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`fcf5aeb53564`). |
| `xforms-v2.json` | Versão 2, importada no X-Forms de DEV (`/app/x-forms/forms/pedir-diarias-passagens-fundect`). |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV. Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` **O servidor não conseguia enviar.** A página 3 dizia "servidores não precisam preencher", mas
  CPF, banco, agência e conta eram obrigatórios e a página aparecia para todo mundo.
- `[FATO]` "Tipo de solicitação" era caixa de seleção limitada a 1 (C4).
- `[FATO]` "Veículo utilizado" estava com `visible: false`: ninguém via.
- `[FATO]` Datas eram texto livre, e o validador de "Data/Saída" estava vazio (sem expressão).
- `[FATO]` "Agência" sem título; "CFP" no lugar de CPF; texto em português de Portugal ("eletrónico",
  "comprovativos").
- `[FATO]` RG opcional pedido junto com o CPF (C1).

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Pergunta nova "Você é servidor ou estagiário?"; página de dados bancários só para estagiário (`visibleIf` na página) | C1, C9 |
| Nome, e-mail e CPF pré-preenchidos com a conta (`autocomplete`) | C2 |
| E-mail novo (pré-preenchido), para a resposta do pedido | B6 |
| Tipo de solicitação: escolha única, rótulo "O que você precisa?" | C4, B1 |
| "Como você vai viajar?" aparece quando o pedido é só de diárias | C9 |
| Datas com `inputType: "date"` e validador "volta ≥ ida", com mensagem que diz como corrigir | C4, D2 |
| Anexo: PDF até 5 MB, opcional, dito no título e na descrição | C8 |
| RG removido | C1 |
| `tooltip` em vínculo, nome, e-mail e no campo de veículo | B3 |
| "Depois do envio" em `html` na última página de cada caminho | B6 |
| `name` canônico: `nome_completo`, `tipo_solicitacao`, `conta`, `arquivo_documento_pessoal` | C7 |

| | v1 | v2 |
|---|---|---|
| Campos | 15 | 16 (entrou vínculo e e-mail, saiu RG) |
| Obrigatórios para o servidor | 12, mais 4 bancários que ele não devia preencher | 8 (3 já vêm da conta) |
| Obrigatórios para o estagiário | 12 | 12 (4 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `FUN-AAAAMMDD-XXXXXX`) → Tables `solicitacoes_diarias_fundect`.
A tabela não guarda CPF nem dados bancários: diz só onde eles estão ("Nas respostas do X-Forms" ou
"No sistema de RH"). LGPD art. 6º III. O anexo entra pelo nome do arquivo.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Nome, e-mail e CPF vindos da conta | `[FATO]` os três preenchidos. `autocomplete: "cpf"` funciona. |
| Data de volta antes da ida | bloqueou com "A data de volta precisa ser no mesmo dia ou depois da data de ida." |
| Só diárias → "Como você vai viajar?" | apareceu |
| Estagiário → página de dados bancários | apareceu |
| Envio | "Resposta enviada!" → `SUCCEEDED` → linha `FUN-20261027-HTEZUS` |

Não testado: caminho do servidor (a página bancária deve sumir) e o envio com anexo.

## Pendências

- Serviço da Fundect não existe no catálogo de DEV. O teste usou o `serviceSlug` do exemplo do Leonardo.
- Confirmar com a Fundect: estagiário tem matrícula? O documento com foto vale só para estagiário?
- Destino do pedido e conexão Gmail, como no WordPress.
