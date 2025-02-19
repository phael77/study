class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self, nome: str):
        print(f"Eu {nome}, estou acendendo a luz do(a) {self.comodo}")

    def apagar(self, nome: str):
        print(f"Eu {nome}, estou apagando a luz do(a) {self.comodo}")

class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def acender_luz(self, interruptor: Interruptor):
        interruptor.acender(self.nome)

    def apagar_luz(self, interruptor: Interruptor):
        interruptor.apagar(self.nome)

    def dormir(self):
        print("Boa noite!, fui dormir")


Raphael = Pessoa("Raphael")
interruptor_sala = Interruptor("Sala")
interruptor_quarto = Interruptor("Quarto")

Raphael.acender_luz(interruptor_sala)
Raphael.apagar_luz(interruptor_quarto)

James = Pessoa("James")
interruptor_quarto2 = Interruptor("Quarto de hóspedes")
interruptor_sala2 = Interruptor("Sala de estar")
James.acender_luz(interruptor_quarto2)
James.apagar_luz(interruptor_sala2)

