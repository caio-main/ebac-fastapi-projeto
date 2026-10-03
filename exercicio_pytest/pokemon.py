def calcula_pontos_ataque(forca_base: int, nivel: int) -> int:
    return forca_base * nivel


def pokemon_evolui(nivel_atual: int, nivel_evolucao: int) -> bool:
    return nivel_atual >= nivel_evolucao