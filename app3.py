from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
security = HTTPBasic()

def validar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    usuario_correto = "admin"
    senha_correta = "1234"
    if credentials.username != usuario_correto or credentials.password != senha_correta:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

class Tarefa(BaseModel):
    id: int
    nome: str
    descricao: str
    concluida: bool = False

tarefas_db = [
    Tarefa(id=1, nome="Estudar FastAPI", descricao="Ver módulo de segurança"),
    Tarefa(id=2, nome="Ir na Academia", descricao="Treino de perna"),
    Tarefa(id=3, nome="Fazer Mercado", descricao="Comprar café e pão"),
    Tarefa(id=4, nome="Reunião Trabalho", descricao="Alinhamento de projeto"),
    Tarefa(id=5, nome="Limpar Casa", descricao="Organizar a sala"),
]

@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas(
    page: int = 1, 
    size: int = 2, 
    sort_by: Optional[str] = "id",
    username: str = Depends(validar_usuario) 
):

    if page < 1 or size < 1:
        raise HTTPException(status_code=400, detail="Página e tamanho devem ser maiores que zero")

    if sort_by not in ["id", "nome", "descricao"]:
        raise HTTPException(status_code=400, detail="Campo de ordenação inválido")
    
    dados_ordenados = sorted(tarefas_db, key=lambda x: getattr(x, sort_by))

    inicio = (page - 1) * size
    fim = inicio + size
    
    return dados_ordenados[inicio:fim]

@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa, username: str = Depends(validar_usuario)):
    tarefas_db.append(tarefa)
    return {"mensagem": f"Tarefa adicionada por {username}"}

@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int, username: str = Depends(validar_usuario)):
    for i, t in enumerate(tarefas_db):
        if t.id == tarefa_id:
            tarefas_db.pop(i)
            return {"mensagem": "Tarefa removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")