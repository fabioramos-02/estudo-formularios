# 3. Padrão de nomenclatura dos campos

> **Status:** esqueleto — a preencher (Antonio)
> **Pergunta desta página:** como nomear os campos de um formulário?

Leia antes o [Guia do Antonio](guia-do-antonio.md). Use os marcadores `[FATO]`, `[INTERPRETAÇÃO]` e
`[RECOMENDAÇÃO]` e registre cada fonte em [fontes.md](fontes.md).

---

## 3.1. Duas coisas diferentes: rótulo e nome técnico

| | O que é | Quem lê | Exemplo |
|---|---|---|---|
| **Rótulo** | Texto exibido ao lado do campo | O cidadão | `CPF` |
| **Nome técnico** | Chave do campo nos dados enviados ao Integrador | Sistemas | `cpf` |

O FormFlow formata os dados coletados e envia ao Integrador em JSON. O **nome técnico** é o que
viaja nesse JSON. Se cada serviço batizar o mesmo dado de um jeito, nada se cruza depois.

*(desenvolver: por que a separação importa, o que quebra quando ela não existe)*

## 3.2. Convenção do nome técnico

*Qual formato adotar (`snake_case` minúsculo, sem acento, sem espaço)? Abreviar ou escrever por
extenso? Prefixo por seção? Como nomear campo que se repete (endereço de várias unidades, por
exemplo)? Como nomear anexo?*

*(a preencher)*

## 3.3. Como escrever o rótulo

*Palavra que o cidadão usa ou termo da norma? Quando usar texto de ajuda em vez de rótulo longo?
Como tratar sigla?*

*(a preencher)*

## 3.4. Consistência entre serviços

*Como garantir que "CPF" seja sempre `cpf`? Quem mantém a lista? O que fazer quando um serviço
precisa de uma variação?*

*(a preencher)*

## 3.5. Dicionário de campos canônicos

Os campos que aparecem em quase todo formulário. **Preencher com o que a pesquisa indicar e com o
que for observado nos 14 formulários auditados.**

| Nome técnico | Rótulo recomendado | Tipo | Máscara | Validação |
|---|---|---|---|---|
| `cpf` | CPF | texto | `000.000.000-00` | dígito verificador |
| `cnpj` | CNPJ | texto | `00.000.000/0000-00` | dígito verificador |
| `nome_completo` | Nome completo | texto | — | *(a preencher)* |
| `email` | E-mail | e-mail | — | *(a preencher)* |
| `telefone_celular` | Celular | texto | `(00) 00000-0000` | *(a preencher)* |
| `data_nascimento` | Data de nascimento | data | `dd/mm/aaaa` | *(a preencher)* |
| `cep` | CEP | texto | `00000-000` | *(a preencher)* |
| `logradouro` | Endereço | texto | — | *(a preencher)* |
| `numero` | Número | texto | — | *(a preencher)* |
| `complemento` | Complemento | texto | — | opcional |
| `bairro` | Bairro | texto | — | *(a preencher)* |
| `municipio` | Município | seleção | — | *(a preencher)* |
| `uf` | UF | seleção | — | *(a preencher)* |

*Acrescentar linhas conforme aparecerem nos formulários auditados.*

---

## Resumo — o padrão proposto

*(preencher no fim: as regras de nomenclatura que o X-Forms deve seguir)*
