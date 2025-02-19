class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def fazer_chamadas(self, numero: str) -> None:
        print(f"\nFazendo uma ligação para o número {numero}...")

    def jogar_frifas(self) -> None:
        print("Abrindo o frifas...")

    def desligar_celular(self):
        print(f"Desligando o celular {self.modelo}")

class Usuario:
    def __init__(self, nome: str, celular: Celular):
        self.nome = nome
        self.__celular = celular

    def fazendo_chamadas(self, numero: str):
        numero_desejado = numero
        self.__celular.fazer_chamadas(numero_desejado)
        print("Deixe seu recado...")

    def diversao(self):
        print("\nQuero jogar um Frifas hehe")
        self.__celular.jogar_frifas()

celular_1 = Celular("Iphone 16")
celular_2 = Celular("Samsung Galaxy S23 Ultra")

Joao = Usuario("João", celular_2)
Maria = Usuario("Maria", celular_1)

Joao.diversao()
Maria.fazendo_chamadas("62 99999-9999")