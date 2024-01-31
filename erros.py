"""Este módulo contém funções que imprimem mensagens de erro.
"""

def op_invalida() -> str:
    """Chamada caso a opção escolhida não corresponda a nenhuma alternativa.
    """
    print("\n------------- Opção inválida! -------------")

def n_cadastrado_tente() -> str:
    """Chamada caso o método buscar retorne None 
    e o usuário tem a opção de tentar inserir o ID do produto novamente.
    """
    print("\n---------- Produto não cadastrado! ----------")
    print("Este id não pertence a nenhum produto, tente novamente:")

def n_cadastrado() -> str:
    """Chamada caso o método buscar retorne None.
    """
    print("\n---------- Produto não cadastrado! ----------")

def ja_cadastrado() -> str:
    """Chamado quando o usuário tenta inserir um 
    produto com um id já cadastrado.
    """
    print("\n----------- Produto já cadastrado! -----------")
    print("Este id pertence a outro produto, tente novamente:")

    
    