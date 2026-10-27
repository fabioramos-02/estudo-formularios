# CGP/SEJUSP — Pedir cópia de laudo pericial

**Origem:** Designer antigo (demo-aws), slug `solicitar-copia-de-laudos-periciais`
**Data:** 27/10/2026
**Mapeamento do Antonio:** [12. Laudos periciais](../mapeamento/12-laudos-periciais.md)

| Arquivo | O que é |
|---|---|
| `xforms-v1-demo.json` | O que estava no ar no demo-aws. Conferido por hash (`ebe1d050de88`). |
| `gerar_v2.py` → `xforms-v2.json` | Versão 2, a importar no X-Forms de DEV (`/app/x-forms/forms/pedir-copia-laudo-pericial`). Hash `2daf7c468f9a`. |
| `gerar_fluxo.py` → `fluxo.json` | Fluxo do X-Flows de DEV (`dWZfs9hkuEAYmt6MFUdfj`). Usa `../fluxo_xflows.py`. |

## O que estava errado na v1

- `[FATO]` "Tipo de solicitante" era caixa de seleção limitada a uma escolha, e vinha no fim da página 1.
  A resposta não mudava nada no formulário.
- `[FATO]` Procuração, documento do solicitante e comprovante de parentesco eram opcionais para todos,
  com "(se aplicável)" no título. Quem precisava deles podia enviar sem.
- `[FATO]` "Nome do outorgante" tinha a ajuda "insira o nome completo do procurador". Outorgante é quem
  dá a procuração, não o procurador.
- `[FATO]` Pedia RG e órgão emissor junto com o CPF (C1).
- `[FATO]` Endereço do solicitante num campo só, com rua, número, bairro, município e CEP.
- `[FATO]` CPF sem máscara e sem validação; e-mail sem validação de formato.
- `[FATO]` "Descrição do fato" era campo de uma linha, com erro de digitação no título ("dofato").
- `[FATO]` Tipo de laudo com erro de digitação ("Análise Laboratorias", `analise_laboratorias`).
- `[FATO]` O termo de ciência era um texto de 85 palavras dentro da opção da caixa de seleção.
  "CGP", "SEJUSP", "DAEMS" e "UFERMS" sem explicação.
- `[FATO]` Anexos aceitavam `.webp` e `.zip`, sem tamanho máximo.
- `[FATO]` Data do fato e data de nascimento aceitavam data no futuro.

## O que mudou na v2

| Mudança | Regra |
|---|---|
| "Você é" sozinho na primeira página, em botões de opção. A resposta decide o que aparece depois | A3, C4, C9 |
| Procuração e nome de quem deu a procuração só para procurador; comprovante de parentesco só para familiar; documento do solicitante para os dois (`visibleIf` + `requiredIf`) | C1, C9 |
| `[INTERPRETAÇÃO]` "Nome do outorgante" virou "Nome de quem deu a procuração", obrigatório para procurador | B1, C9 |
| Documento de identificação da pessoa envolvida passou a ser obrigatório para todos | C9 |
| Seis páginas: quem pede → seus dados → endereço → fato e laudo → documentos → condições | A2, A3, A4 |
| Nome, CPF e e-mail pré-preenchidos com a conta | C2 |
| RG e órgão emissor removidos: o CPF identifica a pessoa (Lei 14.534/2023) | C1 |
| Endereço em CEP, endereço, bairro, município e estado (sigla + nome por extenso) | C4, C5 |
| CPF, CEP e celular com máscara, validação e mensagem que diz como corrigir | C5, D2 |
| Datas não aceitam dia futuro (`maxValueExpression: "today()"`) | C4, D2 |
| Relato do fato e informações adicionais em caixa de texto longo | A6 |
| Tipo de laudo com erro corrigido e valores `analises_laboratoriais`, `criminalistica`, `identificacao`, `medicina_legal`; diz que pode ficar em branco | B1, C7 |
| Condições do termo em lista, com o mesmo conteúdo da v1; aceite numa opção curta | B1 |
| CGP, SEJUSP, DAEMS e UFERMS por extenso na primeira vez | B2 |
| Anexos em PDF, JPG ou PNG até 5 MB, vários arquivos por anexo (frente e verso) | C8 |
| "Depois do envio" em `html` na última página, com o que a v1 já dizia (e-mail com orientações e guia) | B6 |
| `name` canônico: `perfil_solicitante`, `nome_completo`, `cpf`, `email`, `telefone_celular`, `logradouro`, `municipio`, `uf`, `aceite_condicoes`, `arquivo_*` | C7 |

