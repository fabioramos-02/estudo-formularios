# 04. Cadastrar indústria produtos agrotóxicos no e-saniagro

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Cadastrar indústria produtos agrotóxicos no e-saniagro
- **Total de Páginas:** 1
- **Total de Campos:** 13
- **Campos Obrigatórios:** 13 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *Requerimento para cadastro da indústria de produtos agrotóxicos no e-saniagro*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `representante_legal` | Representante legal | `text` (Texto) | **Sim** | Nome do representante legal |
| 2 | `cnpj` | CNPJ | `text` (Texto) | **Sim** | Informe o CNPJ |
| 3 | `razao_social` | Razão Social | `text` (Texto) | **Sim** | Razão social da empresa |
| 4 | `contato` | Contato | `text` (Texto) | **Sim** | Nome do contato da empresa |
| 5 | `telefone_contato` | Telefone do Contato | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 6 | `cep` | CEP | `text` (Texto) | **Sim** | Máscara `99999-999` |
| 7 | `endereco_correspondencia` | Endereço da correspondência | `text` (Texto) | **Sim** | Endereço de correspondência |
| 8 | `estado` | Estado | `dropdown` (Seleção) | **Sim** | Sigla do Estado |
| 9 | `cidade` | Cidade | `text` (Texto) | **Sim** | Cidade da correspondência |
| 10 | `bairro` | Bairro | `text` (Texto) | **Sim** | Bairro |
| 11 | `cnpj_anexo` | CNPJ | `file` (Arquivo) | **Sim** | Cópia do CNPJ da empresa |
| 12 | `contrato_social` | Contrato social | `file` (Arquivo) | **Sim** | Contrato social atualizado |
| 13 | `procuracao_remetente` | Procuração do remetente | `file` (Arquivo) | **Sim** | Procuração específica do representante |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 7
- **Texto / Telefone (`text` + pattern):** 1
- **Texto / CEP (`text` + pattern):** 1
- **Lista Suspensa (`dropdown`):** 1
- **Envio de Arquivo (`file`):** 3


---

| Anterior | Próximo |
|---|---|
| [← Diárias — Fundect](03-diarias-fundect.md) | [Cancelar registro — agrotóxicos →](05-cancelar-agrotoxicos.md) |
