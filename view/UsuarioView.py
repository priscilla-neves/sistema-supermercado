
class TelaUsuario():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- USUARIOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Usuario Pessoa Física")
    print("2 - Incluir Usuario Pessoa Juridica")
    print("3 - Alterar Usuario")
    print("4 - Listar Usuarios")
    print("5 - Excluir Usuario")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_usuario(self):
    print("-------- DADOS USUARIO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    documento = input("Documento: ")

    return {"nome": nome, "telefone": telefone, "documento": documento}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_usuario(self, dados_usuario):
    print("NOME DO USUARIO: ", dados_usuario["nome"])
    print("FONE DO USUARIO: ", dados_usuario["telefone"])
    print("TIPO DOCUMENTO: ", dados_usuario["tipo_documento"])
    print("DOCUMENTO DO USUARIO: ", dados_usuario["documento"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_usuario(self):
    documento = input("documento do usuario que deseja selecionar: ")
    return documento

  def verifica_usuario(self):
    documento = input("Digite o documento do usuario: ")
    return documento    

  def mostra_mensagem(self, msg):
    print(msg)