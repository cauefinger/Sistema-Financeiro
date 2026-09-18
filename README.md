Sistema Financeiro

API de um sistema financeiro desenvolvida em Python utilizando FastAPI e SQLAlchemy.

O projeto permite gerenciar operações financeiras por meio de uma API REST, com foco em organização, autenticação e integração com banco de dados.

============ TAREFAS ============

[OK] Usar o autentificar usuario no login e depois criar o token
[OK] Criar o refrash token
[OK] Chamar o refresh token 
[OK] Subir para o github
[OK] Trabalhar na transacao_router criando o primeiro post
[OK] Passar o arquivo .env, banco.db e pycache pro git ignore
[OK] Verificar a rota de transações
[OK] Testar rota de excluir transação
[OK] Criar a CONTA e todas as rotas/arquivos necessários 
[OK] Utilizar a transação router para criar saldo ou despesa
[ ] Fazer o editar transação e excluir transação considerando o sistema de saldo/despesa
--------- -------------- ----------
[OK] Transação GET está mostrando apenas última transação, arrumar para exibir todas as transações
[OK] Remover CATEGORIA_ID no POST da transação service
[ ] Tratar e forçar erros na rota de transação
[ ] Implementar a categoria transacao na transacao_service (obs: na hora de criar transação não pergunta sobre qual a categoria dela)