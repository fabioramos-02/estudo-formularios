# IAGRO — Pedir certificado de destruição de soqueira de algodão

**Origem:** Designer antigo (demo-aws), slug `requerer-certificado-de-destruicao-de-soqueira-de-algodao`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [11. Soqueira de algodão](../mapeamento/11-soqueira-algodao.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`a8e73f23c2a3`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, a importar no X-Forms de DEV (`/app/x-forms/forms/pedir-certificado-destruicao-soqueira-algodao`). Hash `A_PREENCHER`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`A_PREENCHER`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` Os 8 campos ficavam numa página só, com o título "REQUERIMENTO DE CERTIFICADO" em maiúsculas.
- `[FATO]` Erro de digitação na descrição do formulário ("Solicicitação").
- `[FATO]` "Área de plantio" era caixa de seleção com a ajuda "selecione uma ou duas opções", mas as duas
  opções se excluem: até 50 hectares ou acima de 50 hectares.
- `[FATO]` CPF sem máscara e sem validação; e-mail sem validação de formato.
- `[FATO]` "RF", "DAEMS", "E-Saniagro" e "IAGRO" sem explicação.
- `[FATO]` Anexos sem tipo nem tamanho aceito, e todos aceitavam vários arquivos.
- `[FATO]` O anexo "Comprovante de pagamento" tinha a descrição igual ao título.
- `[FATO]` Nenhuma mensagem de erro própria; nada sobre o que acontece depois do envio.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Três páginas: seus dados → área de plantio → documentos | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta | C2 |
| Área de plantio em botões de opção (uma resposta só), valores `ate_50_hectares` e `acima_50_hectares` | C4 |
| CPF e celular com máscara, validação e mensagem que diz como corrigir; e-mail validado | C5, D2 |
| "IAGRO", "soqueira", "RF" e "DAEMS" explicados na primeira vez; e-Saniagro apresentado como sistema da IAGRO | B1, B2 |
| Ajuda da área diz que a guia DAEMS depende do tamanho (vem da v1) | B3 |
| Anexos em PDF até 5 MB, um arquivo cada, dito na descrição da página | C8 |
| Mensagem de erro própria em todo campo obrigatório | D2 |
| "Depois do envio" em `html` na última página | B6 |
| `name` canônico: `nome_completo`, `telefone_celular`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 1 | 3 |
| Campos | 8 | 8 |
| Obrigatórios | 8 | 8 (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `SOQ-AAAAMMDD-XXXXXX`) → Tables `pedidos_certificado_soqueira`.
A tabela não guarda CPF nem celular, que ficam só nas respostas do X-Forms (LGPD art. 6º III). A área
de plantio é gravada em texto legível. Os anexos entram pelo nome do arquivo.

## Teste em DEV

A fazer.

## Pendências

- Confirmar com a IAGRO: algum caso precisa de mais de um arquivo por anexo (por exemplo, mais de um
  Relatório de Fiscalização)? A v1 aceitava vários; a v2 aceita um.
- Confirmar com a IAGRO: o tamanho de 5 MB por anexo serve? Foto do documento (JPG/PNG) é aceita?
- Confirmar com a IAGRO: onde se emite a guia DAEMS e qual o valor de cada faixa de área. Hoje o
  formulário não diz.
- Confirmar com a IAGRO: o pedido precisa identificar a propriedade (nome, município, inscrição)? A v1
  não pede nada sobre ela.
- `[HIPÓTESE]` O comprovante de pagamento da DAEMS pode ser conferido pelo governo, sem anexo (Lei
  14.129/2021). Perguntar à IAGRO.
- O serviço não existe no catálogo de DEV. Destino do pedido e conexão Gmail, como nos anteriores.
