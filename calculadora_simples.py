def principal():
    operacoes = {
        "1": lambda x, y: x + y,
        "2": lambda x, y: x - y,
        "3": lambda x, y: x * y,
        "4": lambda x, y: x / y
    }

    nomes_operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

    while True:
        try:
            num1 = float(input("\nInsira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
        except ValueError:
            print("Erro: Por favor, insira apenas valores numéricos.")
            continue

        print("\nEscolha uma operação:")
        menu = [f"{i+1} - {nome}" for i, nome in enumerate(nomes_operacoes)]
        for opcao in menu:
            print(opcao)

        escolha = input("Opção escolhida: ").strip()

        if escolha not in operacoes:
            print("Erro: Operação inválida.")
            continue

        if escolha == "4":
            while num2 == 0:
                try:
                    num2 = float(input("Divisão por zero não é permitida. Por favor, insira outro número: "))
                except ValueError:
                    print("Erro: Insira um número válido.")

        resultado = operacoes[escolha](num1, num2)
        print(f"O resultado é: {resultado}")

        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    principal()