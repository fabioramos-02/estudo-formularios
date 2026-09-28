# Recomendações comuns aos 14 formulários

> **Autor:** Antonio (estagiário)
> **Como ler:** achado que aparece em **2 ou mais formulários** vira padrão e fica aqui.
> Achado que só aparece em 1 formulário fica na ficha dele
> (`docs/andamento/mapeamento/NN-*.md`), não sobe para cá.

Este arquivo alimenta `03-nomenclatura.md`, `04-checklist.md` e as seções
finais de `05-auditoria.md`.

---

## 1. Achados que se repetem

> Problema que aparece em mais de um formulário. É daqui que sai a conversa
> com a SGD. Sem número na coluna "Em quantos", não é padrão — é caso isolado.

| # | Achado | Em quantos | Formulários | Item do checklist | O que fazer no X-Forms |
|---|---|---|---|---|---|
| 1 | Campo **RG** (e "Órgão expedidor") redundante — CPF já basta com a nova CIN | 3+ | WordPress, Laudos periciais, Diárias Fundect | C.3 (campo desnecessário) | Remover; manter só `cpf` com máscara |
| 2 | Campo **UF / Estado / Região** redundante quando serviço é só de MS | 3 | Cancelar agrotóxico, Bibliotecas (campo *Região*), Laboratório avícola | C.3 | Remover ou fixar oculto com valor `MS` |
| 3 | **Coordenadas geográficas** exigidas do cidadão | 2 | Bibliotecas, Empresa integradora | C.3 | Remover — endereço + CEP + município já localizam |
| 4 | Dados pessoais **não pré-preenchidos** do gov.br (CPF, nome, e-mail, telefone) | 14 | Todos | C.1 (dado que o governo já tem) | Puxar do gov.br; ver Lei 14.129/2021 + LGPD art. 6º III |
| 5 | **Ordem dos campos** fora da lógica (dado de trabalho antes de identificação, ou tudo misturado) | 2+ | WordPress (*Setor* penúltimo), Laudos periciais (tudo em 1 página) | B.1 (ordem) | Reordenar: identificação → vínculo → pedido → anexos → confirmação |
| 6 | Formulário longo concentrado em **1 única página** (>15 campos) | 2 | Laudos periciais, Bibliotecas | A.1 (*one thing per page*) | Dividir em 2–3 etapas lógicas (GOV.UK Design System) |
| 7 | Campo **duplicado** para o mesmo tipo de dado (dois telefones, três partes de endereço) | 2 | Vet avicultura/suinocultura (2 telefones), Certidão emergência (rua + bairro + número) | C.4 (duplicação) | Unificar em campo múltiplo ou texto único com orientação |
| 8 | Dependência entre campos **não** modelada (Setor↔Órgão, endereço↔CEP) | 2 | WordPress, Laboratório avícola | B.3 (proximidade lógica) | Usar `visibleIf` para exibir o campo dependente só após o pai preenchido |
| 9 | Campos **sem máscara** de entrada em dados de formato fixo (CPF, CEP, telefone) | 2+ | Laboratório avícola, Certidão emergência | D.2 (validação na entrada) | Aplicar máscara — X-Forms lê `9` como dígito numérico |
| 10 | **Texto aberto** onde deveria ser lista fechada (Estado, Cor/Raça) | 2 | Laboratório avícola, outros com UF livre | C.5 (padronização) | Trocar por `dropdown` — evita erro de digitação e diverge de grafia |

---

## 2. O que já está bom e deve ser mantido

> Nem tudo no FormFlow está errado. O que funciona precisa **sobreviver à
> migração** para o X-Forms — não recriar pior por descuido.

- **Máscaras de CPF, CNPJ e telefone** já ativas em vários formulários (Diárias
  Fundect, Soqueira de algodão) — manter via `inputMask` no X-Forms.
- **Uso de `dropdown` para Município** com a lista das cidades de MS — evita
  erro de grafia; manter em todos os formulários com endereço.
- **Upload de arquivo com múltiplos anexos** já configurado (Soqueira, Bibliotecas)
  — manter, adicionar tipo aceito (`.pdf`, `.jpeg`) explícito no rótulo.
- **Campos condicionais (`visibleIf`)** já suportados nativamente — expandir uso,
  não remover onde já existe (ex.: `legislacao_criacao` em Bibliotecas só aparece
  se tipo = pública).
- **Descrição no cabeçalho de cada página** com contexto do que se pede — manter,
  desde que enxuta (ver seção 3, item 6).
- **Separação em etapas** quando ela existe (Diárias Fundect tem 3 páginas
  coerentes: servidor → viagem → dados bancários) — modelo a replicar.

---

## 3. O que precisa mudar (ações prioritárias)

> Mudança estrutural que atravessa vários formulários. Ordem = **impacto na
> experiência de preenchimento** (regra nº 1 do estudo).

1. **Pré-preencher dados do cidadão via gov.br** — CPF, nome completo, e-mail e
   telefone. Aparece em 14/14. Base: Lei 14.129/2021 (vedação de exigir dado que
   a administração já possui) + LGPD art. 6º III (minimização).
2. **Reordenar campos por lógica: identificação → vínculo/perfil → pedido →
   anexos → confirmação.** Hoje quase todos os 14 misturam. Checklist B.1.
3. **Dividir formulário longo em etapas** (*one thing per page*) sempre que
   passar de ~10 campos ou misturar temas distintos. GOV.UK Design System.
4. **Remover campos redundantes** — RG (CIN cobre com CPF), UF/Região (quando
   serviço é só de MS), Coordenadas Geográficas (endereço já localiza), campos
   subjetivos ("descreva em uma frase").
5. **Unificar campos duplicados** — telefones e partes de endereço viram um
   campo múltiplo (`arrayValue: true`) ou campo único com orientação.
6. **Aplicar máscara e validação na entrada** em todo campo de formato fixo
   (CPF, CEP, telefone, data). WCAG 2.2 critério 3.3.1 (identificação de erro).
7. **Trocar texto aberto por `dropdown`** sempre que a lista é finita e
   conhecida (Estado, Cor/Raça, tipo de documento).
8. **Enxugar a descrição do cabeçalho** — descrição longa empurra o primeiro
   campo para baixo da dobra. Manter só o essencial ao cidadão.
9. **Modelar dependências com `visibleIf`** — o campo filho aparece só depois
   do pai preenchido. Reduz poluição visual inicial.
10. **Documentar limites do X-Forms** que apareceram na auditoria — comparação
    entre dois campos (ex.: `cidade_origem != cidade_destino`) e data dinâmica
    (ex.: `data_saida > hoje`) não são suportados hoje. Levar à SGD.

---

## Ver por formulário

Cada achado acima veio das fichas de mapeamento em
[`docs/andamento/mapeamento/`](mapeamento/index.md). Para o caso concreto de um
formulário específico, abra a ficha correspondente.
