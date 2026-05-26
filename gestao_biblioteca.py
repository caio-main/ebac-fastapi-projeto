def principal():
    # Dicionário principal: { "Titulo": {"autor": "Nome", "qtd": 10} }
    biblioteca = {}
    # Lista para armazenar o histórico (Requisito do exercício)
    historico_emprestimos = []

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Remover livro")
        print("4 - Atualizar quantidade de livros")
        print("5 - Registrar empréstimo")
        print("6 - Exibir histórico de empréstimos")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        # 1. Adicionar Livro
        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            autor = input("Nome do autor: ").strip()
            try:
                qtd = int(input("Quantidade de exemplares: "))
                biblioteca[titulo] = {"autor": autor, "qtd": qtd}
                print(f"Livro '{titulo}' adicionado com sucesso!")
            except ValueError:
                print("Erro: Insira um número válido para a quantidade.")

        # 2. Listar Livros (Ordenado alfabeticamente)
        elif opcao == "2":
            if not biblioteca:
                print("A biblioteca está vazia.")
            else:
                print("\nLista de Livros (Ordem Alfabética):")
                # sorted() cria uma lista com as chaves (títulos) em ordem
                for titulo in sorted(biblioteca.keys()):
                    dados = biblioteca[titulo]
                    print(f"{titulo} - {dados['autor']} - {dados['qtd']} exemplares")

        # 3. Remover Livro
        elif opcao == "3":
            titulo = input("Título do livro para remover: ").strip()
            if titulo in biblioteca:
                del biblioteca[titulo]
                print(f"Livro '{titulo}' removido.")
            else:
                print("Erro: Livro não encontrado.")

        # 4. Atualizar Quantidade
        elif opcao == "4":
            titulo = input("Título do livro para atualizar: ").strip()
            if titulo in biblioteca:
                try:
                    nova_qtd = int(input("Nova quantidade de exemplares: "))
                    biblioteca[titulo]["qtd"] = nova_qtd
                    print("Quantidade atualizada com sucesso!")
                except ValueError:
                    print("Erro: Valor inválido.")
            else:
                print("Erro: Livro não encontrado.")

        # 5. Registrar Empréstimo
        elif opcao == "5":
            titulo = input("Título do livro para empréstimo: ").strip()
            if titulo in biblioteca:
                try:
                    qtd_pedida = int(input("Quantidade a ser emprestada: "))
                    if qtd_pedida <= biblioteca[titulo]["qtd"]:
                        biblioteca[titulo]["qtd"] -= qtd_pedida
                        historico_emprestimos.append({"titulo": titulo, "qtd": qtd_pedida})
                        print("Empréstimo realizado com sucesso!")
                    else:
                        print("Erro: Quantidade insuficiente em estoque.")
                except ValueError:
                    print("Erro: Valor inválido.")
            else:
                print("Erro: Livro não encontrado.")

        # 6. Exibir Histórico
        elif opcao == "6":
            if not historico_emprestimos:
                print("Nenhum empréstimo registrado.")
            else:
                print("\nHistórico de Empréstimos:")
                for item in historico_emprestimos:
                    print(f"Livro: {item['titulo']} | Quantidade: {item['qtd']}")

        # 7. Sair
        elif opcao == "7":
            print("Encerrando o sistema da biblioteca. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal() 