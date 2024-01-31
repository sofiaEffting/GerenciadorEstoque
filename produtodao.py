"""Este módulo faz o gerenciamento da tabela produto.
"""

import sqlite3
from produto import Produto
from config import db_path

class ProdutoDao(object):
    """Gerenciador da tabela produto.
    """

    def __init__(self) -> None:
        self.con = None

    def conectar (self) -> None:
        """Caso ainda não esteja conectado, conecta ao banco de dados.
        """
        if self.con is None:
            self.con = sqlite3.connect(db_path)

    def desconectar (self) -> None:
        """Caso estaja conectado, desconecta o 
        banco de dados e confirma as alterações DML.
        """
        if self.con is not None:
            self.con.commit()
            self.con.close()
            self.con = None

    def criar_tabela (self):
        """Caso não exista, cria a tabela produtos que 
        contém id, descricao, quantidade e preço.
        """
        self.conectar()
        if self.con.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
            id int PRIMARY KEY not null,
            descricao varchar not null,
            qtde varchar not null,
            preco real not null);
            """):
            return True
        self.desconectar()

    def inserir_produto (self, p: Produto) -> None:
        """Adiciona um registro na tabela produtos.

        Args:
            p (Produto): Produto a ser inserido.
        """
        self.conectar()
        dados = (p.id, p.descricao, p.qtde, p.preco)
        a = self.con.execute("INSERT INTO produtos (id, descricao, qtde, preco) "\
                    "VALUES (?, ?, ?, ?)", dados)
        print("------------------------------------------------")
        print(a.rowcount, "registro foi inserido:", dados)
        print("------------------------------------------------")
        self.desconectar()

    def buscar (self, id: int):
        """Busca um produto pelo seu ID.

        Args:
            id (int): ID do produto.

        Returns:
            tuple: Dados do produto.
        """
        self.conectar()
        self.produto = self.con.execute('select * from produtos where id = ?', 
                                (id, )).fetchone()
        self.desconectar()
        return self.produto

    def remover_produto (self, id: int) -> None:
        """Remove um registro da tabela produtos.

        Args:
            id (int): Id do produto a ser removido.
        """
        self.conectar()
        a = self.con.execute("DELETE FROM produtos WHERE id = ?", (id,))
        print("------------------------------------------------")   
        print(a.rowcount, "registro foi removido:", self.produto)
        print("------------------------------------------------")
        self.desconectar()

    def alterar_preco (self, id: int, preco: float):
        """Altera o preço de um registro da tabela produtos.

        Args:
            id (int): Id do produto a ser alterado.
            preco (float): Preço novo.

        Returns:
            bool: True se a alteração for bem sucedida.
        """
        self.conectar()
        if self.con.execute("UPDATE produtos SET preco = ? where id = ?;", 
                        (preco, id)):
            return True
        self.desconectar()
        
    def alterar_qtde (self, id: int, qtde: str):
        """Altera a quaantidade de um registro da tabela produtos.

        Args:
            id (int): Id do produto.
            qtde (str): Nova quantidade.

        Returns:
            bool: True se a alteração for bem sucedida.
        """
        self.conectar()
        if self.con.execute("UPDATE produtos SET qtde = ? where id = ?;", 
                        (qtde, id)):
            return True
        self.desconectar()

    def exibir(self):
        """Exibe todos os registros da tabela produtos.
        """
        self.conectar()
        result = self.con.execute("select * from produtos order by id asc").fetchall()
        for i in result:
            self.__repr__(i[0])
        self.desconectar()

    def __repr__(self, id: int):
        """Coverte para string um produto.

        Args:
            id (int): Id do produto a ser impresso.
        """
        p = self.buscar(id)
        result = ('| ID: {} | Descrição: {} | Quantidade: {} | Valor: {} |'.format(p[0], p[1], p[2], p[3]))
        print (result)
