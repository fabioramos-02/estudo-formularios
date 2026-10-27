# IAGRO — Cadastrar ou atualizar empresa integradora de aves ou suínos

**Origem:** Designer antigo (demo-aws), slug `cadastrar-ou-atualizar-empresa-integradora-de-ave-ou-suino`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [10. Empresa integradora — ave/suíno](../mapeamento/10-empresa-integradora.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`ed6fec40473d`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, proposta para o X-Forms de DEV (`/app/x-forms/forms/cadastrar-empresa-integradora-aves-suinos`). Hash `3c4f5f5f9e72`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`nxaMG6ua1oO6kgwsMmNDD`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` 13 campos na segunda página, com título e descrição iguais e em maiúsculas ("FICHA DE CADASTRO…").
- `[FATO]` O título diz "Cadastrar ou atualizar", mas o formulário não perguntava qual dos dois.
- `[FATO]` "Integradora de" era caixa de seleção com mínimo e máximo de 1 opção: na prática, escolha
  única. E não era obrigatória, apesar do mínimo de 1.
- `[FATO]` UF não era obrigatória, mas Município era.
- `[FATO]` CNPJ e CEP sem máscara e sem validação; os dois e-mails sem validação.
- `[FATO]` "Informações complementares" em caixa de uma linha.
- `[FATO]` "IE" sem explicação na descrição ("nº da IE"); `name` das páginas com acento (`página1`).

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Cinco páginas: pedido → representante legal → empresa → endereço → mais informações | A2, A3, A4 |
| Pergunta nova "Você quer": cadastro novo ou atualização | B1, C4 |
| "Integradora de" em botões de opção (`radiogroup`), obrigatória | C4 |
| `[INTERPRETAÇÃO]` Estado ficou obrigatório, como o município | B4 |
| CNPJ, CEP e telefones com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| E-mails com validação | D2 |
| Estado com valor em sigla e nome por extenso | C4 |
| "Informações complementares" em caixa de texto longo, até 1.000 caracteres | A6 |
| "Opcional" escrito no rótulo dos campos que não são obrigatórios | B4 |
| IAGRO, avicultura e suinocultura explicadas na descrição do formulário | B2 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_representante_legal`, `municipio`, `uf`, `atividade_integradora` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 2 | 5 |
| Campos | 16 | 17 (entrou "Você quer") |
| Obrigatórios | 11 | 14 (entraram "Você quer", "Integradora de" e Estado) |

Nenhum campo foi removido. Nome e e-mail do representante **não** vêm da conta: quem preenche pode
não ser o representante legal.

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `INT-AAAAMMDD-XXXXXX`) → Tables `cadastros_empresa_integradora`.
A tabela não guarda telefones, CEP nem coordenada, só município e UF (LGPD art. 6º III). Tipo de pedido
e atividade entram em texto ("Atualização", "Avicultura").

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `3c4f5f5f9e72`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `INT-20261027-CNNAVX` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Pendências

- Confirmar com a IAGRO: quem costuma preencher é o próprio representante legal? Se for, nome e e-mail
  podem vir da conta (C2).
- Confirmar com a IAGRO: uma empresa pode ser integradora de aves **e** de suínos? A v1 só aceitava uma.
- Confirmar com a IAGRO: a resposta vai para o e-mail do representante ou da empresa? A v2 diz
  "do representante legal".
- Confirmar com a IAGRO: o endereço da empresa não tem rua e número na v1 (só CEP, município, via de
  acesso e coordenada). Basta assim?
- Confirmar com a IAGRO: o formato da coordenada geográfica. A v2 mantém o exemplo da v1
  ("S: -20.00000 -50.00000"), sem validação.
- O serviço não existe no catálogo de DEV.
- Destino do pedido e conexão Gmail, como nos anteriores.
