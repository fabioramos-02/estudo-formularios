# 01. SETDIG — Solicitação de Acesso ao WordPress

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


## 📊 Resumo Geral
- **Total de Páginas:** 5
- **Total de Campos:** 28
- **Campos Obrigatórios:** 28 (100% dos campos)

---

## 📄 Distribuição por Páginas

### 1. Página: `perfil` — *Quem está solicitando*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `perfil_solicitante` | Quem está preenchendo este formulário? | `imagepicker` | **Sim** | Seleção por imagem (gestor / colaborador) |

---

### 2. Página: `site` — *Sobre o site*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 2 | `nome_site` | Nome do site | `text` (Texto) | **Sim** | - |
| 3 | `url_site` | Endereço do site | `text` (URL) | **Sim** | Formato de URL (`https://...`) |
| 4 | `permissao_acesso` | Tipo de permissão de acesso | `checkbox` | **Sim** | Permite selecionar 1 opção |

---

### 3. Página: `dados_gestor` — *Dados do gestor do setor*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 5 | `nome_gestor` | Nome completo | `text` (Texto) | **Sim** | Autocomplete `name` |
| 6 | `cpf_gestor` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 7 | `telefone_gestor` | Celular | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 8 | `email_gestor` | E-mail institucional | `text` (E-mail) | **Sim** | Validador de formato de e-mail |
| 9 | `matricula_gestor` | Matrícula | `text` (Texto) | **Sim** | - |
| 10 | `cargo_gestor` | Cargo | `text` (Texto) | **Sim** | - |
| 11 | `orgao_gestor` | Órgão onde trabalha | `dropdown` | **Sim** | Seleção de lista |
| 12 | `setor_gestor` | Setor ou unidade | `text` (Texto) | **Sim** | Visível se `orgao_gestor` preenchido |
| 13 | `municipio_gestor` | Município | `dropdown` | **Sim** | Seleção de lista |

---

### 4. Página: `dados_colaborador` — *Dados do colaborador que vai usar o acesso*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 14 | `nome_colaborador` | Nome completo | `text` (Texto) | **Sim** | Autocomplete `name` |
| 15 | `cpf_colaborador` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 16 | `telefone_colaborador` | Celular | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 17 | `email_colaborador` | E-mail institucional | `text` (E-mail) | **Sim** | Validador de formato de e-mail |
| 18 | `matricula_colaborador` | Matrícula | `text` (Texto) | **Sim** | - |
| 19 | `cargo_colaborador` | Cargo | `text` (Texto) | **Sim** | - |
| 20 | `login_rede_colaborador` | Login de rede | `text` (Texto) | **Sim** | Login de domínio/rede |
| 21 | `orgao_colaborador` | Órgão onde trabalha | `dropdown` | **Sim** | Seleção de lista |
| 22 | `setor_colaborador` | Setor ou unidade | `text` (Texto) | **Sim** | Visível se `orgao_colaborador` preenchido |
| 23 | `municipio_colaborador` | Município | `dropdown` | **Sim** | Seleção de lista |

---

### 5. Página: `dados_responsavel` — *Dados do responsável pelo site*
| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 24 | `nome_responsavel` | Nome completo | `text` (Texto) | **Sim** | Autocomplete `name` |
| 25 | `cpf_responsavel` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 26 | `telefone_responsavel` | Celular | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 27 | `email_responsavel` | E-mail institucional | `text` (E-mail) | **Sim** | Validador de formato de e-mail |
| 28 | `matricula_responsavel` | Matrícula | `text` (Texto) | **Sim** | - |
| 29 | `cargo_responsavel` | Cargo | `text` (Texto) | **Sim** | - |
| 30 | `orgao_responsavel` | Órgão onde trabalha | `dropdown` | **Sim** | Seleção de lista |
| 31 | `setor_responsavel` | Setor ou unidade | `text` (Texto) | **Sim** | Visível se `orgao_responsavel` preenchido |
| 32 | `municipio_responsavel` | Município | `dropdown` | **Sim** | Seleção de lista |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 13
- **Texto / Máscara de CPF (`text` + pattern):** 3
- **Texto / Telefone (`text` + tel):** 3
- **Texto / E-mail (`text` + email):** 3
- **Texto / URL (`text` + url):** 1
- **Lista Suspensa (`dropdown`):** 6
- **Caixa de Seleção (`checkbox`):** 1
- **Seletor de Imagem (`imagepicker`):** 1


---

| Anterior | Próximo |
|---|---|
| &nbsp; | [Cadastro de RT — insumos agrícolas →](02-rt-agricola.md) |
