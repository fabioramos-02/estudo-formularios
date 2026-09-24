# 02. Cadastrar profissional habilitado para cultivos e estabelecimentos de insumos agrícolas

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Cadastrar responsável técnico para cultivos e estabelecimentos de insumos agrícolas
- **Total de Páginas:** 1
- **Total de Campos:** 8
- **Campos Obrigatórios:** 8 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página: `página1` — *Requerimento de cadastro RT*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Informe nome completo |
| 2 | `cpf` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 3 | `email` | Email | `text` (Texto) | **Sim** | Informe seu email |
| 4 | `telefone` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 5 | `rg_cnh` | Documento de identidade - RG ou CNH | `file` (Arquivo) | **Sim** | Anexo de documento |
| 6 | `carteira_conselho` | Carteira do conselho de classe | `file` (Arquivo) | **Sim** | Anexo de carteira (CREA ou CFTA) |
| 7 | `comprovante_residencia` | Comprovante de residência | `file` (Arquivo) | **Sim** | Anexo de comprovante emitido há max. 90 dias |
| 8 | `pergunta1` | Objetivo do cadastro de RT | `checkbox` | **Sim** | Mínimo 1 e máximo 2 escolhas |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 2
- **Texto / Máscara de CPF (`text` + pattern):** 1
- **Texto / Telefone (`text` + pattern):** 1
- **Envio de Arquivo (`file`):** 3
- **Caixa de Seleção (`checkbox`):** 1


---

| Anterior | Próximo |
|---|---|
| [← WordPress — Solicitação de acesso](01-wordpress.md) | [Diárias — Fundect →](03-diarias-fundect.md) |
