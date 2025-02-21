class Pai:
    def pedir(self) -> None:
        print("Filhão faz isso aqui pra mim?")

class Filho(Pai):
    def pedir(self):
        print("Aném pai quero não")

pai = Pai()
filho = Filho()

pai.pedir()
filho.pedir()