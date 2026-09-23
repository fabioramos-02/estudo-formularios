# SETDIG — Solicitação de Acesso ao WordPress

**Origem:** `C:\Users\framos\Downloads\solicitacao-de-acesso-wordpress.json`
**Data:** 2026-09-22
**Skills aplicadas:** `auditoria-metricas` → `nomenclatura-campos` → `regras-diagramacao` → `linguagem-simples-rotulos` → `auditoria-metricas`

**Âncoras:**
- GOV.UK Design System — Form structure (https://www.gov.uk/service-manual/design/form-structure)
- gov.br — Padrão Digital de Governo
- `docs/04-checklist.md` seção A/B/C/D

---

## Métricas — snapshot inicial

| Métrica | Valor |
|---|---|
| Páginas | 7 |
| Campos | 51 |
| Obrigatórios | 50 |
| Condicionais (`visibleIf`) | 4 |
| Tipos | text (39), dropdown (10), checkbox (1), imagepicker (1) |
| Uploads | 0 |

### Campos por página (entrada)

| Página | Campos | Alerta |
|---|---|---|
| pagina_seleciona_usuario | 1 | ok |
| pagina_permissao | 3 | ok |
| pagina_gestor1 | 9 | ⚠ >8 |
| pagina_colaborador_1 | 10 | ⚠ >8 |
| pagina_colaborador_2 | 10 | ⚠ >8 + duplicação |
| pagina_gestor_2 | 9 | ⚠ >8 + duplicação |
| pagina_responsavel | 9 | ⚠ >8 |

### Achados

- **[FATO]** Duplicação estrutural: `pagina_gestor1` ≡ `pagina_gestor_2`; `pagina_colaborador_1` ≡ `pagina_colaborador_2`. Objetivo original: inverter ordem conforme escolha inicial (gestor ou colaborador). O X-Forms não suporta reordenar páginas dinamicamente, então a plataforma foi contornada com blocos duplicados — 19 campos redundantes.
- **[RECOMENDAÇÃO]** Total 51 > 40. Rever necessidade de cada campo (checklist C1).
- **[RECOMENDAÇÃO]** Campos herdáveis do gov.br: `cpf_*`, `nome_*`, `email_*`, `telefone_*`. Considerar pré-preenchimento a partir do login (Lei 14.129/2021 art. 5º I; LGPD art. 6º III — minimização).

---

## Nomenclatura

Dicionário canônico aplicado (fonte: `docs/03-nomenclatura.md` §3.5).

| Antes | Depois | Motivo |
|---|---|---|
| `usuario_selecionado` | `perfil_solicitante` | `[RECOMENDAÇÃO]` clareza — descreve o que a escolha significa |
| `secretaria_orgao_gestor` | `orgao_gestor` | dicionário: `orgao` |
| `secretaria_orgao_colaborador` | `orgao_colaborador` | idem |
| `secretaria_orgao_responsavel` | `orgao_responsavel` | idem |
| `setor_unidade_gestora_gestor` | `setor_gestor` | dicionário: `setor` |
| `setor_unidade_gestora_colaborador` | `setor_colaborador` | idem |
| `setor_unidade_gestora_responsavel` | `setor_responsavel` | idem |
| `cidade_gestor` | `municipio_gestor` | dicionário: `municipio` |
| `cidade_colaborador` | `municipio_colaborador` | idem |
| `cidade_responsavel` | `municipio_responsavel` | idem |
| `login_colaborador` | `login_rede_colaborador` | dicionário: `login_rede` |
| `nome_gestor2`, `cpf_gestor2`, ... | eliminados como `name` distinto — reaproveitam `nome_gestor` na página duplicada | mesma pessoa, mesmo `name`; duas páginas o exibem sob `visibleIf` |
| `nome_colaborador2`, `cpf_colaborador2`, ... | eliminados como `name` distinto — reaproveitam `nome_colaborador` na página duplicada | idem |
| `email_gestor` (imagepicker `Image 3`/`Image 4`) | valores `gestor`/`colaborador` | valores legíveis no e-mail e no fluxo |

### Valores do imagepicker
- `Image 3` → `gestor` (texto exibido: "Sou gestor do setor")
- `Image 4` → `colaborador` (texto exibido: "Sou colaborador")

**[RECOMENDAÇÃO]** Considerar remoção do campo `rg` (não presente no formulário atual, mas comum no padrão). A nova identidade nacional usa CPF como número de registro geral — CPF é suficiente. Fonte: `docs/andamento/recomendacoes.md`.

---

## Diagramação

### Estrutura antes → depois

| | Antes | Depois |
|---|---|---|
| Páginas totais no JSON | 7 | 7 |
| Páginas exibidas ao mesmo cidadão | 7 (todas) | **5** (as outras 2 ficam ocultas por `visibleIf`) |
| Campos totais (`name` únicos) | 51 | **32** |
| Elementos declarados no JSON | 51 | 51 (duas cópias de gestor e duas de colab, cada dupla mutuamente exclusiva) |

### Mudanças

1. **[FATO] Ordem das páginas segue a escolha inicial.** No X-Forms não dá pra reordenar páginas em tempo real, então declaramos as duas ordens e usamos `visibleIf` por página para exibir só a correta:
   - Se `perfil_solicitante = 'gestor'` → aparece `gestor_primeiro` depois `colaborador_depois`.
   - Se `perfil_solicitante = 'colaborador'` → aparece `colaborador_primeiro` depois `gestor_depois`.
   - As páginas duplicadas **compartilham os mesmos `name` de campo** (`nome_gestor`, `cpf_gestor` etc.). Como apenas uma dupla é visível por vez, o cidadão preenche cada campo uma única vez.
   - `[HIPÓTESE]` X-Forms grava o valor no `name` mesmo entre páginas duplicadas ocultas — validar na plataforma. Se der conflito, fallback: sufixo `_alt` na 2ª cópia + coalescer no fluxo Activepieces.

2. **[RECOMENDAÇÃO GOV.UK — one thing per page]** Página `perfil` isolada com única pergunta (imagepicker). Decisão que muda o fluxo → página própria.

3. **[RECOMENDAÇÃO checklist A3]** Ordem canônica **dentro** de cada bloco de pessoa:
   - Identificação (nome, cpf, telefone, e-mail)
   - Vínculo (matrícula, cargo, [login de rede — só colab], órgão, setor, município)
   - `orgao` **imediatamente antes** de `setor` — antes o `setor` era *penúltimo* campo. Agora estão encostados, e `setor` só aparece após `orgao` ser preenchido (`visibleIf`).

4. **[RECOMENDAÇÃO checklist A3]** Ordem canônica **das páginas** vista pelo cidadão:
   1. Escolha (`perfil`)
   2. Detalhe do pedido (`site` — nome, URL, permissão)
   3. Bloco "eu" (gestor ou colaborador, conforme escolha)
   4. Bloco "o outro" (colaborador ou gestor)
   5. Responsável pelo site (sempre)
   - `[FATO]` Original abria com "Sites e Permissões" duas vezes (páginas 1 e 2) — inconsistência de título corrigida.

5. **[FATO] Dependência explícita:** `setor_*` tem `visibleIf: {orgao_*} notempty` — o campo só aparece após o órgão ser selecionado (checklist A3 + fluxo cognitivo).

### Estrutura final

| Ordem visual | Página | Condição | Campos |
|---|---|---|---|
| 1 | `perfil` | sempre | 1 |
| 2 | `site` | sempre | 3 |
| 3 | `gestor_primeiro` | `perfil = 'gestor'` | 9 |
| 4 | `colaborador_depois` | `perfil = 'gestor'` | 10 |
| 3 | `colaborador_primeiro` | `perfil = 'colaborador'` | 10 |
| 4 | `gestor_depois` | `perfil = 'colaborador'` | 9 |
| 5 | `dados_responsavel` | sempre | 9 |

Cidadão sempre vê **5 páginas**. Nunca as 7 juntas.

---

## Linguagem simples

Base legal: **Lei 15.263/2025** (Federal), **Decreto Estadual MS 16.744/2026**.

| Campo | Antes | Depois | Regra |
|---|---|---|---|
| `perfil_solicitante` | "Quem está preenchendo este formulário" | "Quem está preenchendo este formulário?" | pergunta direta |
| `nome_gestor` | "Nome do Gestor" | "Nome completo" | sem redundância — página já diz "Dados do gestor" |
| `cpf_gestor` | "CPF do Gestor" | "CPF" + description "Cadastro de Pessoa Física." | expansão de sigla na 1ª ocorrência |
| `telefone_gestor` | "Telefone do Gestor" | "Celular" | palavra do cidadão |
| `email_gestor` | "email do Gestor" | "E-mail institucional" | precisão + capitalização correta |
| `matricula_gestor` | "Matrícula do Gestor" | "Matrícula" + description "O número que aparece no seu contracheque." | dúvida previsível (checklist B3) |
| `orgao_gestor` | "Secretaria / Órgão" | "Órgão onde trabalha" | palavra do cidadão |
| `setor_gestor` | "Setor/Unidade Gestora" | "Setor ou unidade" | remoção de barra + termo simples |
| `municipio_gestor` | "Cidade" | "Município" | dicionário canônico + padrão IBGE |
| `login_rede_colaborador` | "Login de Rede do Colaborador" | "Login de rede" + description "O login que você usa para entrar no computador do trabalho." | dúvida previsível |
| `url_site` | "URL do SITE" | "Endereço do site" + placeholder `https://exemplo.ms.gov.br` | palavra do cidadão + exemplo |
| `nome_site` | "Nome do SITE" | "Nome do site" | capitalização |

### Mensagens de erro (padrão)

Antes: `"requiredErrorText": "Campo obrigatório"` (todos iguais).
Depois: mensagem específica **como corrigir** (checklist D2).

| Campo | Mensagem |
|---|---|
| CPF | "Digite um CPF válido, com 11 números." |
| E-mail | "Digite um e-mail no formato nome@dominio." |
| Celular | "Digite um celular com DDD." |
| URL | "Digite o endereço completo, começando com https://" |
| Obrigatório genérico | "Preencha [este campo] para continuar." |

---

## Métricas — snapshot final

| Métrica | Antes | Depois | Δ |
|---|---|---|---|
| Páginas exibidas ao cidadão | 7 | 5 | −2 |
| Campos preenchidos pelo cidadão (`name` únicos) | 51 | 32 | −19 |
| Duplicações de dado no preenchimento | 19 | 0 | −19 |
| Páginas declaradas no JSON | 7 | 7 | 0 (2 delas mutuamente exclusivas) |
| Mensagens de erro específicas | 0 | 32 | +32 |
| Campos com `description` (ajuda) | 0 | 3 | +3 |
| `orgao` antes de `setor` em todos blocos | não | sim | ✓ |
| Sigla expandida na 1ª ocorrência | não | sim | ✓ |
| Ordem responde à escolha do perfil | sim (via duplicação) | sim (via `visibleIf`, sem duplicar preenchimento) | ✓ |

---

## Limitações do X-Forms observadas

- **[FATO]** Reordenação dinâmica de páginas por escolha do usuário não suportada. Contornado declarando as duas ordens no JSON, cada página com `visibleIf` no `perfil_solicitante`, e reaproveitando os mesmos `name` de campo nas duplicatas para que o cidadão preencha o dado uma única vez.
- **[HIPÓTESE]** X-Forms respeita `name` compartilhado entre páginas exclusivas por `visibleIf`. Validar na plataforma. Fallback: sufixo `_alt` na 2ª cópia + coalescer no fluxo.
- **[FATO]** Validação cruzada entre campos (ex.: "se `orgao_gestor` = AGEMS, `email_gestor` deve terminar em `@segov.ms.gov.br`") não é expressável na configuração declarativa. Não aplicada em `saida.json`.
- **[FATO]** Máscara de CPF/telefone não persiste no webhook — dígitos chegam sem formatação. O fluxo Activepieces é o local certo pra formatar antes de enviar por e-mail/PDF.
- **[FATO]** Tooltip não suportado. Ajuda vai em `description` (visível permanente).
- **[FATO]** Multivalorado (múltiplos itens do mesmo tipo) só via `matrix` / `paneldynamic` — não usado aqui.

---

## Próximos passos

1. Importar `saida.json` no X-Forms (validação visual — checklist A7 mobile).
2. Rodar `activepieces-fluxo` sobre `saida.json` para gerar o fluxo.
3. Atualizar `docs/03-nomenclatura.md` — acrescentar linhas do dicionário observadas neste formulário (`login_rede`, `orgao`, `setor`, `municipio`, `perfil_solicitante`).
4. Atualizar `docs/05-auditoria.md` — status "solicitacao-de-acesso-wordpress" → **feito**, link para este `notas.md`.
5. Validar com Antonio: rótulos reescritos preservam intenção original?
6. Aplicar orquestrador aos outros 13 formulários.
