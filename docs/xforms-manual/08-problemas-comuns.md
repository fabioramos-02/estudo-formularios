# Problemas comuns

[← Manual do X-Forms](README.md)

## Mensagens e o que fazer

As mensagens de erro do Designer aparecem numa janela **Não foi possível concluir** ou num aviso vermelho no topo da tela, com o motivo devolvido pelo sistema.

| O que aparece                                                                        | Causa                                                                                                   | O que fazer                                                                                                                                             |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Acesso restrito" ao abrir o Designer                                                | A pessoa não está em nenhum grupo do Designer, ou o grupo ainda não vale para a sessão atual.           | Peça ao administrador do X-Forms para ser incluído em `/portal/xforms-designer/admin` ou `/portal/xforms-designer/editor`. Depois saia e entre de novo. |
| "Acesso restrito" na revisão                                                         | A revisão das alterações é só do administrador.                                                         | Peça a um administrador.                                                                                                                                |
| "Você não tem permissão para esta operação."                                         | Ação de outro papel (por exemplo, editor tentando salvar o rascunho de outro editor) ou acesso perdido. | Confira o papel; se for o rascunho de outra pessoa, combine com ela ou com um administrador.                                                            |
| "Outro editor acabou de criar um rascunho para este formulário; recarregue a página" | Duas pessoas começaram uma alteração no mesmo formulário ao mesmo tempo.                                | Recarregue: o rascunho é de quem salvou primeiro.                                                                                                       |
| "O rascunho mudou depois da revisão; abra a revisão de novo antes de aprovar"        | O editor alterou o rascunho enquanto a revisão estava aberta.                                           | Abra a revisão de novo e confira a versão atual.                                                                                                        |
| "O rascunho não está aguardando aprovação"                                           | O editor ainda não enviou, ou alterou depois de enviar.                                                 | Espere o envio; a lista mostra _Aguardando aprovação_ quando estiver pronto.                                                                            |
| "O parâmetro serviceSlug é obrigatório na URL..."                                    | O link do formulário geral está sem o `?serviceSlug=<serviço>`.                                         | Corrija o link divulgado.                                                                                                                               |
| "Erro ao enviar resposta!" com a mensagem de instabilidade, sempre, no mesmo link    | O `serviceSlug` do link não existe no catálogo de serviços do portal, e a resposta é recusada.          | Confira o slug do serviço na página do serviço no portal (`/servicos/<slug>`) e corrija o link divulgado.                                               |
| "Formulário indisponível"                                                            | O formulário está fora do ar, ou a prévia foi aberta por quem não é do Designer.                        | Publique o formulário pela lista (administrador), ou abra a prévia com um usuário do Designer.                                                          |
| "Sessão expirada. Entre novamente para continuar."                                   | A sessão do Smartpass Login venceu.                                                                     | Entre de novo e repita a ação.                                                                                                                          |

## Perguntas frequentes

**O editor pode publicar uma alteração urgente?** Não. Peça a um administrador para revisar, ou para fazer a alteração direto na versão no ar.

**Por que o editor não vê as respostas?** As respostas podem ter dados pessoais dos cidadãos (LGPD), e só o administrador as acessa.

**Duplicar um formulário que ainda não foi aprovado traz as perguntas?** Não: duplicar copia a versão no ar, que num formulário novo de editor fica vazia até a aprovação.
