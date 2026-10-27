# FCMS — Cadastrar biblioteca no Sistema Estadual de Bibliotecas Públicas

**Origem:** Designer antigo (demo-aws), slug `cadastro-no-sistema-estadual-de-bibliotecas-publicas-de-mato-grosso-do-sul-sebpms`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [09. Bibliotecas públicas](../mapeamento/09-bibliotecas-publicas.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`1a8b57a23373`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, para importar no X-Forms de DEV (`/app/x-forms/forms/cadastrar-biblioteca-publica`). Hash `283f55d01c91`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`aJIQiLJiONonf9NVwDx4u`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` A primeira página tinha 18 campos misturando responsável, biblioteca, horário, equipe,
  endereço e acessibilidade.
- `[FATO]` Os anexos ficavam no meio (página 2) e os dados da instituição no fim (página 3) (A3).
- `[FATO]` "Está em funcionamento?" e "Tipo de biblioteca" eram caixas de seleção limitadas a 1 opção,
  no lugar de botões de opção.
- `[FATO]` "Tipo de documento da instituição" era caixa de seleção sem limite: dava para marcar CNPJ
  e CPF ao mesmo tempo. O número vinha num campo só, sem máscara.
- `[FATO]` "Respondeu ao diagnóstico mais recente?" era Sim/Não (`boolean`) obrigatório. No portal o
  `boolean` começa em "Não", então a pergunta passava sem resposta de verdade.
- `[FATO]` Três campos escondidos tinham `isRequired: true` em vez de `requiredIf` (C9).
- `[FATO]` "Nomes de quem trabalha" aparecia mesmo quando o número de pessoas era 0.
- `[FATO]` "Número de pessoas" tinha um validador `expression` vazio.
- `[FATO]` Endereços num campo de texto só, sem máscara de CEP. O endereço da instituição não pedia
  município.
- `[FATO]` E-mail da instituição sem validação de formato.
- `[FATO]` A descrição da página 2 pedia "comprovante de funcionamento", mas não havia campo para ele.
- `[FATO]` Fotos só em JPEG; anexos sem tamanho aceito; nomes sem o prefixo `arquivo_`.
- `[FATO]` Erros de digitação no `name` (`nome_instiucao_vinculada`, `cargo_reponsavel_instituicao`,
  `endereco_intituicao`) e descrições que repetiam o rótulo.
- `[FATO]` Nenhuma mensagem de erro própria; nenhuma orientação sobre o que acontece depois.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| Sete páginas: biblioteca → responsável → funcionamento → endereço e contato → instituição → responsável pela instituição → documentos | A2, A3, A4 |
| Escolha única em botões de opção, com valores curtos (`publica`, `comunitaria`, `sim`, `nao`) | C4 |
| "Diagnóstico" vira Sim/Não em botões, sem resposta marcada de início | C4, B4 |
| Campos escondidos com `visibleIf` + `requiredIf`: lei de criação (pública), horário (funcionando), CNPJ ou CPF da instituição | C9 |
| "Mais informações do horário" só aparece se a biblioteca funciona; "nomes de quem trabalha" só se o número for maior que 0 | C9 |
| Endereço da biblioteca em CEP, endereço, bairro e município; CEP com máscara e validação | C4, C5 |
| CNPJ ou CPF da instituição em campos próprios, com máscara e validação; telefone com validação | C5, D2 |
| E-mail da instituição com validação; a resposta chega nele | B6, D2 |
| Campos opcionais marcados "(opcional)" no rótulo | B4 |
| "FCMS" explicada na descrição do formulário | B2 |
| Fotos em JPG ou PNG; documentos em PDF; até 5 MB, dito na descrição da página | C8 |
| "Depois do envio" em `html` na última página | B6 |
| `name` corrigidos e canônicos (`tipo_biblioteca`, `em_funcionamento`, `logradouro_biblioteca`, `arquivo_*`…) | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 3 | 7 |
| Campos | 31 | 34 (endereço da biblioteca virou CEP + endereço + bairro; número do documento virou CNPJ ou CPF) |
| Obrigatórios | 23 (3 deles escondidos com `isRequired`) | 21 sempre + 5 condicionais |

Nenhum campo da v1 foi removido. Não há campo de quem preenche: a v1 não tinha e não ficou claro se é
sempre o responsável pela biblioteca.

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `BIB-AAAAMMDD-XXXXXX`) → Tables `cadastros_bibliotecas_publicas`.
A tabela não guarda CPF, telefone nem endereços completos, só o município (LGPD art. 6º III). Guarda o
CNPJ da instituição quando houver e o e-mail da instituição, para a resposta. Escolhas em texto legível
("Pública", "Sim"); anexos pelo nome do arquivo, separados por vírgula quando há mais de um.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `283f55d01c91`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `BIB-20261027-60EKBQ` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Pendências

- Perguntar à FCMS: o que é o "diagnóstico mais recente das bibliotecas" e onde se responde? Hoje o
  formulário não explica.
- Perguntar à FCMS: o que é biblioteca "Associada"? Acrescentar uma ajuda curta a cada tipo.
- Perguntar à FCMS: o "comprovante de funcionamento" (fotos atuais, horário e endereço) da v1 é a foto
  da fachada e a de divulgação, ou falta um anexo? A v2 não criou campo novo.
- Perguntar à FCMS: quem costuma preencher é o responsável pela biblioteca? Se sim, o nome dele pode vir
  da conta (`autocomplete: "name"`).
- Perguntar à FCMS: escolaridade pode virar lista de opções? Hoje é texto livre.
- Perguntar à FCMS: telefone fixo (10 números) é comum? A máscara aceita só celular, como na v1.
- Perguntar à FCMS: qual o prazo de resposta. A v2 não informa prazo.
- O serviço não existe no catálogo de DEV. O teste vai usar o `serviceSlug` do exemplo do Leonardo.
- Destino do pedido e conexão Gmail, como nos anteriores.
