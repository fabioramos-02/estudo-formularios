# 10. Cadastrar ou atualizar empresa integradora de ave ou suíno

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Serviço para cadastrar ou atualizar os dados de empresas integradoras da cadeia de avicultura e suinocultura em Mato Grosso do Sul.
- **Total de Páginas:** 2
- **Total de Campos:** 16
- **Campos Obrigatórios:** 10
- **Campos Opcionais:** 6

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *Dados do Representante legal*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome_representante` | Nome | `text` (Texto) | **Sim** | Representante legal |
| 2 | `telefone_representante` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 3 | `email_representante` | E-mail | `text` (Texto) | **Sim** | E-mail do representante legal |

---

### 2. Página 2: `página2` — *FICHA DE CADASTRO DE EMPRESAS INTEGRADORAS DE AVES E SUÍNOS*
*FICHA DE CADASTRO DE EMPRESAS INTEGRADORAS DE AVES E SUÍNOS*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 4 | `nome_fantasia` | Nome fantasia | `text` (Texto) | **Sim** | Nome fantasia da empresa |
| 5 | `razao_social` | Razão social | `text` (Texto) | **Sim** | Conforme cartão CNPJ |
| 6 | `cnpj` | CNPJ | `text` (Texto) | **Sim** | Número do CNPJ |
| 7 | `inscricao_estadual` | Inscrição Estadual | `text` (Texto) | **Sim** | Número da IE |
| 8 | `telefone_empresa` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 9 | `email_empresa` | E-mail | `text` (Texto) | **Sim** | E-mail da integradora |
| 10 | `uf_empresa` | UF | `dropdown` (Seleção) | **Não** | UF do estado |
| 11 | `municipio_empresa` | Município | `text` (Texto) | **Sim** | Nome do município |
| 12 | `cep` | CEP | `text` (Texto) | **Sim** | Número do CEP |
| 13 | `via_acesso` | Via de acesso | `text` (Texto) | **Não** | Ponto de referência |
| 14 | `coordenada_geografica` | Coordenada geográfica | `text` (Texto) | **Não** | Formato em graus decimais (Ex.: `S: -20.00000 -50.00000`) |
| 15 | `integradora` | Integradora de: | `checkbox` | **Não** | Escolha única (Avicultura ou Suinocultura) |
| 16 | `informacoes_complementares` | Informações complementares | `text` (Texto) | **Não** | Outras informações importantes |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 13
- **Texto / Máscara de Telefone (`text` + pattern):** 2
- **Lista Suspensa (`dropdown`):** 1
- **Caixa de Seleção (`checkbox`):** 1


---

| Anterior | Próximo |
|---|---|
| [← Bibliotecas públicas](09-bibliotecas-publicas.md) | [Destruição de soqueira de algodão →](11-soqueira-algodao.md) |
