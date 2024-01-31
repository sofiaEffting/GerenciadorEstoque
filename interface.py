"""Este módulo cria uma interface gráfica para o usuário."""

from produtodao import ProdutoDao
from produto import Produto
import erros

class Interface(object):
    'Representa a interface com o usuário.'

    def __init__(self):
        self.e = ProdutoDao()

    def inserir(self):
        """Recebe os dados e insere um novo produto.
        """
        while True:
            try:
                id = int(input("ID:"))
                desc = str(input("Descrição do produto:"))
                qtde = str(input("Quantidade em estoque:"))
                preco = float(input("Preço de venda:"))
                while True:
                    prod = Produto(id, desc, qtde, preco)
                    if self.e.buscar(prod.id) is None:
                        self.e.inserir_produto(prod)
                        break
                    else:
                        erros.ja_cadastrado()
                        try:
                            id = int(input("ID:"))
                        except ValueError:
                            print("O ID deve ser um número inteiro!")
                break
            except ValueError as err:
                print("------------------------------------------------")
                print("ValueError: {0}".format(err))
                print("Tipo de dado inválido, tente novamente:")
            
    def remover(self):
        """Através do ID busca o produto e o remove.
        """
        while True:
            try:
                id = int(input("ID do produto:"))
                if self.e.buscar(id) is not None:
                    self.e.__repr__(id)
                    aux = input("Deseja excluir? [s/n]: ").upper()
                    if aux == 'S':
                        self.e.remover_produto(id)
                        break
                    elif aux == 'N':
                        b = input("Deseja escolher outro produto? [s/n]: ").upper()
                        if b == 'N':
                            break
                        elif b == 'S':
                            pass
                        else: 
                            erros.op_invalida()
                    else:
                        erros.op_invalida()
                else:
                    erros.n_cadastrado_tente()
            except ValueError:
                erros.op_invalida()

    def buscar (self):
        """Recebe o Id e caso ele esteja no banco o imprime.
        """
        while True:
            id = int(input("ID do produto:"))
            i = self.e.buscar(id)
            if i is None:
                erros.n_cadastrado_tente()
            else:
                print("___________________________________________________________\n")
                self.e.__repr__(id)
                print("___________________________________________________________")
                break

    def exibir (self):
        """Exibe todos os registros do banco de dados.
        """
        print("________________________________________________________")
        print("Valores no banco de dados:\n")
        self.e.exibir()
        print("________________________________________________________")

    def alterar_preco (self):
        """Busca e altera preço de um produto caso estaja cadastrado.
        """
        while True:
            try:
                id = int(input("ID do produto:"))
                if self.e.buscar(id) is not None:
                    self.e.__repr__(id)
                    aux = input("Deseja alterar o preço? [s/n]: ").upper()
                    if aux == 'S':
                        preco_novo = float(input("Preço novo:"))
                        if self.e.alterar_preco(id, preco_novo):
                            print("________________________________________________")
                            print("\nPreço alterado com sucesso!")
                            print("________________________________________________")
                        break
                    elif aux == 'N':
                        b = input("Deseja escolher outro produto? [s/n]: ").upper()
                        if b == 'N':
                            break
                        elif b == 'S':
                            pass
                        else: 
                            erros.op_invalida()
                    else:
                        erros.op_invalida()
                else:
                    erros.n_cadastrado_tente()
            except ValueError:
                    erros.op_invalida()
            
    def alterar_qtde(self):
        """Busca e altera preço de um produto caso estaja cadastrado.
        """
        while True:
            try:
                id = int(input("ID do produto:"))
                if self.e.buscar(id) is not None:
                    self.e.__repr__(id)
                    aux = input("Deseja alterar a quantidade em estoque? [s/n]: ").upper()
                    if aux == 'S':
                        qtde_nova = str(input("Quantidade nova:"))
                        x = self.e.alterar_qtde(id, qtde_nova)
                        if x:
                            print("________________________________________________")
                            print("\nQuantidade alterada com sucesso!")
                            print("________________________________________________")
                        break
                    elif aux == 'N':
                        b = input("Deseja escolher outro produto? [s/n]: ").upper()
                        if b == 'N':
                            break
                        elif b == 'S':
                            pass
                        else: 
                            erros.op_invalida()
                    else:
                        erros.op_invalida()
                else:
                    erros.n_cadastrado_tente()
            except ValueError:
                    erros.op_invalida()

    def imprimir_menu(self):
        """Imprime o menu de opções do programa.
        """
        print("\n+-------------------Menu------------------+")
        print("|        1- Cadastrar Produto             |")
        print("|        2- Remover Produto               |")
        print("|        3- Buscar Produto                |")
        print("|        4- Exibir Tabela                 |")
        print("|        5- Alterar Preço                 |")
        print("|        6- Alterar Quantidade            |")
        print("|        7- Sair                          |")
        print("+-----------------------------------------+")

    def main(self):
        """Recebe a opção do usuário e chama a função correspondente.
        """
        sair = False
        while not sair:
            try:
                self.imprimir_menu()
                print("\n------------------------------------------------")
                opcao = int(input("O que você deseja fazer: "))
                if opcao == 1:
                    self.inserir()
                elif opcao == 2:
                    self.remover()
                elif opcao == 3:
                    self.buscar()
                elif opcao == 4:
                    self.exibir()
                elif opcao == 5:
                    self.alterar_preco()
                elif opcao == 6:
                    self.alterar_qtde()
                elif opcao == 7:
                    sair = True
                else:
                    raise ValueError
            except ValueError:
                erros.op_invalida()

if __name__ == '__main__':
    app = Interface()
    e = ProdutoDao()
    e.criar_tabela()
    app.main()