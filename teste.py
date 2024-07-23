class Animal:
    def __init__(self, nome, idade):
        self.nome = nome            # Atributo público
        self._idade = idade         # Atributo protegido
        self.__tipo = "Animal"      # Atributo privado

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def fazer_som(self):
        return "Som genérico de animal"

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self._idade}, Tipo: {self.__tipo}"

    def atualizar_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade não pode ser negativa")
