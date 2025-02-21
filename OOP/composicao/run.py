class Insert:
    def insert_value(self) -> None:
        print("Inserindo valores no banco de dados")

class Select:
    def by_id(self) -> any:
        print("Selecionando por um elemento no banco de dados")

class Repositorio:
    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self, id: int) -> any:
        self.__select.by_id()

repo = Repositorio()
repo.select_by_id(3)