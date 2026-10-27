# Relatório consolidado — os 14 formulários no X-Forms de DEV

**Secretaria-Executiva de Transformação Digital — SETDIG** · Superintendência de Governo Digital (SGD)
**Data:** 27/10/2026
**Para:** Leonardo (X-VIA) e os órgãos donos dos serviços

## Resumo

- `[FATO]` Os 14 formulários do estudo estão no **X-Forms** e no **X-Flows** de DEV, melhorados pelo
  padrão do estudo. O X-Forms monta o formulário; o X-Flows recebe a resposta, gera um protocolo e grava
  o pedido numa tabela.
- `[FATO]` Cada formulário recebeu pelo menos um envio de teste, e o fluxo rodou sem erro nos 14.
- `[FATO]` Nenhum dos 14 serviços existe no catálogo do portal de DEV. Os testes usaram o serviço de
  exemplo do Leonardo.
- `[FATO]` O pedido ainda não chega a ninguém: falta definir o destino de cada órgão e criar a conexão
  de e-mail no X-Flows.
- Os órgãos precisam responder perguntas sobre os próprios serviços. A lista está no fim, por órgão.

## Os 14 formulários

Endereço em DEV: `https://portal.dev.pgd.ms.gov.br/app/x-forms/forms/<slug>?serviceSlug=<serviço>`.

| # | Órgão | Formulário (slug em DEV) | Páginas v1 → v2 | Teste | Diário |
|---|---|---|---|---|---|
| 1 | SETDIG | `solicitar-acesso-wordpress` | 7 → 5 | pela tela | [notas](andamento/01-wordpress/notas.md) |
| 2 | Fundect | `pedir-diarias-passagens-fundect` | 3 → 3 | pela tela | [notas](andamento/02-diarias-fundect/notas.md) |
| 3 | IAGRO | `cadastrar-responsavel-tecnico-agricola` | 1 → 3 | pela tela | [notas](andamento/03-rt-agricola/notas.md) |
| 4 | IAGRO | `cadastrar-industria-agrotoxicos-e-saniagro` | 1 → 4 | pela tela, 2 caminhos | [notas](andamento/04-industria-agrotoxicos/notas.md) |
| 5 | IAGRO | `cancelar-registro-empresa-agrotoxicos` | 1 → 4 | pela tela | [notas](andamento/05-cancelar-agrotoxicos/notas.md) |
| 6 | IAGRO | `obter-selo-arte` | 1 → 5 | por API | [notas](andamento/06-selo-arte/notas.md) |
| 7 | FCMS | `pedir-certidao-negativa-tombamento` | 1 → 3 | por API | [notas](andamento/07-negativa-tombamento/notas.md) |
| 8 | IAGRO | `cadastrar-veterinario-aves-suinos` | 2 → 6 | por API | [notas](andamento/08-veterinario-avi-suino/notas.md) |
| 9 | FCMS | `cadastrar-biblioteca-publica` | 3 → 7 | por API | [notas](andamento/09-bibliotecas-publicas/notas.md) |
| 10 | IAGRO | `cadastrar-empresa-integradora-aves-suinos` | 2 → 5 | por API | [notas](andamento/10-empresa-integradora/notas.md) |
| 11 | IAGRO | `pedir-certificado-destruicao-soqueira-algodao` | 1 → 3 | pela tela | [notas](andamento/11-soqueira-algodao/notas.md) |
| 12 | CGP | `pedir-copia-laudo-pericial` | 3 → 6 | por API | [notas](andamento/12-laudos-periciais/notas.md) |
| 13 | IAGRO | `cadastrar-laboratorio-sanidade-avicola` | 1 → 5 | por API | [notas](andamento/13-laboratorio-avicola/notas.md) |
| 14 | SEJUSP | `pedir-certidao-atendimento-190-193` | 2 → 6 | por API | [notas](andamento/14-certidao-190-193/notas.md) |

"Pela tela" quer dizer preenchido no portal, como o cidadão faz. "Por API" quer dizer que a resposta foi
enviada direto ao portal, sem passar pela tela. Esse teste confirma o caminho até a tabela, mas não as
mensagens de erro nem os outros caminhos das perguntas condicionais.

## O que mudou em todos

