class Automovel:
    def __init__(self, categoria: str, marca: str, modelo: str, rodas: int, motor: str) -> None:
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.motor = motor

    def ligar(self) -> None:
        print(f"O motor {self.motor} do(a) {self.marca} {self.modelo} está ligando...")

    def velocimetro(self, aceleração) -> None:
        km_hora = 0
        print(f"\nO(a) {self.categoria} está andando em {km_hora + aceleração} km/h")

    
class Moto(Automovel):
    def __init__(self, categoria, marca, modelo, rodas, motor):
        super().__init__(categoria, marca, modelo, rodas, motor)

    def ultrapassar(self, acelerar: int):
        acelerar = acelerar
        self.velocimetro(acelerar)
        print(f"Você está ultrapassando o veículo da frente á {acelerar} km/h")


moto_1 = Moto("Motocicleta", "Yamaha", "Fazer 250", 2, "250 cc")

moto_1.ligar()
moto_1.ultrapassar(100)