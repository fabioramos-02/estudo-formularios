# 08. Cadastrar ou atualizar médico veterinário - avicultura ou suinocultura

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Cadastro ou atualização dos dados cadastrais de médicos veterinários que atuam no setor privado das cadeias produtivas da avicultura e da suinocultura no Estado de Mato Grosso do Sul.
- **Total de Páginas:** 2
- **Total de Campos:** 17
- **Campos Obrigatórios:** 16
- **Campos Opcionais:** 1

---

## 📄 Distribuição por Páginas

### 1. Página 1: `pagina_cadastro_medico` — *FICHA DE CADASTRO DE MÉDICOS VETERINÁRIOS – AVICULTURA/SUINOCULTURA*
*CADASTRO DE MÉDICOS VETERINÁRIOS*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome completo |
| 2 | `cpf` | CPF | `text` (Texto) | **Sim** | Número do CPF |
| 3 | `orgao_expedidor_uf` | Órgão expedidor UF | `text` (Texto) | **Sim** | Estado emissor do RG |
| 4 | `orgao_expedidor` | Órgão expedidor | `text` (Texto) | **Sim** | Órgão expedidor do RG |
| 5 | `rg` | RG | `text` (Texto) | **Sim** | Número do registro geral |
| 6 | `email` | Email | `text` (Texto) | **Sim** | E-mail de contato |
| 7 | `telefone` | Telefones de Contato | `multipletext` (Múltiplos Campos) | **Sim** | Contém 2 subcampos: <br>- `telefone_primario`: (99) 99999-9999<br>- `telefone_adicional`: (99) 99999-9999 |
| 8 | `cep` | CEP | `text` (Texto) | **Sim** | Informe o CEP |
| 9 | `endereco_completo` | Endereço completo | `text` (Texto) | **Sim** | Rua/Avenida, nº e bairro |
| 10 | `uf` | UF | `dropdown` (Seleção) | **Sim** | UF do endereço |
| 11 | `municipio` | Município | `text` (Texto) | **Sim** | Indicativo do município |
| 12 | `crmv_ms` | CRMV/MS | `text` (Texto) | **Não** | Número do CRMV |
| 13 | `empresa_vincula` | Vinculado a alguma empresa integradora ou cooperativa? | `boolean` (Sim/Não) | **Sim** | Define exibição da Página 2 (`visibleIf: {empresa_vincula} = true`) |

---

### 2. Página 2: `pagina_empresa_vinculada` — *EMPRESA INTEGRADORA OU COOPERATIVA VINCULADA*
*Página condicional (Exibida apenas se `empresa_vincula = true`)*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 14 | `cnpj_empresa` | CNPJ | `text` (Texto) | **Sim** | CNPJ da empresa integradora ou cooperativa |
| 15 | `razao_social_fantasia` | Razão social e nome fantasia | `text` (Texto) | **Sim** | Razão social e nome fantasia |
| 16 | `portaria_habitacao` | Nº Portaria de Habilitação no MAPA | `text` (Texto) | **Sim** | Informação necessária para emissão de GTA |
| 17 | `documento_empresa` | Documento da empresa, integradora ou cooperativa | `file` (Arquivo) | **Sim** | Comprovante de vínculo com a empresa |
| 18 | `documento_portaria_habitacao_mapa` | *Sem Título* (`documento_portaria_habitacao_mapa`) | `file` (Arquivo) | **Sim** | Para emissão de GTA (Permite múltiplos arquivos) |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 11
- **Múltiplos Textos / Telefones (`multipletext`):** 1 (com 2 subcampos internos)
- **Lista Suspensa (`dropdown`):** 1
- **Booleano / Sim ou Não (`boolean`):** 1
- **Envio de Arquivo (`file`):** 2


---

| Anterior | Próximo |
|---|---|
| [← Negativa de tombamento](07-negativa-tombamento.md) | [Bibliotecas públicas →](09-bibliotecas-publicas.md) |
