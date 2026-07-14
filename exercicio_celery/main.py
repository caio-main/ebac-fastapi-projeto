from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery_app import celery_app, calcular_soma, calcular_fatorial 
from celery.result import AsyncResult

app = FastAPI(
    title="FastAPI + Celery + Redis",
    description="API para disparo de tarefas assíncronas in background"
)

class SomaInput(BaseModel):
    a: float
    b: float

class FatorialInput(BaseModel):
    n: int

@app.post("/soma", status_code=202)
async def disparar_soma(dados: SomaInput):
    """Dispara a tarefa de soma em background e retorna imediatamente."""
    tarefa = calcular_soma.delay(dados.a, dados.b)
    return {
        "mensagem": "Tarefa de soma enviada para a fila com sucesso!",
        "task_id": tarefa.id,
        "status": tarefa.status
    }

@app.post("/fatorial", status_code=202)
async def disparar_fatorial(dados: FatorialInput):
    """Dispara a tarefa de fatorial em background e retorna imediatamente."""
    if dados.n < 0:
        raise HTTPException(status_code=400, detail="O número deve ser inteiro e maior ou igual a zero.")
        
    tarefa = calcular_fatorial.delay(dados.n)
    return {
        "mensagem": "Tarefa de fatorial enviada para a fila com sucesso!",
        "task_id": tarefa.id,
        "status": tarefa.status
    }

@app.get("/tarefa/{task_id}")
async def obter_status_tarefa(task_id: str):
    """Endpoint para verificar o status e o resultado de uma tarefa pelo ID."""
    resultado_async = AsyncResult(task_id, app=celery_app)
    
    resposta = {
        "task_id": task_id,
        "status": resultado_async.status,
        "resultado": None
    }
    if resultado_async.ready():
        resposta["resultado"] = resultado_async.result
    return resposta