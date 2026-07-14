Exercício: FastAPI + Celery + Redis (Assíncrono)
Este projeto demonstra a configuração e utilização do Celery com Redis como broker para executar tarefas matemáticas demoradas (soma e fatorial) de forma assíncrona, sem bloquear a API FastAPI.

Dependências Utilizadas
FastAPI

Uvicorn

Celery

Redis

Para instalar as bibliotecas necessárias, execute o comando:

pip install fastapi uvicorn celery redis

Como Executar o Projeto
Siga a ordem dos terminais abaixo para rodar a aplicação no Windows:

1. Iniciar o Servidor Redis
Inicie o servidor localmente através do comando:

& "C:\Program Files\Redis\redis-server.exe"

2. Iniciar o Celery Worker
Em um segundo terminal, acesse a pasta do exercício e inicie o worker utilizando o pool solo para compatibilidade com o Windows:

cd exercicio_celery
celery -A celery_app worker -l info -P solo

3. Iniciar a API FastAPI
Em um terceiro terminal, execute a API utilizando o Uvicorn:

cd exercicio_celery
uvicorn main:app --reload

Testes Realizados (PowerShell)
Enviar tarefa de soma (POST)
Invoke-RestMethod -Uri "http://localhost:8000/soma" -Method Post -ContentType "application/json" -Body '{"a": 15.5, "b": 24.5}'

Enviar tarefa de fatorial (POST)
Invoke-RestMethod -Uri "http://localhost:8000/fatorial" -Method Post -ContentType "application/json" -Body '{"n": 10}'

Consultar resultado da tarefa (GET)
Substitua o {task_id} pelo ID retornado na requisição anterior:

Invoke-RestMethod -Uri "http://localhost:8000/tarefa/{task_id}" -Method Get