| | v1 | v2 |
|---|---|---|
| Páginas | 3 | 6 |
| Campos | 22 | 24 (saíram RG e órgão emissor; endereço virou 5 campos) |
| Obrigatórios, pessoa envolvida | 13 | 16 (3 já vêm da conta) |
| Obrigatórios, procurador | 13 | 19 (3 já vêm da conta) |
| Obrigatórios, familiar | 13 | 18 (3 já vêm da conta) |

## Fluxo (X-Flows de DEV)

Webhook → CODE (protocolo `LAU-AAAAMMDD-XXXXXX`) → Tables `pedidos_copia_laudos`.
A tabela guarda o que serve para achar o laudo e acompanhar o pedido: perfil, nome da vítima, data do
fato, número da ocorrência e tipo de laudo. Não guarda CPF, data de nascimento, celular, endereço
completo nem o relato, só município e UF (LGPD art. 6º III). Os anexos entram pelo nome dos arquivos,
separados por `;`.

## Teste em DEV (27/10/2026)

| Teste | Resultado |
|---|---|
| Importação por API (`createForm`) | schema salvo igual ao local (hash `2daf7c468f9a`), publicado, webhook certo |
| Abrir o formulário no portal | abriu sem erro |
| Envio por API (`submitFormResponse`) com `resposta-teste.json` (dados fictícios, primeira opção de cada escolha) | aceito → `SUCCEEDED` → linha `LAU-20261027-S724J3` |

Não testado pela tela: os outros caminhos das condições e as mensagens de erro. O envio por API pula a validação da tela.

## Serviço no catálogo (27/10/2026)

| | |
|---|---|
| Serviço no CMS | Solicitar cópia de laudos periciais (ID [1309](https://cms.app.dev.pgd.ms.gov.br/admin/content/services/1309)) |
| Página do serviço | <https://portal.dev.pgd.ms.gov.br/servicos/emissao-de-copia-de-laudos-periciais145> |
| Acessar serviço | <https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/pedir-copia-laudo-pericial?serviceSlug=emissao-de-copia-de-laudos-periciais145> |

## Pendências

- Confirmar com a CGP: pode tirar o RG e o órgão emissor? Na v2 eles saíram.
- Confirmar com a CGP: "Nome do outorgante" é o nome de quem deu a procuração? A ajuda da v1 dizia
  "nome do procurador".
- Confirmar com a CGP: o documento da pessoa envolvida é obrigatório para todos? Na v1 era opcional;
  na v2 ficou obrigatório.
- Confirmar com a CGP: "pessoa envolvida no fato" é sempre a vítima? A v1 pede "Nome da vítima" para
  todos os perfis.
- Confirmar com a CGP: quem conta como familiar de 1º grau (pais e filhos; cônjuge entra?). Precisa da
  certidão de óbito?
- Confirmar com a CGP: os formatos `.webp` e `.zip` da v1 eram necessários? Na v2 ficaram PDF, JPG e PNG,
  até 5 MB.
- Confirmar com a CGP: qual o prazo para o e-mail com as orientações chegar. A v2 não promete prazo.
- ~~O serviço não existe no catálogo de DEV.~~ Vinculado em 27/10/2026. Destino do pedido e conexão Gmail, como nos anteriores.
