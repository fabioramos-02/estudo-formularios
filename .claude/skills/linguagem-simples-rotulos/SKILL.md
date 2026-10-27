---
name: linguagem-simples-rotulos
description: Reescreve rótulos (`title`), textos de ajuda (`description`), placeholders e mensagens de erro dos campos de um JSON X-Forms conforme Lei 15.263/2025 e Decreto Estadual 16.744/2026 (linguagem simples). Aplica verbo direto, remove jargão jurídico, expande sigla na primeira ocorrência, limita ≤10 palavras por rótulo. Chama o agente `linguagem-simples-revisor` para pontuar. Dispara em "linguagem simples nos campos", "reescrever rótulos", "melhorar textos do formulário", ou quando `/melhorar-formulario` chama.
---

# linguagem-simples-rotulos

Entrega: JSON X-Forms com `title`, `description`, `tooltip`, `placeholder` e mensagens de erro reescritos + diff markdown.
Exemplo do X-Forms atual: `.claude/referencia/xforms-precadastro-familiar.json`.

## Base legal

- Lei 15.263/2025 (Federal, linguagem simples).
- Decreto Estadual MS 16.744/2026.
- WCAG 2.2 critérios 3.3.x.

## Regras

### Rótulo (`title`)
1. **Verbo direto** se pede ação: "Digite seu CPF" > "CPF" quando o exemplo ajuda; caso comum, rótulo curto substantivo: "CPF".
2. **Palavra que o cidadão usa** > termo da norma. "Cidade" > "Município do domicílio".
3. **≤10 palavras.**
4. **Sigla:** expandir na primeira ocorrência: "CPF (Cadastro de Pessoa Física)". Nas próximas: só "CPF".
5. **Sem jargão jurídico** salvo obrigatório por norma — nesse caso, adicionar `description` explicando.
6. **Sem redundância** de bloco: se a página é "Dados do gestor", não repetir "do gestor" em todo campo. `title` = "Nome completo" (não "Nome completo do gestor").

### Texto de ajuda (`description`)
- Usar quando a dúvida é previsível (checklist B3).
- Frase curta explicando **o que preencher**, não o motivo.
- Ex.: campo `matricula` → description "O número que aparece no seu contracheque."

### Dica no ícone (`tooltip`)
O X-Forms mostra o `tooltip` num ícone ao lado da pergunta: a pessoa só vê se clicar.
- **`description` (visível):** o que a pessoa **precisa** para responder certo. Formato, o que entra e
  o que não entra, se é opcional. Ex.: "Some salário, pensão e aposentadoria. Não inclua o Bolsa
  Família."
- **`tooltip` (escondido):** o que **ajuda**, mas não muda a resposta. Por que pedimos, de onde veio o
  dado, um exemplo a mais. Ex.: "Para onde enviaremos o número do protocolo."
- Na dúvida, `description`. Âncora: GOV.UK hint text fica sempre visível (`[RECOMENDAÇÃO]`, B3 e D1).
- Mesmas regras de escrita da `description`: frase curta, sem jargão.

### Placeholder
- **Só** quando um exemplo real ajuda. Não repetir o rótulo.
- Ex.: rótulo "E-mail", placeholder `nome@dominio.gov.br`.

### Mensagens de erro
Ficam em `validators[].text`. Padrão: **como corrigir**, não só "inválido".
- CPF: "Digite um CPF válido, com 11 números."
- E-mail: "Digite um e-mail no formato nome@dominio."
- Obrigatório: "Preencha este campo para continuar."

### Botão de envio
Texto = ação: "Enviar solicitação" > "OK" (checklist B5).

### Outros textos que o cidadão lê
- `choices[].text`, `labelTrue`/`labelFalse` (Sim/Não), `addRowText` e `removeRowText` da lista de
  pessoas, `title` das colunas de `matrixdynamic`.
- `html` (avisos na tela). A última página diz o que acontece depois: protocolo, prazo, quem
  responde (B6). `completedHtml` não aparece no portal: mover o texto para a última página.
- `description` do formulário e das páginas.

## Fluxo

1. Ler JSON.
2. Para cada campo, aplicar as regras acima.
3. **Opcional:** chamar subagent `linguagem-simples-revisor` para pontuar o conjunto de rótulos e sugerir ajustes.
4. Escrever JSON de saída.
5. Emitir diff markdown.

## Saída

```md
## Linguagem simples

| Campo | Antes | Depois | Regra |
|---|---|---|---|
| `cpf_gestor` | "CPF do Gestor" | "CPF" | sem redundância — página já diz "Dados do gestor" |
| `secretaria_orgao_gestor` | "Secretaria / Órgão" | "Órgão onde trabalha" | palavra do cidadão |
| erro CPF | "" | "Digite um CPF válido, com 11 números." | mensagem de erro objetiva |
```

## Uso

Chamado direto ou por `melhorar-formulario`. Roda **depois** de `regras-diagramacao` (assume estrutura final).

## Fora de escopo

- Não altera `name`, tipo, máscara ou ordem — só textos apresentados ao cidadão.

## Como o Antonio edita esta skill

Quando um formulário auditado mostrar um jargão que se repete e ainda não está aqui:
1. Acrescentar linha em "Palavra que o cidadão usa > termo da norma" com o par (jargão → palavra simples).
2. Se for uma mensagem de erro recorrente (CEP inválido, data no futuro), acrescentar no bloco "Mensagens de erro (padrão)".
3. Refletir descobertas em `docs/02-aprendizados.md` seção B.
