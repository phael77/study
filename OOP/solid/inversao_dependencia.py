from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2
from elementos.interfaces.elemento_interface import ElementoInterface   

class Principal:
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print("Estou na classe principal!")
        

elem = Elemento()
elem2 = Elemento2()

cl1 = Principal(elem)
cl1.run()
print()
cl2 = Principal(elem2)
cl2.run()