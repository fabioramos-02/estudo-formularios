# IAGRO — Pedir o Selo Arte

**Origem:** Designer antigo (demo-aws), slug `obter-selo-arte`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [06. Selo Arte](../mapeamento/06-selo-arte.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`498b9751607a`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, para importar no X-Forms de DEV (`/app/x-forms/forms/obter-selo-arte`). Hash `c81a8020375c`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`8bjn9jvi02Tco1J4RmGHn`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 9 campos ficavam numa página só, com o título em maiúsculas ("REQUERIMENTO DE SOLICITAÇÃO
  DE SELO ARTE").
- `[FATO]` A declaração de ciência estava na descrição da página, sem nenhum campo para a pessoa
  confirmar que leu.
- `[FATO]` Toda descrição repetia o rótulo ("Informe seu nome", "Informe o município").
- `[FATO]` "Múnicipio" com acento errado.
- `[FATO]` CPF com máscara, mas sem validação nem mensagem de erro própria.
- `[FATO]` Não havia e-mail para a resposta (B6) e o formulário não dizia quem analisa o pedido.
- `[FATO]` "Registro no serviço de inspeção" e "Número" eram dois campos sem explicação da diferença.
- `[FATO]` "Produtos" era uma linha só, para uma lista.
- `[FATO]` O anexo (logomarca) não dizia tipo nem tamanho aceito; `name` sem o prefixo `arquivo_`.
- `[FATO]` Nenhuma mensagem de erro própria; nenhuma orientação sobre o que acontece depois.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Cinco páginas: quem pede → estabelecimento → endereço → produtos e declaração → documentos | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta; e-mail novo para a resposta | C2, B6 |
| Declaração em `html` com linguagem limpa, sem mudar o sentido, e caixa de aceite obrigatória | B1, D1 |
| Produtos em caixa de texto longo, um por linha | A6 |
| CPF com validação e mensagem que diz como corrigir; `requiredErrorText` em todo obrigatório | C5, D2 |
| Descrições que repetiam o rótulo saíram; ficou só ajuda útil | B3 |
| Logomarca em PDF, JPG ou PNG até 5 MB, dito na descrição da página | C8 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `logradouro`, `declaracao_ciencia`, `arquivo_logomarca` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 5 |
| Campos | 9 | 11 (entraram e-mail e aceite da declaração) |
| Obrigatórios | 9 | 11 (3 já vêm da conta) |

Nenhum campo da v1 foi removido.

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `ART-AAAAMMDD-XXXXXX`) → Tables `pedidos_selo_arte`.
A tabela não guarda CPF nem endereço, só o município (LGPD art. 6º III). A declaração é gravada como
"Aceita"; a logomarca, pelo nome do arquivo.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `c81a8020375c`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro; nome, CPF e e-mail vindos da conta |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `ART-20261027-3WKZ6L` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Pendências

- Limpar as linhas de teste da tabela `pedidos_selo_arte` (o envio de teste repetiu 5 vezes).

- Confirmar com a IAGRO: "Registro no serviço de inspeção" é o serviço (municipal, estadual ou
  federal)? Se for, vira botões de opção com a lista que a IAGRO indicar.
- Confirmar com a IAGRO o órgão que analisa: a v1 não diz; a v2 usa IAGRO, conforme
  [Auditoria](../../05-auditoria.md).
- Perguntar à IAGRO: qual o prazo de resposta e se há outros documentos exigidos. A v2 não informa prazo.
- Perguntar à IAGRO: a logomarca precisa de tamanho ou resolução mínima?
- O serviço não existe no catálogo de DEV. O teste vai usar o `serviceSlug` do exemplo do Leonardo.
- Destino do pedido e conexão Gmail, como nos anteriores.
