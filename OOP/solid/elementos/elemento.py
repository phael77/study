from .interfaces.elemento_interface import ElementoInterface

class Elemento(ElementoInterface):
    def executar(self) -> None:
        print("Executando algo!")