# Mapeamento do Formulário: SETDIG — Solicitação de Acesso ao WordPress

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

--- --- ---

# Mapeamento do Formulário: Cadastrar profissional habilitado para cultivos e estabelecimentos de insumos agrícolas

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

--- --- ---

# Mapeamento do Formulário: Solicitação de Diárias para Servidores da Fundect

## 📊 Resumo Geral
- **Descrição:** Serviço para solicitação online e acompanhamento de diárias de viagens oficiais da Fundect, permitindo o envio eletrónico de pedidos e documentos comprovativos.
- **Total de Páginas:** 3
- **Total de Campos:** 15
- **Campos Obrigatórios:** 12
- **Campos Opcionais:** 3

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *Dados do Servidor e da Viagem*
*Informe os dados do servidor que vai viajar e os dados de sua viagem*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Informe seu nome |
| 2 | `matricula` | Matricula | `text` (Texto) | **Sim** | Informe sua matrícula |
| 3 | `solicitacao` | Tipo de Solicitação | `checkbox` | **Sim** | Mínimo 1 e máximo 1 escolha |

---

### 2. Página 2: `página2` — *Roteiro da Viagem*
*Preencha as informações do roteiro da viagem*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 4 | `cidade_origem` | Cidade de Origem | `text` (Texto) | **Sim** | Informe a cidade de origem |
| 5 | `cidade_destino` | Cidade de Destino | `text` (Texto) | **Sim** | Informe a cidade de destino |
| 6 | `data_saida` | Data/Saída | `text` (Data) | **Sim** | Validador do tipo `expression` |
| 7 | `data_retorno` | Data/Retorno | `text` (Data) | **Sim** | Informe a data de retorno |
| 8 | `objetivo_viagem` | Objetivo da Viagem | `comment` (Texto Longo) | **Sim** | Informe o objetivo da viagem |
| 9 | `veiculo_utilizado` | Veículo utilizado | `comment` (Texto Longo) | **Não** | Oculto por padrão (`visible: false`) |
| 10 | `documento_pessoal` | Documento pessoal com foto | `file` (Arquivo) | **Não** | Cópia do documento em PDF |

---

### 3. Página 3: `página3` — *Dados Bancários e Pessoais*
*Dados obrigatórios para estagiário. Servidores não precisam preencher, pois seus dados já constam no sistema de Recursos Humanos.*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 11 | `cpf` | CPF | `text` (Texto) | **Sim** | Máscara `999.999.999-99` |
| 12 | `rg` | RG | `text` (Texto) | **Não** | Informe o número do RG |
| 13 | `banco` | Banco | `text` (Texto) | **Sim** | Informe o código ou nome do banco |
| 14 | `agencia` | *Sem Título* (`agencia`) | `text` (Texto) | **Sim** | Agência com dígito |
| 15 | `conta_corrente` | Conta Corrente | `text` (Texto) | **Sim** | Número da conta |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 8
- **Texto / Máscara de CPF (`text` + pattern):** 1
- **Texto Multilinha / Comentário (`comment`):** 2
- **Caixa de Seleção (`checkbox`):** 1
- **Envio de Arquivo (`file`):** 1

--- --- ---

# Mapeamento do Formulário: Cadastrar indústria produtos agrotóxicos no e-saniagro

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

--- --- ---

# Mapeamento do Formulário: Cancelar o registro de estabelecimento comercial e prestador de serviço de agrotóxico

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

-- -- --

# Mapeamento do Formulário: Obter selo arte

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

--- --- ---

# Mapeamento do Formulário: Solicitação da Negativa de Tombamento

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

--- --- ---

# Mapeamento do Formulário: Cadastrar ou atualizar médico veterinário - avicultura ou suinocultura

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

--- --- ---

# Mapeamento do Formulário: Cadastro no Sistema Estadual de Bibliotecas Públicas

## 📊 Resumo Geral
- **Descrição:** Cadastro oficial de bibliotecas públicas e comunitárias de Mato Grosso do Sul junto à Fundação de Cultura de Mato Grosso do Sul (FCMS), que garante reconhecimento institucional e acesso a formações, recursos, acervos, equipamentos e parcerias.
- **Total de Páginas:** 3
- **Total de Campos:** 31
- **Campos Obrigatórios:** 22
- **Campos Opcionais:** 9

---

## 📄 Distribuição por Páginas

