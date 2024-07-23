class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)  # Chama o construtor da classe base
        self.raca = raca                # Atributo público específico da subclasse
        self._tipo = "Cachorro"         # Sobrescreve o atributo protegido da classe base

    def fazer_som(self):
        return "Latido"

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self._idade}, Raça: {self.raca}, Tipo: {self._tipo}"

    # Método específico para a classe Cachorro
    def brincar(self):
        return "O cachorro está brincando"