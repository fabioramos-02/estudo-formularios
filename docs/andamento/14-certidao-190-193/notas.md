# SEJUSP — Pedir certidão de atendimento de emergência (190 ou 193)

**Origem:** Designer antigo (demo-aws), slug `solicitar-emissao-de-certidao-de-atendimento-de-emergencia-teste`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [14. Certidão 190/193](../mapeamento/14-certidao-190-193.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`07a70ee96768`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, a importar no X-Forms de DEV (`/app/x-forms/forms/pedir-certidao-atendimento-190-193`). Hash `7bb3bd919892`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`YyOm7iK7xlkACYgvE1R3o`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` A descrição diz que o serviço vale para Campo Grande, Dourados, Corumbá e Ponta Porã, mas a
  cidade do fato era uma lista com os 79 municípios, opcional e na segunda página. Quem é de outra
  cidade só descobria no fim, se lesse a descrição.
- `[FATO]` 190 ou 193 era caixa de seleção limitada a uma escolha, com o título "Telefone de origem das
  chamadas de emergência".
- `[FATO]` "Data e horário do fato" era um campo só de data e hora, que exige a hora, mas a ajuda dizia
  "se possível, o horário aproximado".
- `[FATO]` "Informações adicionais" era obrigatório, mas a ajuda dizia "outras informações que considere
  relevantes".
- `[FATO]` A página 1 tinha 12 campos: dados pessoais, endereço e os 4 anexos. Documento do representante
  e procuração eram opcionais para todos, e o formulário não perguntava se quem preenche é a pessoa
  que ligou.
- `[FATO]` CPF sem máscara e sem validação; e-mail sem validação de formato.
- `[FATO]` A cidade de quem ligou era opcional, embora o endereço fosse obrigatório.
- `[FATO]` Anexos sem tamanho máximo, e todos aceitavam vários arquivos.
- `[FATO]` Erro de digitação na ajuda da finalidade ("registro de atendimento..Ex.").
- `[FATO]` A JSON tem 19 campos; o mapeamento registra 18.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Elegibilidade primeiro: 190 ou 193 e cidade do fato na primeira página; aviso, sem bloquear, quando a cidade não é uma das quatro | A3, B3, C9 |
| "Você é" sozinho na página: a pessoa que ligou, representante legal ou procurador | A3, C9 |
| Documento do representante só para representante e procurador; procuração só para procurador (`visibleIf` + `requiredIf`) | C1, C9 |
| Nome de quem preenche só quando é outra pessoa. Nome e CPF de quem ligou pré-preenchidos com a conta e apagados (`resetValueIf`) quando quem preenche é outra pessoa | C2, C9 |
| E-mail e celular são de quem preenche: a resposta vai para essa pessoa | B6, C3 |
| Seis páginas: ligação → quem pede → contato → quem ligou → o que aconteceu → documentos | A2, A3, A4 |
| 190 e 193 em botões de opção, com o nome do serviço ao lado | B1, C4 |
| Data do fato em campo de data (não aceita dia futuro) e hora aproximada em campo próprio e opcional | C4, C9 |
| "Informações adicionais" passou a ser opcional | B4, C1 |
| Cidade de quem ligou passou a ser obrigatória | C9 |
| CPF e celular com máscara, validação e mensagem que diz como corrigir; e-mail validado | C5, D2 |
| Anexos em PDF até 5 MB; só "Outros documentos" aceita vários arquivos | C8 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `perfil_solicitante`, `nome_completo`, `email`, `telefone_celular`, `data_fato`, `hora_fato`, `municipio_ocorrencia`, sufixo `_ligou` para os dados de quem ligou, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 2 | 6 |
| Campos | 19 | 22 (entraram "Você é", o nome de quem preenche e a hora separada da data) |
| Obrigatórios, a pessoa que ligou | 13 | 15 (3 já vêm da conta) |
| Obrigatórios, representante legal | 13 | 17 (2 já vêm da conta) |
| Obrigatórios, procurador | 13 | 18 (2 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `CER-AAAAMMDD-XXXXXX`) → Tables `pedidos_certidao_emergencia`.
A tabela guarda o que serve para achar a ligação: 190 ou 193, cidade, data e hora do fato. Não guarda
CPF, data de nascimento, celular, endereços nem o relato (LGPD art. 6º III). O nome do pedido é o de
quem preenche (ou o de quem ligou, quando é a mesma pessoa). Os anexos entram pelo nome do arquivo.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `7bb3bd919892`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `CER-20261027-ZCAUNU` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Solicitar emissão de certidão de atendimento de emergência (ID [1400](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/1400)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/emissao-de-certidao-de-atendimento66> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/pedir-certidao-atendimento-190-193?serviceSlug=emissao-de-certidao-de-atendimento66> |

## Pendências

- Confirmar com a SEJUSP: o serviço atende só Campo Grande, Dourados, Corumbá e Ponta Porã? Se sim, o
  aviso da cidade pode virar bloqueio (validador) e a lista pode ter só as quatro cidades.
- Confirmar com a SEJUSP: para achar a ligação, precisa do número de telefone de onde se ligou? A v1 só
  pede um telefone de contato.
- Confirmar com a SEJUSP: o endereço de quem ligou é necessário para emitir a certidão (C1)?
- Confirmar com a SEJUSP: o documento de identificação continua necessário, já que o CPF vem da conta?
- Confirmar com a SEJUSP: "Informações adicionais" e a hora do fato podem ser opcionais? Na v2 são.
- Confirmar com a SEJUSP: a finalidade pode virar lista de opções (uso pessoal, administrativo,
  judicial, como diz a descrição)?
- Confirmar com a SEJUSP: qual unidade emite a certidão e em quanto tempo responde. A v2 não promete prazo.
- `[HIPÓTESE]` `resetValueIf` apaga o nome e o CPF que a conta preencheu quando a pessoa escolhe
  representante ou procurador. Se voltar para "a pessoa que ligou", os campos ficam vazios. Conferir
  em **Visualizar** no portal.
- ~~O serviço não existe no catálogo de DEV.~~ Vinculado em 27/10/2026. Destino do pedido e conexão Gmail, como nos anteriores.
