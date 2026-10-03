from pokemon import calcula_pontos_ataque, pokemon_evolui


def test_calcula_pontos_ataque_nivel_um():
    assert calcula_pontos_ataque(10, 1) == 10


def test_calcula_pontos_ataque_nivel_zero():
    assert calcula_pontos_ataque(5, 0) == 0


def test_calcula_pontos_ataque_nivel_cinco():
    assert calcula_pontos_ataque(20, 5) == 100


def test_pokemon_nao_evolui():
    assert pokemon_evolui(15, 20) is False


def test_pokemon_evolui_nivel_exato():
    assert pokemon_evolui(20, 20) is True


def test_pokemon_evolui_nivel_superior():
    assert pokemon_evolui(25, 20) is True