| Mudança | Por quê |
|---|---|
| Uma página por assunto, com barra de progresso | Quem preenche sabe onde está e quanto falta (GOV.UK, gov.br) |
| Nome, CPF e e-mail vêm da conta gov.br | Não pedir o que o governo já tem (Lei 14.129/2021) |
| Campo que só vale num caso só aparece nesse caso | Ex.: procuração só para quem representa outra pessoa |
| Mensagem de erro que diz como corrigir | "Digite o CNPJ com 14 números." no lugar de "Campo obrigatório" |
| Máscara e validação em CPF, CNPJ, CEP e telefone | Menos erro de digitação |
| Anexo diz formato e tamanho | PDF (ou foto) até 5 MB |
| "Depois do envio" na última página | O portal não mostra a tela final do SurveyJS |
| E-mail para a resposta, onde a v1 não tinha | Hoje o órgão não tinha como responder |
| RG removido onde já se pede CPF (05, 07, 08, 12; Fundect no 02) | O CPF basta para identificar a pessoa (Lei 14.534/2023). **Cada órgão precisa confirmar.** |

A tabela do X-Flows guarda só o que serve para acompanhar o pedido. CPF, telefone, endereço completo e
dados bancários ficam só nas respostas do X-Forms (LGPD, art. 6º, III).

## Para o Leonardo (X-VIA)

### Para colocar os serviços no ar

1. **Catálogo.** Cadastrar os 14 serviços no catálogo do portal de DEV, ou indicar os slugs que já
   existem. Sem isso o link não funciona para o cidadão ("Erro ao enviar resposta!").
2. **Destino do pedido.** Criar a conexão de e-mail (Gmail) no X-Flows de DEV, ou outra saída, e combinar
   com cada órgão quem recebe.
3. **Protocolo.** Hoje o fluxo gera um protocolo provisório (`ART-20261027-XXXXXX`). Trocar pelo
   protocolo da API de Tramitação quando estiver disponível.
4. **Linhas de teste.** Limpar as tabelas de DEV antes da homologação com os órgãos. A do Selo Arte
   (`pedidos_selo_arte`) tem 5 envios repetidos.

### O que o estudo encontrou no X-Forms

| Achado | Pergunta ou pedido |
|---|---|
| `[FATO]` `autocomplete` `name`, `email` e `cpf` pré-preenchem com a conta. `tel` não pré-preenche. | Quais chaves existem? `celular` e `cidade` aparecem no exemplo, mas não foram testadas. |
| `[FATO]` O pré-preenchimento vale para todo campo com a chave, inclusive dados de outra pessoa. | Resolvido com `resetValueIf`. Vale registrar no manual. |
| `[FATO]` Busca de endereço pelo CEP não é possível só com o JSON. | **Pedido de demanda:** campo de CEP que preencha endereço, bairro e município. |
| `[HIPÓTESE]` `choicesByUrl` poderia carregar a lista de municípios pelo estado (serviço do IBGE). | O renderizador do portal aceita `choicesByUrl`? |
| `[FATO]` A máscara de telefone tem tamanho fixo: fixo (10 números) ou celular (11), não os dois. | Existe máscara que aceite os dois? |
| `[FATO]` CPF e CNPJ são conferidos só pelo formato, não pelo dígito verificador. | O X-Forms tem validador nativo de CPF e CNPJ? |
| `[FATO]` Ao salvar, o Designer apaga propriedades com valor padrão (`storeDataAsText`, `allowMultiple`). | Sem impacto; só registro. |
| `[FATO]` Criar formulário e enviar resposta funcionam por server actions do Next.js (`createForm`, `submitFormResponse`). O ID muda a cada versão, e chamadas seguidas dão erro 429. | Existe ou vai existir uma API documentada para importar formulários e testar envios? Facilitaria homologar em lote. |

## Pendências por órgão

Cada item é uma pergunta sobre o serviço. A resposta muda o formulário, por isso o estudo não decidiu
sozinho. O diário de cada formulário tem o detalhe.

### SETDIG

**01 — Acesso ao WordPress**
- Pedir a lista oficial de órgãos. A lista atual repete nomes (EPE, FADEB, PROCON) e inclui órgãos
  municipais (AGETRAN, SETRAT).
- Definir quem recebe o pedido.

### Fundect

**02 — Diárias e passagens**
- Estagiário tem matrícula?
- O documento com foto vale só para estagiário?

### IAGRO

**03 — Responsável técnico agrícola**
- Anexo de até 5 MB serve? Aceitar foto (JPG ou PNG) do documento?

**04 — Indústria de agrotóxicos (e-Saniagro)**
- O comprovante de CNPJ é público na Receita Federal. Pode deixar de ser pedido (Lei 14.129/2021)?
- O "Contato" da versão antiga era quem preenche ou outra pessoa da indústria?

**05 — Cancelar registro de agrotóxicos**
- Pode tirar o RG?
- Que guia de recolhimento é essa, onde se emite e qual o valor?
- Comprovante de CNPJ: mesma pergunta do 04.

