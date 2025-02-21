class Produto:
    def __init__(self, nome: str, valor: float):
        self.__nome = nome
        self.__valor = valor

    def info_produto(self) -> None:
        print(f"O produto {self.__nome} está com o preço de {self.__valor}")

class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None: 
        print("\nCompra finalizada. Lista de produtos abaixo")
        print("\n     Produtos\n")
        for product in self.__produtos:
            product.info_produto()


produto1 = Produto("Televisão", 2049.99)
produto2 = Produto("Smartphone", 2999.99)
produto3 = Produto("Notebook", 1999.99)

carrinho = CarrinhoCompras()
carrinho.adicionar_produtos(produto1)
carrinho.adicionar_produtos(produto2)
carrinho.adicionar_produtos(produto3)

carrinho.finalizar_compra()