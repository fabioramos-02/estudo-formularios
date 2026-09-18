# 4. Checklist de avaliação

A régua usada para avaliar cada formulário. Toda pergunta é feita do ponto de vista de **quem
preenche**, e a resposta é **sim**, **não** ou **não se aplica**.

Não existe nota nem ranking. Cada **não** vira um item da lista de melhorias para a reconstrução no
X-Forms.

!!! tip "Como usar"
    Copie os blocos abaixo para dentro da ficha do formulário
    (`docs/fichas/_template.md` já traz uma cópia pronta) e marque enquanto navega.
    Quando marcar **não**, escreva uma linha dizendo o que viu.

---

## A. Organização

- [ ] **A1.** Os campos estão em uma coluna só?
- [ ] **A2.** Campos do mesmo assunto estão agrupados?
- [ ] **A3.** A ordem faz sentido para quem preenche (e não para quem processa)?
- [ ] **A4.** Se tem várias etapas, dá para saber em qual você está?
- [ ] **A5.** Dá para voltar e corrigir uma etapa anterior sem perder o que já preencheu?
- [ ] **A6.** O tamanho da caixa sugere o tamanho da resposta esperada?
- [ ] **A7.** Funciona no celular sem zoom e sem rolagem lateral?

## B. Linguagem

- [ ] **B1.** Dá para entender cada rótulo sem consultar a norma do serviço?
- [ ] **B2.** As siglas estão explicadas na primeira vez que aparecem?
- [ ] **B3.** Onde a dúvida é previsível, existe texto de ajuda?
- [ ] **B4.** Está claro o que é obrigatório e o que é opcional?
- [ ] **B5.** O texto do botão diz o que vai acontecer ("Enviar solicitação", não "OK")?
- [ ] **B6.** O formulário explica o que acontece depois do envio (prazo, protocolo, resposta)?

## C. Campos e dados

- [ ] **C1.** Todo campo pedido é realmente necessário para este serviço?
- [ ] **C2.** O formulário deixa de pedir dado que o governo já tem ou que o login já forneceu?
- [ ] **C3.** O mesmo dado não é pedido duas vezes no mesmo fluxo?
- [ ] **C4.** O tipo de campo é o certo (data é campo de data, município é seleção, não texto livre)?
- [ ] **C5.** Há máscara onde o formato importa (CPF, CNPJ, CEP, telefone, data)?
- [ ] **C6.** A validação aceita as variações legítimas (nome com acento, CEP com e sem hífen)?
- [ ] **C7.** O nome técnico do campo segue o padrão e bate com o usado em outros serviços?
- [ ] **C8.** O anexo informa formato, tamanho máximo e quantidade aceita?

## D. Erro e acessibilidade

- [ ] **D1.** Cada campo tem rótulo visível e associado a ele?
- [ ] **D2.** A mensagem de erro diz **como corrigir**, não só que está errado?
- [ ] **D3.** O erro aparece junto do campo (e, em formulário longo, também resumido no topo)?
- [ ] **D4.** O que já foi preenchido se mantém depois do erro?
- [ ] **D5.** Dá para percorrer o formulário inteiro só com o teclado, na ordem certa?
- [ ] **D6.** O foco fica visível ao navegar por teclado?
- [ ] **D7.** A informação não depende só de cor (campo com erro não é só vermelho)?

---

## Registro do resultado

Para cada **não**, anote na ficha:

| Item | O que foi observado | O que fazer no X-Forms |
|---|---|---|
| ex.: C2 | Pede nome e CPF mesmo já estando logado pelo gov.br | Preencher automaticamente a partir do login |

---

!!! note "Este checklist não está fechado"
    Ele nasceu do que já se sabia antes da pesquisa. Depois de preencher as páginas
    [1](01-diagramacao.md), [2](02-aprendizados.md) e [3](03-nomenclatura.md), revise esta lista
    com o Fabio: item que a pesquisa não sustenta sai, item que ela revelou entra.
