class Produto (object):
    """Representa um objeto Produto.
    """

    def __init__(self, id: int, descricao: str, qtde: str, preco: float) -> None:
        self.id = id
        self.descricao = descricao
        self.qtde = qtde
        self.preco = preco
