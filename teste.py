class Teste:
    def __init__(self):
        # Criar um animal e um cachorro
        self.animal = Animal("Leão", 5)
        self.cachorro = Cachorro("Rex", 3, "Labrador")

    def executar_testes(self):
        # Testar a classe Animal
        print("Testando Animal:")
        print(self.animal)  # Saída: Nome: Leão, Idade: 5, Tipo: Animal
        print(self.animal.fazer_som())  # Saída: Som genérico de animal
        self.animal.set_tipo("Felino")
        print(self.animal.get_tipo())  # Saída: Felino
        self.animal.atualizar_idade(6)
        print(self.animal)  # Saída: Nome: Leão, Idade: 6, Tipo: Felino

        # Testar a classe Cachorro
        print("\nTestando Cachorro:")
        print(self.cachorro)  # Saída: Nome: Rex, Idade: 3, Raça: Labrador, Tipo: Cachorro
        print(self.cachorro.fazer_som())  # Saída: Latido
        print(self.cachorro.brincar())  # Saída: O cachorro está brincando

        # Acessar e modificar atributos
        print("\nAcessando e modificando atributos:")
        print(f"Nome do cachorro: {self.cachorro.nome}")
        print(f"Idade do cachorro: {self.cachorro._idade}")
        print(f"Raça do cachorro: {self.cachorro.raca}")
        print(f"Tipo do cachorro: {self.cachorro._tipo}")

        self.cachorro.raca = "Poodle"
        print(f"Nova raça do cachorro: {self.cachorro.raca}")

# Executar os testes
if __name__ == "__main__":
    teste = Teste()
    teste.executar_testes()


