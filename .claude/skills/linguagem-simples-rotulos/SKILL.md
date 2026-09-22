---
name: linguagem-simples-rotulos
description: Reescreve rótulos (`title`), textos de ajuda (`description`), placeholders e mensagens de erro dos campos de um JSON X-Forms conforme Lei 15.263/2025 e Decreto Estadual 16.744/2026 (linguagem simples). Aplica verbo direto, remove jargão jurídico, expande sigla na primeira ocorrência, limita ≤10 palavras por rótulo. Chama o agente `linguagem-simples-revisor` para pontuar. Dispara em "linguagem simples nos campos", "reescrever rótulos", "melhorar textos do formulário", ou quando `/melhorar-formulario` chama.
---

# linguagem-simples-rotulos

Entrega: JSON X-Forms com `title`, `description`, `placeholder` e mensagens de erro reescritos + diff markdown.

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

### Placeholder
- **Só** quando um exemplo real ajuda. Não repetir o rótulo.
- Ex.: rótulo "E-mail", placeholder `nome@dominio.gov.br`.

### Mensagens de erro
Padrão: **como corrigir**, não só "inválido".
- CPF: "Digite um CPF válido, com 11 números."
- E-mail: "Digite um e-mail no formato nome@dominio."
- Obrigatório: "Preencha este campo para continuar."

### Botão de envio
Texto = ação: "Enviar solicitação" > "OK" (checklist B5).

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
