class Motor:
        def __init__(self, power: int, fuel: str) -> None:
            self.power = power
            self.fuel = fuel

class Car:
    def __init__(self, brand: str, model: str, motor: Motor) -> None:
        self.model = model
        self.motor = motor
        self.brand = brand

    def ligar(self):
        print(f"O carro {self.brand} {self.model} está ligado")
        print(f"O carro {self.brand} {self.model} tem um motor de {self.motor.power} cavalos de potência e é movido a {self.motor.fuel}")


motor_1 = Motor(200, "Gasolina")

car_1 = Car("Volkswagen", "Fusca", motor_1)

car_1.ligar()
