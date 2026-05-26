import os

estoque = {}

def limpar_tela():
    # Limpa o terminal para o menu ficar organizado
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    try:
        quantidade = int(input(f"Digite a quantidade de {nome}: "))
        preco = float(input(f"Digite o preço de {nome}: "))
        
        # Estrutura: { "Produto": {"quantidade": X, "preço": Y} }
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        print(f"\n✅ Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("\n❌ Erro: Quantidade e Preço devem ser números!")
    input("\nPressione Enter para continuar...")

def listar_produtos():
    if not estoque:
        print("\n⚠️ O estoque está vazio.")
    else:
        print("\n--- Lista de Produtos (Ordem Alfabética) ---")
        # Usando lambda para ordenar pelas chaves (nomes dos produtos)
        produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0].lower())
        
        for nome, dados in produtos_ordenados:
            print(f"Nome do produto: {nome} - Quantidade: {dados['quantidade']} - Preço: R${dados['preço']:.2f}")
    
    input("\nPressione Enter para continuar...")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ").strip()
    if nome in estoque:
        del estoque[nome]
        print(f"\n🗑️ Produto '{nome}' removido!")
    else:
        print("\n❌ Erro: Produto não encontrado no estoque.")
    input("\nPressione Enter para continuar...")

def atualizar_quantidade():
    nome = input("Digite o nome do produto para atualizar: ").strip()
    if nome in estoque:
        try:
            nova_qtd = int(input(f"Digite a nova quantidade para {nome}: "))
            estoque[nome]["quantidade"] = nova_qtd
            print(f"\n🔄 Quantidade de '{nome}' atualizada para {nova_qtd}!")
        except ValueError:
            print("\n❌ Erro: A quantidade deve ser um número inteiro.")
    else:
        print("\n❌ Erro: Produto não encontrado.")
    input("\nPressione Enter para continuar...")

def exibir_menu():
    while True:
        limpar_tela()
        print("=== GERENCIADOR DE ESTOQUE ===")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Remover produto")
        print("4. Atualizar quantidade de produto")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            remover_produto()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")
            input("Pressione Enter...")

# Inicia o programa
if __name__ == "__main__":
    exibir_menu() 