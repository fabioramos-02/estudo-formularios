# 07. Solicitação da Negativa de Tombamento

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Formulário de Solicitação da Certidão Negativa de Tombamento, documento oficial que atesta que determinado imóvel ou bem não está protegido por tombamento em nível municipal, estadual ou federal.
- **Total de Páginas:** 1
- **Total de Campos:** 10
- **Campos Obrigatórios:** 10 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *Formulário de Solicitação da Certidão Negativa de Tombamento*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome do Requerente | `text` (Texto) | **Sim** | Nome do Requerente |
| 2 | `cpf_requerente` | CPF do Requerente | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 3 | `rg_requerente` | RG do Requerente | `text` (Texto) | **Sim** | RG do Requerente |
| 4 | `cpf_proprietario` | CPF do Proprietário | `text` (Texto) | **Sim** | CPF do Proprietário |
| 5 | `rg_proprietario` | RG do Proprietário | `text` (Texto) | **Sim** | RG do Proprietário |
| 6 | `identificacao_imovel` | Identificação do imóvel | `text` (Texto) | **Sim** | Nome e localização do imóvel |
| 7 | `procuracao` | Procuração | `file` (Arquivo) | **Sim** | Anexo de procuração (Assinada por Gov.br ou certificado digital) |
| 8 | `certidao_matricula_atualizada_imovel` | Certidão de matrícula atualizada do imóvel | `file` (Arquivo) | **Sim** | Certidão de matrícula atualizada em PDF |
| 9 | `rg_cpf_proprietario` | RG e CPF do Proprietário | `file` (Arquivo) | **Sim** | Anexo dos documentos do proprietário (Permite múltiplos arquivos) |
| 10 | `rg_cpf_requerente` | RG e CPF do Requerente | `file` (Arquivo) | **Sim** | Anexo dos documentos do requerente (Permite múltiplos arquivos) |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 5
- **Texto / Máscara de CPF (`text` + pattern):** 1
- **Envio de Arquivo (`file`):** 4


---

| Anterior | Próximo |
|---|---|
| [← Selo Arte](06-selo-arte.md) | [Veterinário — avicultura/suinocultura →](08-veterinario-avi-suino.md) |
