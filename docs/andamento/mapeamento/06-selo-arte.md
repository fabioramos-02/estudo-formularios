# 06. Obter selo arte

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Requerimento de solicitação do Selo Arte conforme legislação vigente para produtos alimentícios de origem animal produzidos de forma artesanal.
- **Total de Páginas:** 1
- **Total de Campos:** 9
- **Campos Obrigatórios:** 9 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *REQUERIMENTO DE SOLICITAÇÃO DE SELO ARTE*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome do requerente |
| 2 | `cpf` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 3 | `nome_estabelecimento` | Nome do estabelecimento | `text` (Texto) | **Sim** | Nome do estabelecimento produtor |
| 4 | `registro_servico_inspecao` | Registro no serviço de inspeção | `text` (Texto) | **Sim** | Registro no serviço de inspeção |
| 5 | `numero_registro` | Número | `text` (Texto) | **Sim** | Número do registro |
| 6 | `municipio` | Múnicipio | `dropdown` (Seleção) | **Sim** | Seleção de município |
| 7 | `endereco` | Endereço | `text` (Texto) | **Sim** | Endereço completo |
| 8 | `produtos` | Produtos | `text` (Texto) | **Sim** | Descrição dos produtos |
| 9 | `identidade_visual_industria` | Identidade visual da indústria | `file` (Arquivo) | **Sim** | Anexo da logomarca |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 6
- **Texto / Máscara de CPF (`text` + pattern):** 1
- **Lista Suspensa (`dropdown`):** 1
- **Envio de Arquivo (`file`):** 1


---

| Anterior | Próximo |
|---|---|
| [← Cancelar registro — agrotóxicos](05-cancelar-agrotoxicos.md) | [Negativa de tombamento →](07-negativa-tombamento.md) |
