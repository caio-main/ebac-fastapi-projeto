from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Nossa "banco de dados" temporário
tarefas = []

# Modelo para o Lab aceitar os dados
class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False

@app.post("/tarefas")
def adicionar(tarefa: Tarefa):
    tarefas.append(tarefa.dict())
    return {"status": "Adicionada"}

@app.get("/tarefas")
def listar():
    return tarefas

@app.put("/tarefas/{nome}")
def concluir(nome: str):
    for t in tarefas:
        if t["nome"] == nome:
            t["concluida"] = True
            return {"status": "Concluída"}
    return {"erro": "Não encontrada"}

@app.delete("/tarefas/{nome}")
def remover(nome: str):
    global tarefas
    tarefas = [t for t in tarefas if t["nome"] != nome]
    return {"status": "Removida"}