### 1. Página 1: `pagina_dados_biblioteca` — *Cadastro de Dados da Biblioteca*
*Manter os dados atualizados anualmente ou sempre que houver alteração na gestão, endereço ou estrutura.*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome_responsavel_biblioteca` | Nome do responsável pela biblioteca | `text` (Texto) | **Sim** | Nome do responsável |
| 2 | `cargo_responsavel_biblioteca` | Cargo do Responsável pela biblioteca | `text` (Texto) | **Sim** | Cargo do responsável |
| 3 | `escolaridade_responsavel_biblioteca` | Escolaridade do responsável pela biblioteca | `text` (Texto) | **Sim** | Escolaridade do responsável |
| 4 | `nome_biblioteca` | Nome da biblioteca | `text` (Texto) | **Sim** | Nome da biblioteca |
| 5 | `diagnostico_mais_recente_biblioteca` | Respondeu ao diagnóstico mais recente das bibliotecas? | `boolean` (Sim/Não) | **Sim** | Confirmação de resposta |
| 6 | `esta_funcionamento` | Está em funcionamento ? | `checkbox` | **Sim** | Escolha única (Sim/Não) |
| 7 | `tipo_cadastrada` | Tipo de biblioteca a ser cadastrada | `checkbox` | **Sim** | Escolha única (Pública/Comunitária/Associada) |
| 8 | `legislacao_criacao` | Legislação de Criação | `text` (Texto) | **Sim** | Exibida apenas se `tipo_cadastrada = 'publica'` |
| 9 | `numero_pessoas_bibliotecas` | Número de pessoas que trabalham na biblioteca | `text` (Número) | **Sim** | Mínimo 0, numérico |
| 10 | `nome_completo_pessoas_trabalham_biblioteca` | Nome completo das pessoas que trabalham na biblioteca | `comment` (Texto Longo) | **Não** | Exibida apenas se `numero_pessoas_bibliotecas` for preenchido |
| 11 | `descreva_biblioteca_frase` | Descreva sua biblioteca em uma frase | `text` (Texto) | **Sim** | Frase descritiva |
| 12 | `historia_biblioteca` | Conte a história da biblioteca | `comment` (Texto Longo) | **Sim** | História da biblioteca |
| 13 | `horario_funcionamento` | Horário de funcionamento | `comment` (Texto Longo) | **Sim** | Exibida apenas se `esta_funcionamento = 'sim'` |
| 14 | `informacoes_adicionais_horario_funcionamento` | Informações adicionais sobre o horário de funcionamento | `text` (Texto) | **Não** | Informações adicionais |
| 15 | `endereco_biblioteca` | Endereço da Biblioteca | `text` (Texto) | **Sim** | CEP, Logradouro, Número, Complemento, Bairro |
| 16 | `municipio` | Município | `dropdown` (Seleção) | **Sim** | Seleção de município |
| 17 | `facilidade_pessoas_deficiencia` | Possui alguma facilidade para pessoas com deficiência ou mobilidade reduzida? | `boolean` (Sim/Não) | **Não** | Acessibilidade |
| 18 | `facilidade_acessibilidade_oferece` | Quais facilidades de acessibilidade a biblioteca oferece | `text` (Texto) | **Não** | Exibida apenas se `facilidade_pessoas_deficiencia = true` |

---

### 2. Página 2: `pagina_anexos` — *Informações adicionais e anexos de arquivos*
*Anexar documento de criação da biblioteca (decreto, lei ou ato administrativo, no caso de bibliotecas públicas). Enviar comprovante de funcionamento (fotos atuais do espaço, horário de atendimento e endereço completo).*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 19 | `rede_sociais` | Contato e Redes Sociais da Biblioteca | `text` (Texto) | **Não** | E-mail, Telefone, Redes Sociais |
| 20 | `legislacao_arquivo` | Legislação | `file` (Arquivo) | **Sim** | Exibida apenas se `tipo_cadastrada = 'publica'` |
| 21 | `foto_capa` | Foto de capa | `file` (Arquivo) | **Não** | Foto da fachada ou entrada (JPEG) |
| 22 | `foto_divulgacao` | Foto de divulgação | `file` (Arquivo) | **Não** | Imagem de divulgação (JPEG) |
| 23 | `documentacao_cadastro_anteriores` | Documentação de Cadastros anteriores | `file` (Arquivo) | **Não** | Comprovantes de cadastros anteriores (PDF/JPEG, Múltiplos) |

---

### 3. Página 3: `pagina_instituicao` — *Dados sobre a Instituição ligada a biblioteca*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 24 | `nome_responsavel_instituicao` | Nome do Responsável | `text` (Texto) | **Sim** | Nome do responsável pela instituição |
| 25 | `cargo_reponsavel_instituicao` | Cargo do responsável | `text` (Texto) | **Sim** | Cargo do responsável |
| 26 | `telefone_instituicao` | Telefone da Instituição | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 27 | `email_instituicao` | E-mail da Instituição | `text` (Texto) | **Sim** | E-mail da instituição |
| 28 | `nome_instiucao_vinculada` | Nome da instituição à qual a biblioteca está vinculada | `text` (Texto) | **Sim** | Nome da instituição vinculada |
| 29 | `tipo_documento_instituicao` | Tipo de documento da instituição | `checkbox` | **Sim** | Opções: CNPJ ou CPF |
| 30 | `numero_documento_vinculado_biblioteca` | Número do documento vinculado à biblioteca | `text` (Texto) | **Sim** | Número do CNPJ ou CPF |
| 31 | `endereco_intituicao` | Endereço da Instituição | `text` (Texto) | **Sim** | Endereço completo da instituição |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 16
- **Texto / Máscara de Telefone (`text` + pattern):** 1
- **Texto Multilinha / Comentário (`comment`):** 3
- **Booleano / Sim ou Não (`boolean`):** 2
- **Caixa de Seleção (`checkbox`):** 3
- **Lista Suspensa (`dropdown`):** 1
- **Envio de Arquivo (`file`):** 5

--- --- ---

# Mapeamento do Formulário: Cadastrar ou atualizar empresa integradora de ave ou suíno

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

--- --- ---

# Mapeamento do Formulário: Requerer certificado de destruição de soqueira de algodão

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

--- --- ---

# Mapeamento do Formulário: Solicitar cópia de laudos periciais

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

--- --- ---

# Mapeamento do Formulário: Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola

## 📊 Resumo Geral
- **Descrição:** Serviço para cadastrar ou atualizar os dados de laboratórios que realizam análises de sanidade avícola para os programas oficiais de monitoramento sanitário.
- **Total de Páginas:** 1
- **Total de Campos:** 14
- **Campos Obrigatórios:** 11
- **Campos Opcionais:** 3

---

## 📄 Distribuição por Páginas

### 1. Página 1: `página1` — *FICHA DE CADASTRO DE LABORATÓRIO DE DIAGNÓSTICO EM SANIDADE AVÍCOLA*
*DADOS PARA CADASTRO DO LABORATÓRIO*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome` | Nome | `text` (Texto) | **Sim** | Nome |
| 2 | `escopo_aves` | Escopo - Aves (Salmonela/Micoplasma) | `text` (Texto) | **Não** | Tipo de testes ou outro escopo |
| 3 | `nome_fantasia` | Nome fantasia | `text` (Texto) | **Sim** | Nome fantasia do laboratório |
| 4 | `razao_social` | Razão social | `text` (Texto) | **Sim** | Conforme cartão CNPJ |
| 5 | `cnpj` | CNPJ | `text` (Texto) | **Sim** | Número do CNPJ |
| 6 | `inscricao_estadual` | Inscrição Estadual | `text` (Texto) | **Sim** | Número da IE |
| 7 | `portaria_credenciamento` | Nº Portaria de Credenciamento | `text` (Texto) | **Não** | Para laboratórios credenciados junto ao MAPA |
| 8 | `crl` | Nº do CRL | `text` (Texto) | **Não** | Preencher se houver |
| 9 | `telefone` | Telefone | `text` (Texto) | **Sim** | Telefone do laboratório |
| 10 | `email` | E-mail | `text` (Texto) | **Sim** | E-mail do laboratório |
| 11 | `cep` | CEP | `text` (Texto) | **Sim** | Máscara `99999-999` |
| 12 | `enredeco_completo` | Endereço completo | `text` (Texto) | **Sim** | Exibida apenas se `cep` for preenchido (Rua/Avenida, nº e bairro) |
| 13 | `uf` | UF | `dropdown` (Seleção) | **Sim** | Exibida apenas se `cep` for preenchido (Seleção das 27 UFs) |
| 14 | `municipio` | Município | `text` (Texto) | **Sim** | Exibida apenas se `cep` for preenchido |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples / Formatado (`text`):** 13
- **Lista Suspensa (`dropdown`):** 1

