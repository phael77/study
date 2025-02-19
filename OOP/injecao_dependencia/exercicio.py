class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_banco(self) -> None:
        self.connection = True

class RepositorioBancoDeDados:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        return None
    
class RegraDeNegocio:
    def __init__(self, repo: RepositorioBancoDeDados) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        try:
            soma = sum(dados)
            print(f"A soma dos dados é igual á: {soma}")
        except:
            print("Erro na busca de dados!!! Por favor verifique novamente sua conexão")

connector = ConectorBancoDeDados()
connector.conectar_banco()

repo = RepositorioBancoDeDados(connector)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()