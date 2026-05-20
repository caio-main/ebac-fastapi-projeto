"""
INSTRUÇÕES DE EXECUÇÃO:
1. Abra o terminal na pasta onde este arquivo está salvo.
2. Execute o comando: python pokedex.py
3. Interaja com o menu digitando o número da opção desejada.
Dependências: Nenhuma (utiliza apenas a biblioteca padrão do Python 3).
"""

pokedex = {}
historico_capturas = []


def adicionar_pokemon():
    """Adiciona um novo Pokémon na Pokédex"""
    print("\n--- ADICIONAR POKÉMON ---")
    nome = input("Digite o nome do Pokémon: ").strip().capitalize()

    if nome in pokedex:
        print(f"Erro: O Pokémon '{nome}' já está cadastrado na Pokédex!")
        return

    tipo = input("Digite o tipo do Pokémon (ex: Fogo, Água, Elétrico): ").strip().capitalize()
    
    try:
        nivel = int(input("Digite o nível do Pokémon (1-100): "))
        if nivel < 1 or nivel > 100:
            print("Erro: O nível deve estar entre 1 e 100.")
            return
    except ValueError:
        print("Erro: O nível deve ser um número inteiro válido.")
        return

    pokedex[nome] = {
        "tipo": tipo,
        "nivel": nivel
    }
    print(f"Sucesso: {nome} adicionado com sucesso!")


def listar_pokemon():
    """Exibe os Pokémon cadastrados em ordem alfabética"""
    print("\n--- LISTAR POKÉMON ---")
    if not pokedex:
        print("A Pokédex está vazia.")
        return

    nomes_ordenados = sorted(pokedex.keys())
    
    for nome in nomes_ordenados:
        dados = pokedex[nome]
        print(f"{nome} - {dados['tipo']} - Nível: {dados['nivel']}")


def remover_pokemon():
    """Remove um Pokémon da Pokédex"""
    print("\n--- REMOVER POKÉMON ---")
    nome = input("Digite o nome do Pokémon a ser removido: ").strip().capitalize()

    if nome in pokedex:
        del pokedex[nome]
        print(f"Sucesso: {nome} foi removido da Pokédex.")
    else:
        print(f"Erro: O Pokémon '{nome}' não foi encontrado na Pokédex.")


def atualizar_nivel():
    """Atualiza o nível de um Pokémon existente"""
    print("\n--- ATUALIZAR NÍVEL ---")
    nome = input("Digite o nome do Pokémon: ").strip().capitalize()

    if nome not in pokedex:
        print(f"Erro: O Pokémon '{nome}' não existe na Pokédex.")
        return

    try:
        novo_nivel = int(input("Digite o novo nível (1-100): "))
        if novo_nivel < 1 or novo_nivel > 100:
            print("Erro: O nível deve estar entre 1 e 100.")
            return
    except ValueError:
        print("Erro: O nível deve ser um número inteiro válido.")
        return

    # Atualiza o nível no dicionário
    pokedex[nome]["nivel"] = novo_nivel
    print(f"Sucesso: Nível de {nome} atualizado para {novo_nivel}!")


def registrar_captura():
    """Registra a quantidade de vezes que um Pokémon foi capturado"""
    print("\n--- REGISTRAR CAPTURA ---")
    nome = input("Digite o nome do Pokémon capturado: ").strip().capitalize()

    if nome not in pokedex:
        print(f"Erro: O Pokémon '{nome}' precisa estar cadastrado na Pokédex primeiro.")
        return

    try:
        quantidade = int(input("Digite a quantidade de vezes capturada: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro válido.")
        return

    historico_capturas.append({
        "nome": nome,
        "quantidade": quantidade
    })
    print(f"Sucesso: Captura de {quantidade}x {nome} registrada!")


def exibir_historico():
    """Exibe o histórico de todas as capturas realizadas"""
    print("\n--- HISTÓRICO DE CAPTURAS ---")
    if not historico_capturas:
        print("Nenhuma captura foi registrada ainda.")
        return

    for registro in historico_capturas:
        print(f"Pokémon: {registro['nome']} | Quantidade: {registro['quantidade']}x")


def menu():
    """Fluxo principal do programa com menu de opções"""
    while True:
        print("\n================ POKÉDEX ================")
        print("1. Adicionar Pokémon")
        print("2. Listar Pokémon (Ordem Alfabética)")
        print("3. Remover Pokémon")
        print("4. Atualizar Nível do Pokémon")
        print("5. Registrar Captura")
        print("6. Exibir Histórico de Capturas")
        print("7. Sair")
        print("=========================================")
        
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == "1":
            adicionar_pokemon()
        elif opcao == "2":
            listar_pokemon()
        elif opcao == "3":
            remover_pokemon()
        elif opcao == "4":
            atualizar_nivel()
        elif opcao == "5":
            registrar_captura()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            print("\nEncerrando a Pokédex... Até mais, treinador!")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 7.")

if __name__ == "__main__":
    menu()