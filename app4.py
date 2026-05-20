from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class TarefaDB(Base):
    __tablename__ = "tarefas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: Optional[bool] = False

class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

    class Config:
        from_attributes = True 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Gerenciador de Tarefas com SQLite - EBAC")

@app.post("/tarefas", response_model=TarefaResponse, status_code=201)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    nova_tarefa = TarefaDB(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        concluida=tarefa.concluida
    )
    db.add(nova_tarefa)
    db.commit() 
    db.refresh(nova_tarefa) 
    return nova_tarefa

@app.get("/tarefas", response_model=List[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(TarefaDB).all()

@app.put("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaCreate, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaDB).filter(TarefaDB.id == tarefa_id).first()
    
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    tarefa.titulo = tarefa_atualizada.titulo
    tarefa.descricao = tarefa_atualizada.descricao
    tarefa.concluida = tarefa_atualizada.concluida
    
    db.commit()
    db.refresh(tarefa)
    return tarefa

@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaDB).filter(TarefaDB.id == tarefa_id).first()
    
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(tarefa)
    db.commit()
    return None