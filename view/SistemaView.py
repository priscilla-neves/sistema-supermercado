class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Sistema de Acompanhamento de Preços de Supermercado - Florianópolis ---------")
        print("Escolha sua opcao")
        print("1 - Cadastrar Usuário")
        print("2 - Login ")
        opcao = int(input("Escolha a opcao:"))
        return opcao

    def tela_opcoes_principal(self):
        print("-------- Sistema de Acompanhamento de Preços de Supermercado - Florianópolis ---------")
        print("Escolha sua opcao")
        print("1 - Supermercado")
        print("2 - Categoria")
        print("3 - Produto")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao        