# API FastAPI com Cache Redis 📚🚀

Este projeto implementa uma API de livros utilizando FastAPI integrada ao Redis como camada de cache. Aplica-se a estratégia **Cache-Aside** para otimizar o tempo de resposta das consultas e reduzir o processamento do servidor principal.

---

## 🛠️ Como Executar o Projeto

### Passo 1: Subir o Redis via Docker
Para rodar o servidor do Redis rapidamente de forma isolada na porta padrão `6379`, execute o seguinte comando no seu terminal:
```bash
docker run --name redis-livros -p 6379:6379 -d redis