--- --- ---

# Mapeamento do Formulário: Solicitar emissão de certidão de atendimento de emergência

## 📊 Resumo Geral
- **Descrição:** Serviço para solicitação de certidão oficial que comprove chamadas feitas ao 190 (Polícia Militar) ou 193 (Bombeiros) nas cidades de Campo Grande, Dourados, Corumbá e Ponta Porã, para uso pessoal, administrativo ou judicial.
- **Total de Páginas:** 2
- **Total de Campos:** 18
- **Campos Obrigatórios:** 13
- **Campos Opcionais:** 5

---

## 📄 Distribuição por Páginas

### 1. Página 1: `pagina_ligou` — *Dados de quem ligou*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 1 | `nome_completo_ligou` | Nome completo | `text` (Texto) | **Sim** | Informe seu nome completo |
| 2 | `cpf_ligou` | CPF | `text` (Texto) | **Sim** | Informe seu CPF |
| 3 | `data_nascimento_ligou` | Data de nascimento | `text` (Data) | **Sim** | Formato de data (`inputType: "date"`) |
| 4 | `telefone_ligou` | Telefone | `text` (Telefone) | **Sim** | Máscara `(99) 99999-9999` |
| 5 | `email_ligou` | E-mail | `text` (Texto) | **Sim** | E-mail válido do solicitante |
| 6 | `endereco_ligou` | Endereço completo | `text` (Texto) | **Sim** | Bairro, Rua/Avenida, Número |
| 7 | `complemento_endereco_ligou` | Complemento endereço | `text` (Texto) | **Não** | Ex.: casa, apartamento, ponto de referência |
| 8 | `cidade_ligou` | Cidade | `dropdown` (Seleção) | **Não** | Seleção dentre os 79 municípios do MS |
| 9 | `documento_identificacao_cpf` | Documento de identificação e CPF | `file` (Arquivo) | **Sim** | RG ou CNH contendo CPF (Formato PDF / Múltiplos) |
| 10 | `documento_identificacao_representante` | Documento de identificação do representante legal ou procurador | `file` (Arquivo) | **Não** | Anexar se aplicável (Formato PDF / Múltiplos) |
| 11 | `procuracao_ligou` | Procuração | `file` (Arquivo) | **Não** | Procuração se houver (Formato PDF / Múltiplos) |
| 12 | `outros_documentos` | Outros documentos | `file` (Arquivo) | **Não** | Documentos complementares (Formato PDF / Múltiplos) |

