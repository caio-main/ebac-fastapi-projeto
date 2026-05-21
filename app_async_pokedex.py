import asyncio
import random
import time

# Passo 1 e 3: Definindo as funções assíncronas para cada região com Pokémons específicos
async def busca_pokemon_kanto():
    # Lista de Pokémons possíveis de Kanto
    pokemons_kanto = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"]
    pokemon = random.choice(pokemons_kanto)
    
    # Passo 2: Simula o tempo de busca aleatório entre 1 e 5 segundos (Não bloqueante!)
    tempo_busca = random.uniform(1, 5)
    print(f"[Kanto] Iniciando busca... (Deve demorar {tempo_busca:.2f}s)")
    await asyncio.sleep(tempo_busca)
    
    print(f"[Kanto] 🟢 Sucesso! Encontrado: {pokemon}")
    return f"Kanto: {pokemon}"

async def busca_pokemon_johto():
    pokemons_johto = ["Chikorita", "Cyndaquil", "Totodile", "Marill"]
    pokemon = random.choice(pokemons_johto)
    
    tempo_busca = random.uniform(1, 5)
    print(f"[Johto] Iniciando busca... (Deve demorar {tempo_busca:.2f}s)")
    await asyncio.sleep(tempo_busca)
    
    print(f"[Johto] 🟢 Sucesso! Encontrado: {pokemon}")
    return f"Johto: {pokemon}"

async def busca_pokemon_hoenn():
    pokemons_hoenn = ["Treecko", "Torchic", "Mudkip", "Ralts"]
    pokemon = random.choice(pokemons_hoenn)
    
    tempo_busca = random.uniform(1, 5)
    print(f"[Hoenn] Iniciando busca... (Deve demorar {tempo_busca:.2f}s)")
    await asyncio.sleep(tempo_busca)
    
    print(f"[Hoenn] 🟢 Sucesso! Encontrado: {pokemon}")
    return f"Hoenn: {pokemon}"

# Função principal que gerencia o Event Loop e mede o tempo
async def main():
    print("====== INICIANDO SIMULADOR DE CAPTURA ASSÍNCRONA ======\n")
    
    tempo_inicial = time.perf_counter()
    
    resultados = await asyncio.gather(
        busca_pokemon_kanto(),
        busca_pokemon_johto(),
        busca_pokemon_hoenn()
    )
    
    # Calcula o tempo total decorrido
    tempo_total = time.perf_counter() - tempo_inicial
    
    # Passo 6: Mostra os resultados organizados no console
    print("\n====== RESUMO DA EXPEDIÇÃO ======")
    for resultado in resultados:
        print(f"• {resultado}")
        
    print(f"\n⏱️ Tempo total de execução concorrente: {tempo_total:.2f} segundos")
    print("==================================================")

# Ponto de entrada que aciona o Event Loop do asyncio
if __name__ == "__main__":
    asyncio.run(main())