class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"O cachorro {self.nome} latiu!")

class Gato(Animal):
    # Sobrescrevendo o método emitir_som
    def emitir_som(self):
        print(f"O gato {self.nome} miou!")

if __name__ == "__main__":
    meu_cachorro = Cachorro(nome="Rex", idade=5)
    meu_gato = Gato(nome="Mingau", idade=3)

    print(f"Dados do Cachorro: {meu_cachorro.nome}, {meu_cachorro.idade} anos.")
    meu_cachorro.emitir_som()

    print("-" * 20)

    print(f"Dados do Gato: {meu_gato.nome}, {meu_gato.idade} anos.")
    meu_gato.emitir_som()