class TelaProduto():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- PRODUTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Produto")
    print("2 - Alterar Produto")
    print("3 - Listar Produto")
    print("4 - Excluir Produto")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_produto(self):
    print("-------- DADOS PRODUTO ----------")
    supermercado = input("Nome do Supermercado: ")
    nome = input("Nome do Produto: ")
    descricao = input("Descricao: ")
    categoria = input("Categoria: ")

    return {"supermercado": supermercado, "nome": nome, "descricao": descricao, "categoria": categoria}

  def pega_dados_qualificador(self):
    print("-------- DADOS QUALIFICADOR ----------")
    titulo = input("Nome Qualificador: ")
    descricao = input("Descricao Qualificador: ")

    return {"titulo": titulo, "descricao": descricao}    

  def pega_dados_preco(self):
    print("-------- DADOS PREÇO ----------")
    data = input("Data da postagem do Preço: ")
    valor = input("Valor: ")

    return {"data": data, "valor": valor}        

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_produto(self, dados_produto):
    print("NOME DO SUPERMERCADO: ", dados_produto["supermercado"])
    print("NOME DO PRODUTO: ", dados_produto["nome"])
    print("DESCRIÇÃO DO PRODUTO: ", dados_produto["descricao"])
    print("CATEGORIA DO PRODUTO: ", dados_produto["categoria_titulo"])
    print("TITULO DO QUALIFICADOR DO PRODUTO: ", dados_produto["qualificador_titulo"])
    print("DESCRIÇÃO QUALIFICADOR DO PRODUTO: ", dados_produto["qualificador_descricao"])
    print("PRECO DO PRODUTO: ", dados_produto["preco_valor"])
    print("DATA DE POSTAGEM DO PRECO DO PRODUTO: ", dados_produto["preco_data"])
    print("USUARIO: ", dados_produto["usuario"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_produto(self):
    nome = input("Nome do produto que deseja selecionar: ")
    return nome

  def mostra_mensagem(self, msg):
    print(msg)