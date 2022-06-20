
class TelaSupermercado():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- SUPERMERCADO ----------")
    print("Escolha a opcao")
    print("1 - Incluir Supermercado")
    print("2 - Alterar Supermercado")
    print("3 - Listar Supermercado")
    print("4 - Excluir Supermercado")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_supermercado(self):
    print("-------- DADOS SUPERMERCADO ----------")
    estabelecimento = input("Estabelecimento: ")
    endereco = input("Endereco: ")
    return {"estabelecimento": estabelecimento, "endereco": endereco}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_supermercado(self, dados_supermercado):
    print("ESTABELECIMENTO: ", dados_supermercado["estabelecimento"])
    print("ENDEREÇO: ", dados_supermercado["endereco"])
    print("DOCUMENTO USUÁRIO: ", dados_supermercado["usuario"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_supermercado(self):
    estabelecimento = input("Estabelecimento que deseja selecionar: ")
    return estabelecimento

  def mostra_mensagem(self, msg):
    print(msg)