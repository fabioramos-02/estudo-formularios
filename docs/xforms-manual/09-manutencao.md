# Manutenção deste manual

[← Manual do X-Forms](README.md)

## Manutenção deste manual

Este manual descreve o Designer como ele está. Mudou uma tela, um botão, um texto ou uma regra que o usuário vê, o manual muda na mesma entrega, e a captura correspondente é regenerada.

As imagens vivem em `docs/manual/img/`, numeradas pelo capítulo a que pertencem (`01-` e `02-` para a Central, `1x-` para a lista, `2x-` para criar e editar, `3x-` para tipos de pergunta, `4x-` para a aprovação, `5x-` para divulgação, `6x-` para lógica e expressões e `7x-` para NPS). Captura nova entra com o próximo número da seção.

As capturas atuais saíram de um ambiente local com o front, o gateway (KrakenD), a API e o Postgres reais e dados de teste: um formulário e um NPS publicados pelo administrador com alteração de um editor aguardando aprovação, outros com alteração devolvida e itens novos de editor. Para regenerar:

1. Suba o Postgres, a API (`xvia-x-forms-backend`) com as migrations aplicadas e o gateway com a configuração `local`, conforme o README de cada repositório, e o front com `pnpm dev` ([`AGENTS.md`](https://gitlabs.ms.gov.br/xvia/x-forms/xvia-x-forms/-/blob/develop/AGENTS.md)).
2. Entre com um usuário administrador e um editor (grupos em [papéis](README.md#quem-faz-o-quê-papéis)) e monte os mesmos cenários.
3. Capture só a área da tela que interessa, sem dados reais de cidadãos, e substitua o arquivo com o mesmo nome.