**06 — Selo Arte**
- "Registro no serviço de inspeção" é o tipo de serviço (municipal, estadual ou federal)? Se for, vira
  lista de opções.
- A IAGRO é mesmo quem analisa? A versão antiga não diz.
- Qual o prazo de resposta? Há outros documentos exigidos?
- A logomarca precisa de tamanho ou resolução mínima?

**08 — Veterinário de aves ou suínos**
- Pode tirar o RG?
- Quem preenche é sempre o veterinário, ou a empresa pode cadastrar por ele?
- O número no CRMV (Conselho Regional de Medicina Veterinária) é mesmo opcional?
- O segundo telefone pode ser opcional?
- A portaria do MAPA vale para todo veterinário com vínculo ou só para quem emite GTA?
- Que documento comprova o vínculo com a empresa ou cooperativa?

**10 — Empresa integradora de aves ou suínos**
- Quem preenche é o representante legal? Se for, nome e e-mail podem vir da conta.
- Uma empresa pode ser integradora de aves e de suínos ao mesmo tempo?
- A resposta vai para o e-mail do representante ou da empresa?
- O endereço não tem rua nem número. Basta assim?
- Em que formato vem a coordenada geográfica?

**11 — Soqueira de algodão**
- Algum anexo precisa de mais de um arquivo (por exemplo, mais de um Relatório de Fiscalização)?
- Anexo de até 5 MB serve? Aceitar foto?
- Onde se emite a guia DAEMS e qual o valor de cada faixa de área?
- O pedido precisa identificar a propriedade?
- `[HIPÓTESE]` O pagamento da DAEMS pode ser conferido pelo governo, sem anexo?

**13 — Laboratório de sanidade avícola**
- O "Nome" da versão antiga era de quem preenche, do responsável técnico ou do laboratório?
- O que é o CRL?
- O endereço precisa aparecer só depois do CEP?
- O escopo das análises é mesmo opcional?

### FCMS — Fundação de Cultura de MS

**07 — Certidão negativa de tombamento**
- Pode tirar o RG do requerente e do proprietário?
- A cópia do RG e do CPF de quem pede ainda é necessária, já que a conta gov.br confirma o CPF?
- Aceitar foto (JPG ou PNG) dos documentos?
- A certidão de matrícula precisa ter sido emitida há no máximo quanto tempo?
- Qual o prazo e como a certidão é entregue?
- A versão antiga fala em "imóvel ou bem". Bem móvel entra?

**09 — Cadastro no Sistema Estadual de Bibliotecas Públicas**
- O que é o "diagnóstico mais recente das bibliotecas" e onde se responde?
- O que é biblioteca "Associada"?
- O "comprovante de funcionamento" são as fotos ou falta um anexo?
- Quem preenche é sempre o responsável pela biblioteca?
- Escolaridade pode virar lista de opções?
- Telefone fixo é comum? Hoje o campo só aceita celular.
- Qual o prazo de resposta?

### CGP — Coordenadoria-Geral de Perícias

**12 — Cópia de laudo pericial**
- Pode tirar o RG e o órgão emissor?
- "Outorgante" é quem deu a procuração?
- O documento da pessoa envolvida deve ser obrigatório para todos?
- A pessoa envolvida no fato é sempre a vítima?
- Quem conta como familiar de 1º grau? O cônjuge entra? Precisa da certidão de óbito?
- Os formatos `.webp` e `.zip` eram necessários?
- Em quanto tempo chega o e-mail com as orientações?

### SEJUSP — Secretaria de Estado de Justiça e Segurança Pública

**14 — Certidão de atendimento de emergência (190 ou 193)**
- O serviço atende só Campo Grande, Dourados, Corumbá e Ponta Porã? Se sim, o aviso vira bloqueio.
- Para achar a ligação, precisa do número de onde se ligou?
- O endereço de quem ligou é necessário?
- O documento de identificação ainda é necessário, já que o CPF vem da conta?
- "Informações adicionais" e a hora do fato podem ser opcionais?
- A finalidade pode virar lista de opções (uso pessoal, administrativo, judicial)?
- Que unidade emite a certidão e em quanto tempo?

## Próximos passos

1. Leonardo: catálogo, destino do pedido e conexão de e-mail. Sem isso nenhum serviço vai ao ar.
2. Órgãos: responder as perguntas acima. O estudo ajusta o formulário e testa de novo.
3. Estudo: testar pela tela os outros caminhos das perguntas condicionais dos formulários 06 a 14.
