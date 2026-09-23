# Recomendações que foram utiliaas no SETDIG - Solicitação de Acesso Wordpress mas poderam ser utilizadas em outros formulários, como os que estão em andamento.

**na primeira etapa, estão sendo pedido os dados dos getores mas como o gestor que fará a solicitação, acho que dados como cpf, nome completo, rg, orgao expedidor e telefone podem ser retirados do gov, seguindo o principio da [FATO] Lei nº 13.709/2018 - Lei Geral de Proteção de Dados (LGPD) sobre minimização (art. 6º III), onde o governo, neste caso o govbr, já possui esses dados.**


**[RECOMENDAÇÃO] o campo (Setor/Unidade Gestora) poderia estar ligado com o campo (Secretaria / Órgãos). Para que quando um valor for selecionado no campo (Setor/Unidade Gestora) o campo (Secretaria / Órgãos) fica se vizivel.**


**[RECOMENDAÇÃO] o campo rg realmemte será necesário, por que com a nova carteira de identidade que utiliza o cpf como numero do resgistro geral, acho que o campo cpf já será suficiente.**


**[INTERPRETAÇÃO] os campos estão mal distribuidos como por exemplo o campo (Secretaria / Órgãos) é o primeiro campo enquanto o (Setor/Unidade Gestora) é o penultimo, [RECOMENDAÇÃO] para mim os campos com dados pessoias deveriao ser colocados como primeiros, e os dados sobre o trabalho logo em seguida.**


# Cancelar o registro de estabelecimento comercial e prestador de serviço de agrotóxico

**[RECOMENDAÇÃO] o campo UF realmente será necessário, por que o campo munícipio já está preenchido com as cidades do MS, onde o usuario só pode selecionar elas.**

**[RECOMENDAÇÃO] logicas que não estão no X-Forms, comparar campos entre si, por exemplo (cidade_origem != cidade_destino). E para o campo data/saída ou data/retorno, eles teriam que ser maior que o dia atual da solicitação mas não tem como selecionar o dia dinamicamente**


# Obter Selo ARTE

**[RECOMENDAÇÃO] o campo produtos deverá ser multiplo para o usuario poder adicionar todos os seus produtos a serem vendidos**


# Cadastrar ou atualizar médico veterinário - avicultura ou suinocultura

**[RECOMENDAÇÃO] Foi feito a junção dos campo Telefone e Telefone Adicional para apenas um campo Telefone Contato onde esse campo é Texto múltiplo, onde Telefone está como Telefone Principal e Telefone Adicional está como Telefone Adicional, os dois estão como obrigatórios**


# Cadastro no Sistema Estadual de Bibliotecas Públicas

**[RECOMENDAÇÃO] campos que acho desnecessário ter (Descreva sua biblioteca em uma frase) e (Coordenadas Geográficas).**

**[INTERPRETAÇÃO] o campo Horário de funcionamento deveria ser obrigatório? por que uma biblioteca que não está em funcionamento, não possui horário de funcionamento.**

**[INTERPRETAÇÃO] o campo Região não faz sentido no formulario porque o que adiante ter esse campo, se a resposta sempre será Centro-Oeste, por que o serviço será só para biblioteca do estado do Mato Grosso do Sul, e no campo municipio só pode ser selecionado cidades do MS, portanto afirmando que o serviço será pro estado MS.**

**[RECOMENDAÇÃO]  primeira etapa onde serão caastrados os dados sobre a biblioteca erá dividido em duas etapas para que um formulário não fiquei muito grande, na minha opnião será divido em (Cadastro de Dados da Biblioteca) em seguida (Informações adicionais e anexos de arquivos) mas terei que ver se poderá ser divido de outra maneira, já que o preenchimento dos dados da biblioteca ocupam 23 campo, contando que o campo (Coordenadas Geográficas) e (Regiões) foram removidos**