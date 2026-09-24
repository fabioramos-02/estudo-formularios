# 13. Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Serviço para cadastrar ou atualizar os dados de laboratórios que realizam análises de sanidade avícola para os programas oficiais de monitoramento sanitário.
- **Total de Páginas:** 1
- **Total de Campos:** 14
- **Campos Obrigatórios:** 11
- **Campos Opcionais:** 3

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *FICHA DE CADASTRO DE LABORATÓRIO DE DIAGNÓSTICO EM SANIDADE AVÍCOLA*
*DADOS PARA CADASTRO DO LABORATÓRIO*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome |
| 2 | `escopo_aves` | Escopo - Aves (Salmonela/Micoplasma) | `text` (Texto) | **Não** | Tipo de testes ou outro escopo |
| 3 | `nome_fantasia` | Nome fantasia | `text` (Texto) | **Sim** | Nome fantasia do laboratório |
| 4 | `razao_social` | Razão social | `text` (Texto) | **Sim** | Conforme cartão CNPJ |
| 5 | `cnpj` | CNPJ | `text` (Texto) | **Sim** | Número do CNPJ |
| 6 | `inscricao_estadual` | Inscrição Estadual | `text` (Texto) | **Sim** | Número da IE |
| 7 | `portaria_credenciamento` | Nº Portaria de Credenciamento | `text` (Texto) | **Não** | Para laboratórios credenciados junto ao MAPA |
| 8 | `crl` | Nº do CRL | `text` (Texto) | **Não** | Preencher se houver |
| 9 | `telefone` | Telefone | `text` (Texto) | **Sim** | Telefone do laboratório |
| 10 | `email` | E-mail | `text` (Texto) | **Sim** | E-mail do laboratório |
| 11 | `cep` | CEP | `text` (Texto) | **Sim** | Máscara `99999-999` |
| 12 | `enredeco_completo` | Endereço completo | `text` (Texto) | **Sim** | Exibida apenas se `cep` for preenchido (Rua/Avenida, nº e bairro) |
| 13 | `uf` | UF | `dropdown` (Seleção) | **Sim** | Exibida apenas se `cep` for preenchido (Seleção das 27 UFs) |
| 14 | `municipio` | Município | `text` (Texto) | **Sim** | Exibida apenas se `cep` for preenchido |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples / Formatado (`text`):** 13
- **Lista Suspensa (`dropdown`):** 1


---

| Anterior | Próximo |
|---|---|
| [← Cópia de laudos periciais](12-laudos-periciais.md) | [Certidão de atendimento 190/193 →](14-certidao-190-193.md) |
