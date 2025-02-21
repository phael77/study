from abc import ABC, abstractmethod

class Pessoa(ABC): #Classe abstrata não possui objetos - só pode ser herdada
#metodos abstratos, mas pelo menos um metodo concreto
    def correr(self):
        print("A pessoa está correndo")

    @abstractmethod #Classe filha DEVE implementar esse método
    def trabalhar(self):
        pass
    
class Professor(Pessoa):
    def trabalhar(self):
        print("O professor está lecionando")

class Lixeiro(Pessoa):
    def trabalhar(self):
        print("O lixeiro está catando o lixo")

p1 = Professor()
p1.correr()
p1.trabalhar()

print()

p2 = Lixeiro()
p2.trabalhar()