## Registro dos achados que se repetem.

| Item | O que foi observado | O que fazer no X-Forms | Em quantos formulários se repete |
|---|---|---|---|
| A2 | Campos mal organizados e misturados (ex.: CEP em primeiro e Cidade como penúltimo). | Organizar os campos por categorias com ordem de prioridade (ex.: Identificação → Vínculo → Pedido → Anexos → Confirmação). | Se repete em todos os formulários |
| C1 | Campo RG presente mesmo quando há CPF, tornando-se inútil devido à unificação do novo RG. | Remover o campo RG dos formulários. Incluir o campo "Órgão expedidor" apenas nos casos em que for estritamente necessário para o órgão. | Se repete em 6 formulários |
| C1 | Campos de UF / Estado / Região em serviços atendidos exclusivamente no estado de MS. | Remover esses campos ou deixá-los ocultos no corpo da resposta do formulário. | Se repete em mais de 4 formulários |
| C1 | Solicitação de coordenadas geográficas (Latitude e Longitude), que são dados de difícil acesso e compreensão para o usuário. | Remover os campos de coordenadas geográficas, priorizando os campos de endereço tradicionais (Rua, CEP) que já são obrigatórios. | Se repete em mais de 3 formulários |
| C2 | Falha no autopreenchimento do Gov.br quando o formulário possui mais de um perfil/envolvido (ex.: Colaborador e Gestor). | Configurar o autopreenchimento para múltiplos envolvidos e criar uma etapa dedicada para verificar quem está preenchendo a solicitação. | Se repete em 1 formulário |
| A1 | Formulários muito extensos (> 15 campos) concentrados em uma única página. | Eliminar campos redundantes/fúteis ou reestruturar o formulário dividindo os campos em múltiplas páginas/etapas. | Se repete em mais de 8 formulários |
| C3 | Campos duplicados e espalhados para o mesmo tipo de dado (ex.: 2 telefones, endereço fragmentado em 3 partes). | Unificar em um único campo múltiplo (para telefones) ou texto único (para endereço), agrupando os dados para evitar confusão. | Se repete em mais de 4 formulários |
| C9 | Campos interligados sem lógica de dependência ativa (ex.: Setor ↔ Órgão, Endereço ↔ CEP). | Posicionar os campos correlacionados lado a lado/abaixo e implementar lógica relacional (ex.: `visibleIf`) entre campo pai e filho. | Se repete em mais de 8 formulários |
| C5 | Falta de máscara de formatação e validação em campos de formato fixo (ex.: CPF). | Aplicar máscaras de preenchimento e validação de quantidade exata de dígitos (ex.: 11 dígitos no CPF) para impedir envio com erros. | Se repete em todos os formulários |
| C4 | Uso de campos de texto livre para dados padronizados (ex.: Estados, Cor/Raça). | Substituir campos de texto aberto por listas suspensas (dropdown) com opções fechadas para evitar digitação incorreta. | Se repete em mais de 6 formulários |

Detalhe e justificativa sobre a coluna Item e seus dados em [docs/04-checklist.md](docs/04-checklist.md#a-organizacao).