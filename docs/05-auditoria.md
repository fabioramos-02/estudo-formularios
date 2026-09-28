# 5. Auditoria dos 14 formulários

Os formulários que existem hoje no FormFlow e serão reconstruídos no X-Forms. Cada um recebe uma
ficha, preenchida com o [checklist](04-checklist.md).

**Status:** `a fazer` · `em andamento` · `pronto`

| # | Serviço | Órgão | Status |
|---|---|---|---|
| 1 | [Solicitar acesso ao WordPress](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/validar-antonio-wordpress) | SEGOV | pronto |
| 2 | [Solicitação de diárias para servidores da Fundect](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/solicitacao-de-diarias-para-servidores-da-fundect) | Fundect | pronto |
| 3 | [Cadastrar profissional habilitado para cultivos e estabelecimentos de insumos agrícolas](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastrar-profissional-habilitado-para-cultivos-e-estabelecimentos-de-insumos-agricolas) | IAGRO | pronto |
| 4 | [Cadastrar indústria de produtos agrotóxicos no e-Saniagro](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastrar-industria-produtos-agrotoxicos-no-e-saniagro) | IAGRO | pronto |
| 5 | [Cancelar o registro de estabelecimento comercial e prestador de serviço de agrotóxico](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cancelar-o-registro-de-estabelecimento-comercial-e-prestador-de-servico-de-agrotoxico) | IAGRO | pronto |
| 6 | [Obter Selo ARTE](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/obter-selo-arte) | IAGRO | pronto |
| 7 | [Solicitação da Negativa de Tombamento](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/solicitacao-da-negativa-de-tombamento) | FCMS | pronto |
| 8 | [Cadastrar ou atualizar médico veterinário — avicultura ou suinocultura](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastrar-ou-atualizar-medico-veterinario-avicultura-ou-suinocultura) | IAGRO | pronto |
| 9 | [Cadastro no Sistema Estadual de Bibliotecas Públicas](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastro-no-sistema-estadual-de-bibliotecas-publicas-de-mato-grosso-do-sul-sebpms) | FCMS | pronto |
| 10 | [Cadastrar ou atualizar empresa integradora de ave ou suíno](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastrar-ou-atualizar-empresa-integradora-de-ave-ou-suino) | IAGRO | pronto |
| 11 | [Requerer certificado de destruição de soqueira de algodão](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/requerer-certificado-de-destruicao-de-soqueira-de-algodao) | IAGRO | pronto |
| 12 | [Solicitar cópia de laudos periciais](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/solicitar-copia-de-laudos-periciais) | CGP | pronto |
| 13 | [Cadastrar ou atualizar laboratório de diagnóstico em sanidade avícola](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/cadastrar-ou-atualizar-laboratorio-de-diagnostico-em-sanidade-avicola) | IAGRO | pronto |
| 14 | [Solicitar emissão de certidão de atendimento de emergência](https://portal.demo-aws.xvia.com.br/app/ms-forms-designer/forms/edit/solicitar-emissao-de-certidao-de-atendimento-de-emergencia-teste) | SEJUSP | pronto |

Ao terminar uma ficha: troque o status para `pronto`.

---

## Achados que se repetem

> Síntese dos padrões que aparecem em mais de um formulário. Lista completa,
> com todos os formulários citados por linha, em
> [andamento/recomendacoes.md](andamento/recomendacoes.md#1-achados-que-se-repetem).

| # | Achado | Em quantos | Item do checklist | O que fazer no X-Forms |
|---|---|---|---|---|
| 1 | Campo RG (e "Órgão expedidor") redundante — CPF já basta com a nova CIN | 3+ | C.3 | Remover; manter só `cpf` com máscara |
| 2 | Campo UF / Estado / Região redundante quando serviço é só de MS | 3 | C.3 | Remover ou fixar oculto com valor `MS` |
| 3 | Coordenadas geográficas exigidas do cidadão | 2 | C.3 | Remover — endereço + CEP + município já localizam |
| 4 | Dados pessoais **não** pré-preenchidos do gov.br | 14 | C.1 | Puxar do gov.br (Lei 14.129/2021 + LGPD art. 6º III) |
| 5 | Ordem dos campos fora da lógica | 2+ | B.1 | identificação → vínculo → pedido → anexos → confirmação |
| 6 | Formulário longo em 1 única página (>15 campos) | 2 | A.1 | Dividir em etapas (*one thing per page*) |
| 7 | Campo duplicado para o mesmo dado (2 telefones, 3 partes de endereço) | 2 | C.4 | Unificar em campo múltiplo ou texto único |
| 8 | Dependência entre campos não modelada (Setor↔Órgão, endereço↔CEP) | 2 | B.3 | `visibleIf` — filho só aparece após pai preenchido |
| 9 | Falta máscara em campos de formato fixo (CPF, CEP, telefone) | 2+ | D.2 | Aplicar máscara — X-Forms lê `9` como dígito numérico |
| 10 | Texto aberto onde deveria ser lista fechada (Estado, Cor/Raça) | 2 | C.5 | Trocar por `dropdown` |

## O que já está bom e deve ser mantido

- **Máscaras** de CPF, CNPJ e telefone já ativas em vários formulários — manter via `inputMask`.
- **`dropdown` para Município** com cidades de MS — manter em todos com endereço.
- **Upload com múltiplos anexos** já configurado — manter, declarar tipo aceito.
- **Campos condicionais `visibleIf`** já suportados nativamente — expandir uso.
- **Descrição no cabeçalho** de cada página com contexto — manter, desde que enxuta.
- **Separação em etapas coerentes** (modelo: Diárias Fundect — servidor → viagem → dados bancários).

Detalhe e justificativa em [andamento/recomendacoes.md](andamento/recomendacoes.md#2-o-que-ja-esta-bom-e-deve-ser-mantido).

## O que precisa mudar (ações prioritárias)

Ordem = impacto na experiência de preenchimento.

1. **Pré-preencher dados do cidadão via gov.br** (14/14) — Lei 14.129/2021 + LGPD art. 6º III.
2. **Reordenar campos por lógica** — identificação → vínculo → pedido → anexos → confirmação.
3. **Dividir formulário longo em etapas** (>10 campos ou temas distintos) — GOV.UK.
4. **Remover campos redundantes** — RG, UF/Região, coordenadas, campos subjetivos.
5. **Unificar campos duplicados** — telefones e partes de endereço.
6. **Aplicar máscara e validação na entrada** — WCAG 2.2 critério 3.3.1.
7. **Trocar texto aberto por `dropdown`** quando a lista é finita e conhecida.
8. **Enxugar a descrição do cabeçalho** — não empurrar o primeiro campo para fora da dobra.
9. **Modelar dependências com `visibleIf`** — reduzir poluição visual inicial.
10. **Documentar limites do X-Forms** — comparação entre campos e data dinâmica não são suportados hoje. Levar à SGD.

Justificativa e evidência por formulário em [andamento/recomendacoes.md](andamento/recomendacoes.md#3-o-que-precisa-mudar-acoes-prioritarias).
