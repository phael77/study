class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando seu show!")

class Circo:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def apresentacao(self, artista: Artista) -> None:
        print(f"\nO circo {self.nome} está começando a sua apresentação!!!\n")
        artista.apresentar_show()
        print(f"\nO público presente é animal e adorou o show do {artista.tipo}!!!")

circo = Circo("Maximus")

palhaco = Artista("palhaço")
magico = Artista("mágico")
malabarista = Artista("malabarista")

circo.apresentacao(palhaco)