# Data

Podemos dividir os tipos de datas de tal maneira:

* datas de documentos ou cartões, como um passaporte ou cartão de crédito
* datas aproximadas, como ‘Dezembro de 2017’
* datas relativas, como ‘4 dias a partir de hoje’

## Para pedir datas de documentos ou cartões:

Ao solicitar esses dados, deverão ser passados na forma como estiver no documento, podendo ter um exemplo no campo que o usuário irá colocar a informação, ou podendo ser na descrição. Por exemplo na CNH deverá ter um exemplo `22/12/2012`, ou em cartões `27/32`.

## Pedindo datas aproximadas:

Para datas que os usuários podem não saber ou ter dificuldade para lembrar. Por exemplo, permitir que o usuário insira a data `'01/25'` para um campo que diz "a data em que você ingressou na empresa".

## Padrões que são usados mas por causa das ferramentas do X-forms não serão utilizados:

Datas memoráveis, como data de nascimento ou casamento. No *gov.uk*, para esse tipo de data, eles dividem o dia, mês e ano em 3 campos, mas acredito que no X-Form é mais prático o campo do tipo data, em que o usuário poderá clicar no ícone de calendário, podendo assim ter uma visão mais ampla dos dias.

---

# E-mail

## Diga aos usuários por que você deseja o endereço de e-mail

Deixe claro para que será utilizado o endereço de e-mail para que:

* usuários se sintam confiantes de que você não vai abusar disso
* usuários com vários endereços de e-mail possam escolher qual deles lhe dar

> **Nota:** Se o campo de endereço de e-mail fizer parte de uma caixa de login, você não precisa dizer *‘Precisamos do seu e-mail para que possamos entrar em você’*.

## Ajudar os usuários a inserir um endereço de e-mail válido

Verifique se inseriram corretamente utilizando a ferramenta de validação, usando a lógica se contém no campo e-mail por exemplo `@gmail.com`. Se esse campo não conter esses caracteres alinhados, irá dar erro e o usuário não conseguirá dar continuidade ao formulário.

### Se o endereço de e-mail não estiver no formato correto e não houver exemplo

Diga: *‘Insira um endereço de e-mail no formato correto, como o nome@example.com’*.

Definindo o tipo `'email'` para o campo e-mail, já se valida o formato do e-mail.

Você também deve definir o atributo `autocomplete` para `email`. Isso permite que os navegadores preencham automaticamente o endereço de e-mail em nome de um usuário se ele já o tiver inserido anteriormente.

O campo deve ser amplo o suficiente para que a maioria dos usuários veja todo o seu endereço de e-mail depois de inseri-lo. Uma boa regra é garantir que você possa ver pelo menos 30 caracteres de uma só vez. Você pode analisar seus dados de usuário para refinar isso.

---

# Nome

## Quando usar esse padrão

Você deve seguir esse padrão sempre que precisar pedir o nome de um usuário como parte do seu serviço.  
*Só peça os nomes das pessoas se você precisar dessas informações para entregar um serviço.*

## Campos de nome único ou múltiplo

Um único campo de nome pode acomodar a gama mais ampla de tipos de nome, mas significa que você não pode extrair de forma confiável partes de um nome. Mas acredito que não será necessária a separação do nome para o sobrenome.

## Campos de nome de rotulagem

Campos de nome único de etiqueta:
* «Nome completo»

Para vários campos de nome, use:
* «Primeiro nome»
* «Último nome»

Use o atributo `autocomplete` no componente de entrada de texto quando você estiver pedindo o nome de um usuário. Isso permite que os navegadores preencham automaticamente as informações em nome de um usuário se ele já as tiver inserido anteriormente.

## Não faça o cheque ortográfico nos nomes do usuário

Às vezes, os navegadores verificam as informações que um usuário insere em uma entrada de texto. Para garantir que os nomes do usuário não sejam verificados por ortografia, defina o atributo `spellcheck` para `false` como mostrado neste exemplo.

---

# Telefone

## Use o atributo autocomplete

Use o atributo `autocomplete` em entradas de número de telefone. Isso permite que os navegadores preencham automaticamente as informações em nome de um usuário se ele já as tiver inserido anteriormente.

### Se o número de telefone não estiver no formato correto e não houver exemplo

Diga: *‘Insira um número de telefone, como 67 99217-2147’, +55 67 99217-2147’, 67 92172147*,.*.