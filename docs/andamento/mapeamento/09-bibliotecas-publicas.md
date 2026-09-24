# 09. Cadastro no Sistema Estadual de Bibliotecas Públicas

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


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


---

| Anterior | Próximo |
|---|---|
| [← Veterinário — avicultura/suinocultura](08-veterinario-avi-suino.md) | [Empresa integradora — ave/suíno →](10-empresa-integradora.md) |
