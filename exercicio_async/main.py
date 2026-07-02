from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI(
    title="API Assíncrona de Livros",
    description="Exercício prático de endpoints assíncronos com FastAPI"
)

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str

livros_db: List[Livro] = []


@app.get("/livros", response_model=List[Livro])
async def listar_livros():
    """Retorna a lista de todos os livros cadastrados."""
    await asyncio.sleep(0.5) 
    return livros_db

@app.post("/livros", response_model=Livro, status_code=201)
async def criar_livro(livro: Livro):
    """Adiciona um novo livro ao banco de dados."""
    await asyncio.sleep(0.5) 
    
    for l in livros_db:
        if l.id == livro.id:
            raise HTTPException(status_code=400, detail="Um livro com este ID já existe.")
            
    livros_db.append(livro)
    return livro

@app.put("/livros/{id}", response_model=Livro)
async def atualizar_livro(id: int, livro_atualizado: Livro):
    """Atualiza as informações de um livro existente pelo ID."""
    await asyncio.sleep(0.5) 
    
    for index, livro in enumerate(livros_db):
        if livro.id == id:
            livros_db[index] = livro_atualizado
            return livros_db[index]
            
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.delete("/livros/{id}", status_code=204)
async def deletar_livro(id: int):
    """Remove um livro do banco de dados pelo ID."""
    await asyncio.sleep(0.5) 
    
    for index, livro in enumerate(livros_db):
        if livro.id == id:
            del livros_db[index]
            return 
            
    raise HTTPException(status_code=404, detail="Livro não encontrado.")