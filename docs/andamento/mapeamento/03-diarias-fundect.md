# 03. Solicitação de Diárias para Servidores da Fundect

[← Mapeamento (índice)](index.md) · [Andamento](../index.md)


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


---

| Anterior | Próximo |
|---|---|
| [← Cadastro de RT — insumos agrícolas](02-rt-agricola.md) | [Indústria de agrotóxicos — e-saniagro →](04-industria-agrotoxicos.md) |
