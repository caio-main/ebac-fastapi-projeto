from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Passo 1: Criar o Modelo com Pydantic
class Tarefa(BaseModel):
    nome: str          # Obrigatório
    descricao: str     # Obrigatório
    concluida: bool = False  # Opcional, padrão False

# Passo 3: Lista para armazenar objetos do tipo Tarefa
tarefas: List[Tarefa] = []

# Passo 2: Rota para Adicionar Tarefa (POST)
@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    # O FastAPI valida os dados automaticamente aqui!
    tarefas.append(tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso!"}

# Passo 4: Rota para Listar Tarefas (GET)
@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    # O Pydantic converte os objetos para JSON automaticamente
    return tarefas

# Passo 5: Atualizar as outras rotas usando o campo 'nome'
@app.put("/tarefas/{nome}")
def marcar_concluida(nome: str):
    for t in tarefas:
        if t.nome == nome: # Acessando como objeto (.nome) e não dicionário (["nome"])
            t.concluida = True
            return {"mensagem": f"Tarefa '{nome}' concluída!"}
    return {"erro": "Tarefa não encontrada"}

@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str):
    for i, t in enumerate(tarefas):
        if t.nome == nome:
            tarefas.pop(i)
            return {"mensagem": f"Tarefa '{nome}' removida!"}
    return {"erro": "Tarefa não encontrada"}