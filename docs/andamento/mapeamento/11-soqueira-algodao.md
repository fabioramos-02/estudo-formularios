# 11. Requerer certificado de destruição de soqueira de algodão

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Solicitação do Certificado de Destruição de Soqueira de Algodão.
- **Total de Páginas:** 1
- **Total de Campos:** 8
- **Campos Obrigatórios:** 8
- **Campos Opcionais:** 0

---

## 📄 Distribuição por Páginas

### 1. Página 1: `pagina` — *REQUERIMENTO DE CERTIFICADO*
*Requerer certificado de destruição de soqueira de algodão*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome do responsável |
| 2 | `cpf` | CPF | `text` (Texto) | **Sim** | Número do CPF |
| 3 | `telefone` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 4 | `email` | Email | `text` (Texto) | **Sim** | E-mail do solicitante |
| 5 | `area_plantio` | Área de plantio | `checkbox` | **Sim** | Opções: <br>- Até 50 hectares (`igual_menor_50_hectares`) <br>- Acima de 50 hectares (`acima_50_hectares`) |
| 6 | `relatorio_fiscalizacao` | Relatório de Fiscalização (RF) | `file` (Arquivo) | **Sim** | Emitir no E-Saniagro (Permite múltiplos arquivos) |
| 7 | `guia_daems` | Guia da DAEMS | `file` (Arquivo) | **Sim** | Emitir DAEMS correspondente à área de plantio (Permite múltiplos arquivos) |
| 8 | `comprovante_pagamento` | Comprovante de pagamento | `file` (Arquivo) | **Sim** | Comprovante de pagamento da taxa (Permite múltiplos arquivos) |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 3
- **Texto / Máscara de Telefone (`text` + pattern):** 1
- **Caixa de Seleção (`checkbox`):** 1
- **Envio de Arquivo (`file`):** 3


---

| Anterior | Próximo |
|---|---|
| [← Empresa integradora — ave/suíno](10-empresa-integradora.md) | [Cópia de laudos periciais →](12-laudos-periciais.md) |
