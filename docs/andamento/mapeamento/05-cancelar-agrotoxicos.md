# 05. Cancelar o registro de estabelecimento comercial e prestador de serviço de agrotóxico

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Serviço para solicitar o encerramento oficial do registro de empresas que atuam com agrotóxicos (fabricação, comércio, transporte, armazenamento ou prestação de serviços).
- **Total de Páginas:** 1
- **Total de Campos:** 14
- **Campos Obrigatórios:** 14 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *TERMO DE COMPROMISSO*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome do responsável pela empresa |
| 2 | `cpf` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 3 | `uf_orgao` | UF | `dropdown` (Seleção) | **Sim** | UF do Órgão Expedidor |
| 4 | `orgao_expedidor` | Órgão Expedidor | `text` (Texto) | **Sim** | Órgão Expedidor do RG |
| 5 | `rg` | RG | `text` (Texto) | **Sim** | RG do responsável da empresa |
| 6 | `nome_empresa` | Nome da empresa | `text` (Texto) | **Sim** | Nome da empresa |
| 7 | `cnpj` | CNPJ | `text` (Texto) | **Sim** | CNPJ da empresa |
| 8 | `inscricao_estadual` | Inscrição Estadual | `text` (Texto) | **Sim** | Inscrição Estadual da empresa |
| 9 | `uf` | UF | `dropdown` (Seleção) | **Sim** | UF do endereço/empresa |
| 10 | `municipio` | Município | `text` (Texto) | **Sim** | Município |
| 11 | `endereco` | Endereço | `text` (Texto) | **Sim** | Endereço da empresa |
| 12 | `motivo` | Motivo | `dropdown` (Seleção) | **Sim** | Motivo do cancelamento (4 opções) |
| 13 | `copia_cnpj` | Cópia do CNPJ | `file` (Arquivo) | **Sim** | Anexo da cópia do CNPJ |
| 14 | `guia_recolhimento` | Guia de recolhimento | `file` (Arquivo) | **Sim** | Anexo da guia de recolhimento |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 8
- **Texto / Máscara de CPF (`text` + pattern):** 1
- **Lista Suspensa (`dropdown`):** 3
- **Envio de Arquivo (`file`):** 2


---

| Anterior | Próximo |
|---|---|
| [← Indústria de agrotóxicos — e-saniagro](04-industria-agrotoxicos.md) | [Selo Arte →](06-selo-arte.md) |
