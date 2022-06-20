class TelaCategoria():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CATEGORIA ----------")
    print("Escolha a opcao")
    print("1 - Incluir Categoria")
    print("2 - Listar Categoria")
    print("3 - Alterar Categoria")
    print("4 - Excluir Categoria")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_categoria(self):
    print("-------- DADOS CATEGORIA ----------")
    supermercado = input("Supermercado: ")
    categoria = input("Categoria: ")

    return {"supermercado": supermercado, "categoria": categoria}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    print("CODIGO: ", dados_categoria["codigo"])
    print("CATEGORIA: ", dados_categoria["categoria"])
    print("SUPERMERCADO: ", dados_categoria["supermercado"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    categoria = input("Categoria que deseja selecionar: ")
    return categoria

  def mostra_mensagem(self, msg):
    print(msg)