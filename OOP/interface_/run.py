from abc import ABC, abstractmethod

class Trabalhador(ABC): #Interface

    @abstractmethod
    def trabalhar(self) -> None:
        pass

    @abstractmethod
    def bater_ponto(self) -> None:
        pass

    @abstractmethod
    def almocar(self) -> None:
        pass

    @abstractmethod
    def volta_casa(self) -> None:
        pass

class Repositor(Trabalhador):
    def __init__(self, nome: str, mercado: str):
        self.nome = nome
        self.mercado = mercado

    def trabalhar(self):
        print(f"O repositor {self.nome} está trabalhando no mercado {self.mercado}!")

    def bater_ponto(self):
        print(f"O repositor {self.nome} bateu o ponto.")
    
    def almocar(self):
        print(f"Hora do almoco do {self.nome}")

    def volta_casa(self):
        print(f"Finalmente {self.nome} está indo pra casa!!!")

zezin = Repositor("Zezin", "Costa Atacadão")

zezin.trabalhar()
zezin.bater_ponto()
zezin.almocar()
zezin.volta_casa()