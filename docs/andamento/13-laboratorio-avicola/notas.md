# IAGRO — Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola

**Origem:** Designer antigo (demo-aws), slug `cadastrar-ou-atualizar-laboratorio-de-diagnostico-em-sanidade-avicola`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [13. Laboratório — sanidade avícola](../mapeamento/13-laboratorio-avicola.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`611b8a432893`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, proposta para o X-Forms de DEV (`/app/x-forms/forms/cadastrar-laboratorio-sanidade-avicola`). Hash `586ac9fb8691`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`sEcb6w2R5yzQmCpDDum77`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 14 campos ficavam numa página só, com título e descrição em maiúsculas.
- `[FATO]` O primeiro campo era "Nome", com a descrição "nome": não dizia de quem.
- `[FATO]` A portaria de credenciamento dizia "campo obrigatório apenas para os laboratórios que forem
  credenciados junto ao MAPA", mas era opcional para todos e não havia pergunta sobre credenciamento.
- `[FATO]` O título diz "Cadastrar ou atualizar", mas o formulário não perguntava qual dos dois.
- `[FATO]` CNPJ e telefone sem máscara e sem validação; e-mail sem validação.
- `[FATO]` "Escopo" (os testes feitos) em caixa de uma linha.
- `[FATO]` Siglas sem explicação: MAPA, CRL, IE.
- `[FATO]` `name` com erro de digitação: `enredeco_completo`.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Cinco páginas: pedido → quem pede → laboratório → análises e credenciamento → endereço | A2, A3, A4 |
| Pergunta nova "Você quer": cadastro novo ou atualização | B1, C4 |
| `[INTERPRETAÇÃO]` "Nome" virou o nome de quem preenche, vindo da conta | C2, B1 |
| Pergunta nova "O laboratório é credenciado no MAPA?". A portaria só aparece e só é obrigatória para quem diz Sim (`visibleIf` + `requiredIf`) | C9 |
| Mantidas as 3 condicionais da v1: endereço, município e estado aparecem depois do CEP, agora com `requiredIf` | C9 |
| "Escopo" virou "Que análises o laboratório faz em aves?", em caixa de texto longo, com o exemplo Salmonela e Micoplasma da v1 | B1, A6 |
| CNPJ e CEP com máscara; telefone com validação que aceita fixo ou celular (sem máscara, que tem tamanho fixo) | C5, C6, D2 |
| E-mail do laboratório com validação; a resposta chega nele | D2, B6 |
| Estado com valor em sigla e nome por extenso | C4 |
| MAPA e IAGRO explicados; "opcional" escrito no rótulo | B2, B4 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `logradouro`, `telefone_laboratorio`, `email_laboratorio`, `escopo_analises`, `numero_portaria_credenciamento`, `numero_crl` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 5 |
| Campos | 14 | 16 (entraram "Você quer" e "credenciado no MAPA?") |
| Obrigatórios, não credenciado | 11 | 13 (1 já vem da conta) |
| Obrigatórios, credenciado | 11 | 14 (1 já vem da conta) |

Nenhum campo foi removido.

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `LAB-AAAAMMDD-XXXXXX`) → Tables `cadastros_laboratorio_avicola`.
A tabela não guarda telefone, CEP nem endereço completo, só município e UF (LGPD art. 6º III). Tipo de
pedido e credenciamento entram em texto ("Cadastro novo", "Sim").

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `586ac9fb8691`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `LAB-20261027-RO4LFU` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Pendências

- Confirmar com a IAGRO: o "Nome" da v1 era de quem preenche, do responsável técnico ou do laboratório?
  A v2 trata como quem preenche.
- Confirmar com a IAGRO: o que é o CRL? A v2 mantém só a sigla, sem explicar.
- Confirmar com a IAGRO: o endereço precisa mesmo aparecer só depois do CEP? A condição da v1 foi
  mantida, mas não ajuda quem preenche: o CEP é obrigatório e os campos sempre aparecem.
- Confirmar com a IAGRO: o escopo das análises é mesmo opcional? Na v1 era.
- O serviço não existe no catálogo de DEV.
- Destino do pedido e conexão Gmail, como nos anteriores.