---

### 2. Página 2: `pagina_ocorrencia` — *Dados da Ocorrência*
*Informe os dados da Ocorrência.*

| # | Campo (`name`) | Rótulo / Título | Tipo | Obrigatório | Observações / Validação |
|---|---|---|---|---|---|
| 13 | `telefone_origem_emergencia` | Telefone de origem das chamadas de emergência | `checkbox` | **Sim** | Escolha única: <br>- `190` <br>- `193` |
| 14 | `cidade_ocorrencia` | Cidade | `dropdown` (Seleção) | **Não** | Cidade onde o fato ocorreu (79 municípios do MS) |
| 15 | `endereco_ocorrencia` | Endereço completo da ocorrência | `text` (Texto) | **Sim** | Bairro, Rua/Avenida, Número (ou "Sem número") |
| 16 | `data_horario_fato` | Data e horário do fato | `text` (Data e Hora) | **Sim** | Formato data/hora (`inputType: "datetime-local"`) |
| 17 | `finalidade_registro` | Finalidade do registro de atendimento | `text` (Texto) | **Sim** | Motivo do pedido (Ex.: Questões judiciais) |
| 18 | `descricao_ocorrencia` | Descrição da ocorrência | `comment` (Texto Longo) | **Sim** | Relato breve sobre o ocorrido |
| 19 | `informacoes_adicionais` | Informações adicionais | `comment` (Texto Longo) | **Sim** | Informações relevantes adicionais |

---

## 📈 Contagem Por Tipo de Campo
- **Texto Simples (`text`):** 5
- **Texto / Máscara de Telefone (`text` + pattern):** 1
- **Texto / Seleção de Data (`text` + date):** 1
- **Texto / Seleção de Data e Hora (`text` + datetime-local):** 1
- **Área de Texto / Texto Longo (`comment`):** 2
- **Lista Suspensa (`dropdown`):** 2
- **Caixa de Seleção (`checkbox`):** 1
- **Envio de Arquivo (`file`):** 4

--- --- ---