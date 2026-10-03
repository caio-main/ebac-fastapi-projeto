import pytest
from pokemon import calcula_pontos_ataque, pokemon_evolui


# Fixtures que fornecem os dados dos Pokémons
@pytest.fixture
def pikachu():
    return {"nome": "Pikachu", "forca_base": 10, "nivel": 1}


@pytest.fixture
def charizard():
    return {"nome": "Charizard", "forca_base": 20, "nivel": 5}


# Testes para calcula_pontos_ataque usando as fixtures
def test_calcula_pontos_ataque_pikachu(pikachu):
    resultado = calcula_pontos_ataque(pikachu["forca_base"], pikachu["nivel"])
    assert resultado == 10


def test_calcula_pontos_ataque_charizard(charizard):
    resultado = calcula_pontos_ataque(charizard["forca_base"], charizard["nivel"])
    assert resultado == 100


# Testes para pokemon_evolui usando as fixtures
def test_pokemon_nao_evolui_pikachu(pikachu):
    # Pikachu nivel 1 tentando evoluir com exigencia de nivel 16
    assert pokemon_evolui(pikachu["nivel"], 16) is False


def test_pokemon_evolui_charizard(charizard):
    # Charizard nivel 5 tentando evoluir com exigencia de nivel 5
    assert pokemon_evolui(charizard["nivel"], 5) is True