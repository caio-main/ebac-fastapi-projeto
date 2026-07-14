from celery import Celery
import time
import math

# Configura o Celery utilizando o Redis oficial
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def calcular_soma(a: float, b: float) -> float:
    """Calcula a soma de dois números simulando uma tarefa demorada."""
    print(f"[Celery] Iniciando cálculo de soma: {a} + {b}...")
    time.sleep(5)  # Simula um workload pesado de 5 segundos
    resultado = a + b
    print(f"[Celery] Soma concluída! Resultado: {resultado}")
    return resultado

@celery_app.task
def calcular_fatorial(n: int) -> int:
    """Calcula o fatorial de um número de forma iterativa com delay simulado."""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos.")
        
    print(f"[Celery] Iniciando cálculo de fatorial para {n}...")
    time.sleep(5)  # Simula um workload pesado de 5 segundos
    resultado = math.factorial(n)
    print(f"[Celery] Fatorial concluído! Resultado: {resultado}")
    return resultado