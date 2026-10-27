# IAGRO — Cadastrar ou atualizar médico veterinário de aves ou suínos

**Origem:** Designer antigo (demo-aws), slug `cadastrar-ou-atualizar-medico-veterinario-avicultura-ou-suinocultura`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [08. Veterinário — avicultura/suinocultura](../mapeamento/08-veterinario-avi-suino.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`967dd2a2cfbc`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, proposta para o X-Forms de DEV (`/app/x-forms/forms/cadastrar-veterinario-aves-suinos`). Hash `118236e6e4fb`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`GZk1GB2cCfvqkBSjneilf`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` 13 campos na primeira página, com título e descrição em maiúsculas ("FICHA DE CADASTRO…").
- `[FATO]` Pedia RG, órgão expedidor e UF do órgão junto com o CPF (C1).
- `[FATO]` O e-mail do veterinário tinha a descrição "e-mail do laboratório", copiada de outro formulário.
- `[FATO]` Os dois telefones eram obrigatórios, inclusive o "Telefone Adicional".
- `[FATO]` "Vinculado a alguma empresa…" era `boolean` obrigatório. No portal o booleano começa em
  "Não", então a obrigação não fazia nada.
- `[FATO]` O título diz "Cadastrar ou atualizar", mas o formulário não perguntava qual dos dois.
- `[FATO]` CPF, CNPJ e CEP sem máscara e sem validação; e-mail sem validação.
- `[FATO]` O anexo da portaria não tinha título (só o `name` `documento_portaria_habitacao_mapa`).
- `[FATO]` Anexos sem tipo nem tamanho aceito. Siglas sem explicação: CRMV, MAPA, GTA.
- `[FATO]` `name` com erro: `portaria_habitacao` (é "habilitação"), `empresa_vincula`.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Seis páginas: pedido → seus dados → endereço → vínculo → empresa → documentos. As duas últimas só aparecem para quem tem vínculo | A2, A3, A4 |
| Pergunta nova "Você quer": cadastro novo ou atualização | B1, C4 |
| `[INTERPRETAÇÃO]` Quem preenche é o próprio veterinário: nome, CPF e e-mail vêm da conta | C2, B6 |
| RG, órgão expedidor e UF do órgão removidos: o CPF identifica a pessoa | C1 |
| "Vínculo com empresa" em botões Sim/Não (`radiogroup`), no lugar do booleano | C4, C9 |
| Campos da empresa e anexos com `requiredIf`: só obrigatórios para quem tem vínculo | C9 |
| Telefones mantidos em `multipletext`; o segundo virou opcional | C1, B4 |
| CPF, CNPJ, CEP e celular com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| Estado com valor em sigla e nome por extenso | C4 |
| CRMV, MAPA e GTA escritos por extenso na primeira vez; IAGRO na descrição do formulário | B2 |
| Anexos em PDF até 5 MB, dito na descrição da página; portaria aceita vários arquivos, como na v1 | C8 |
| "Depois do envio" em `html` na última página dos dois caminhos | B6 |
| `name` canônico: `nome_completo`, `logradouro`, `numero_crmv`, `empresa_vinculada`, `numero_portaria_mapa`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 2 (a segunda condicional) | 6 (as duas últimas condicionais) |
| Campos | 18 | 16 (saíram RG, órgão e UF do órgão; entrou "Você quer") |
| Obrigatórios, sem vínculo | 12 | 10 (3 já vêm da conta) |
| Obrigatórios, com vínculo | 17 (e o booleano não obrigava nada) | 15 (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `VET-AAAAMMDD-XXXXXX`) → Tables `cadastros_veterinario_avi_suino`.
A tabela não guarda CPF, telefones nem endereço completo, só município e UF (LGPD art. 6º III). O tipo
de pedido e o vínculo entram em texto ("Cadastro novo", "Sim"). Os anexos entram pelo nome do arquivo;
a portaria, que aceita vários, pelos nomes separados por `;`.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `118236e6e4fb`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `VET-20261027-VH6OBA` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Cadastrar ou atualizar médico veterinário - avicultura ou suinocultura (ID [2440](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/2440)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/cadastrar-ou-atualizar-medico-veterinario-avicultura-ou-suinocultura84> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/cadastrar-veterinario-aves-suinos?serviceSlug=cadastrar-ou-atualizar-medico-veterinario-avicultura-ou-suinocultura84> |

## Pendências

- Confirmar com a IAGRO: pode tirar o RG? Na v2 ele saiu.
- Confirmar com a IAGRO: quem preenche é sempre o próprio veterinário? Se a empresa integradora ou a
  cooperativa cadastrar o veterinário, os campos pessoais não podem vir da conta (ver `01-wordpress`).
- Confirmar com a IAGRO: o número no CRMV-MS é mesmo opcional? Na v1 era.
- Confirmar com a IAGRO: o segundo telefone pode ser opcional? Na v2 é.
- Confirmar com a IAGRO: a portaria de habilitação no MAPA vale para todo veterinário com vínculo ou
  só para quem emite GTA? A v1 dizia "quando for emitir GTA", mas obrigava todos.
- Confirmar com a IAGRO: que documento comprova o vínculo com a empresa ou cooperativa.
- ~~O serviço não existe no catálogo de DEV.~~ Vinculado em 27/10/2026.
- Destino do pedido e conexão Gmail, como nos anteriores.
