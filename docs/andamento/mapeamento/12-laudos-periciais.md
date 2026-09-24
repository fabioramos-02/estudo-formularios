# 12. Solicitar cópia de laudos periciais

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Descrição:** Serviço para solicitação de cópias de laudos periciais emitidos pela CGP/SEJUSP/MS para fins judiciais, seguros ou outras finalidades oficiais.
- **Total de Páginas:** 3
- **Total de Campos:** 22
- **Campos Obrigatórios:** 13
- **Campos Opcionais:** 9

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *Dados do Solicitante da cópia de laudos periciais*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome_solicitante` | Nome | `text` (Texto) | **Sim** | Nome completo do solicitante |
| 2 | `cpf_solicitante` | CPF | `text` (Texto) | **Sim** | CPF do solicitante |
| 3 | `rg` | RG | `text` (Texto) | **Sim** | Registro Geral do solicitante |
| 4 | `orgao_emissor` | Órgão emissor | `text` (Texto) | **Sim** | Órgão emissor do RG |
| 5 | `telefone_solicitante` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 6 | `email_solicitante` | E-mail | `text` (Texto) | **Sim** | E-mail do solicitante |
| 7 | `endereco_solicitante` | Endereço | `text` (Texto) | **Sim** | Endereço completo (Rua, nº, bairro, município e CEP) |
| 8 | `data_nascimento` | Data de nascimento | `text` (Data) | **Sim** | Formato de data (`inputType: "date"`) |
| 9 | `tipo_solicitante` | Tipo de solicitante | `checkbox` | **Sim** | Escolha única: <br>- Pessoa envolvida no evento<br>- Procurador devidamente constituído<br>- Familiar de 1º grau de vítima fatal |

---

### 2. Página 2: `página2` — *Dados sobre a vítima do evento*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 10 | `nome_vitima` | Nome da vítima | `text` (Texto) | **Sim** | Nome da vítima envolvida no evento |
| 11 | `nome_outorgante` | Nome do outorgante | `text` (Texto) | **Não** | Se for procurador, insira o nome completo do procurador |
| 12 | `copia_procuracao` | Anexar cópia da procuração (se aplicável) | `file` (Arquivo) | **Não** | Suporta: `.pdf`, `.png`, `.jpg`, `.webp`, `.zip`, `.jpeg` (Múltiplos) |
| 13 | `documento_identificacao_pessoa_envolvida` | Documento de identificação da pessoa envolvida no evento | `file` (Arquivo) | **Não** | Suporta: `.pdf`, `.png`, `.jpg`, `.webp`, `.zip`, `.jpeg` (Múltiplos) |
| 14 | `documento_identificacao_pessoal_solicitante` | Documento de Identificação pessoal do solicitante (familiares de 1º grau) ou Procurador (se aplicável) | `file` (Arquivo) | **Não** | Suporta: `.pdf`, `.png`, `.jpg`, `.webp`, `.zip`, `.jpeg` (Múltiplos) |
| 15 | `documento_comprove_relacao_parentesco` | Documento que comprove a relação de parentesco com a vítima fatal (se aplicável) | `file` (Arquivo) | **Não** | Suporta: `.pdf`, `.png`, `.jpg`, `.webp`, `.zip`, `.jpeg` (Múltiplos) |

---

### 3. Página 3: `página3` — *Dados sobre o inquérito ou boletim de ocorrência*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 16 | `numero_inquerito_boletim` | Número do inquérito/boletim de ocorrência policial ou processo penal | `text` (Texto) | **Não** | Número do B.O. ou processo penal |
| 17 | `endereco_evento` | Local de ocorrência do fato | `text` (Texto) | **Não** | Endereço completo do fato (Rua, Bairro, Cidade, CEP, complemento) |
| 18 | `descricao_fato` | Descrição do fato | `text` (Texto) | **Sim** | Descrição detalhada do ocorrido |
| 19 | `data_fato` | Data do fato | `text` (Data) | **Sim** | Formato de data (`inputType: "date"`) |
| 20 | `tipo_laudo` | Informe o tipo do laudo pericial solicitado | `checkbox` | **Não** | Mínimo 1 seleção: <br>- Análise Laboratoriais<br>- Criminalística<br>- Identificação<br>- Medicina-Legal |
| 21 | `informacoes_adicionais` | Informações adicionais | `text` (Texto) | **Não** | Texto livre para observações |
| 22 | `termo` | Condições para fornecimento da cópia do laudo pericial | `checkbox` | **Sim** | Aceite dos termos referentes a segredo de justiça e taxa DAEMS de 0,5 UFERMS/folha |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 11
- **Texto / Máscara de Telefone (`text` + pattern):** 1
- **Texto / Seleção de Data (`text` + date):** 2
- **Caixa de Seleção (`checkbox`):** 3
- **Envio de Arquivo (`file`):** 4


---

| Anterior | Próximo |
|---|---|
| [← Destruição de soqueira de algodão](11-soqueira-algodao.md) | [Laboratório — sanidade avícola →](13-laboratorio-avicola.md) |
