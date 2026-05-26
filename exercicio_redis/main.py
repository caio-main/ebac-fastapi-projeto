import json
from fastapi import FastAPI, HTTPException
import fakeredis.aioredis as aioredis

app = FastAPI(title="API de Livros com Cache Redis")

BANCO_LIVROS = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Corvo", "autor": "Edgar Allan Poe"}
]

CACHE_KEY = "livros"
TTL_SEGUNDOS = 60

redis_client = None

@app.on_event("startup")
async def startup_event():
    """Estabece a conexão com o Redis simulado de forma reutilizável"""
    global redis_client
    redis_client = aioredis.FakeRedis(decode_responses=True)

@app.on_event("shutdown")
async def shutdown_event():
    """Fecha a conexão com o Redis ao encerrar o app"""
    if redis_client:
        await redis_client.close()


async def salvar_livros_redis(livros: list):
    """Salva a lista de livros no Redis convertendo para string JSON e define o TTL"""
    if redis_client:
        livros_json = json.dumps(livros)
        await redis_client.setex(CACHE_KEY, TTL_SEGUNDOS, livros_json)

async def deletar_livros_redis():
    """Remove a chave de livros do Redis para garantir a consistência dos dados"""
    if redis_client:
        await redis_client.delete(CACHE_KEY)


@app.get("/livros")
async def listar_livros():
    """Endpoint de listagem aplicando a estratégia Cache-Aside"""
    if not redis_client:
        return BANCO_LIVROS

    cache_livros = await redis_client.get(CACHE_KEY)
    
    if cache_livros:
        print("--> Dados recuperados do CACHE (Redis)")
        return json.loads(cache_livros)
    
    print("--> Cache Miss! Buscando do BANCO DE DADOS e atualizando o cache...")
    livros_banco = BANCO_LIVROS
    
    await salvar_livros_redis(livros_banco)
    
    return livros_banco

@app.post("/livros")
async def adicionar_livro(livro: dict):
    """Endpoint para adicionar livros (Invalida o cache antigo para manter consistência)"""
    BANCO_LIVROS.append(livro)
    
    await deletar_livros_redis()
    print("--> Novo livro adicionado. Cache antigo deletado com sucesso!")
    
    return {"mensagem": "Livro adicionado e cache invalidado", "livro": livro}