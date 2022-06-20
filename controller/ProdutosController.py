from view.ProdutoView import TelaProduto
from model.Produto import Produto
from model.Qualificador import Qualificador
from model.Preco import Preco

class ControladorProdutos():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema, controlador_usuario, controlador_categoria, controlador_supermercado):
    self.__produtos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_produto = TelaProduto()
    self.__controlador_usuario = controlador_usuario
    self.__controlador_categoria = controlador_categoria
    self.__controlador_supermercado = controlador_supermercado

  def pega_produto_por_nome(self, nome: str):
    for produto in self.__produtos:
      if(produto.nome == nome):
        return produto
    return None

  def incluir_produto(self):
    usuario_logado = self.__controlador_usuario.usuario_logado
    
    #Lista Supermercados
    self.__controlador_supermercado.lista_supermercado()
    # Lista de categorias
    self.__controlador_categoria.lista_categoria()

    dados_produto = self.__tela_produto.pega_dados_produto()

    supermercado = self.__controlador_supermercado.pega_supermercado_por_estabelecimento(dados_produto["supermercado"])
    while (supermercado is None):
      print("Insira o nome de um dos supermercados cadastrados na lista acima")   
      dados_produto = self.__tela_produto.pega_dados_produto()   
      supermercado = self.__controlador_supermercado.pega_supermercado_por_estabelecimento(dados_produto["supermercado"])

    categoria = self.__controlador_categoria.pega_categoria_por_titulo(dados_produto["categoria"])
    while (categoria is None):  
      print("Insira o nome de um das categorias cadastrados na lista acima")   
      dados_produto = self.__tela_produto.pega_dados_produto() 
      categoria = self.__controlador_categoria.pega_categoria_por_titulo(dados_produto["categoria"])
    
    dados_qualificador = self.__tela_produto.pega_dados_qualificador()
    qualificador = Qualificador(dados_qualificador["titulo"], dados_qualificador["descricao"], usuario_logado)

    dados_preco = self.__tela_produto.pega_dados_preco()
    preco = Preco(dados_preco["data"], dados_preco["valor"], usuario_logado)

    produto = Produto(supermercado, categoria, dados_produto["nome"], dados_produto["descricao"], usuario_logado, qualificador, preco)
    self.__produtos.append(produto)

  def alterar_produto(self):
    usuario_logado = self.__controlador_usuario.usuario_logado       
    self.lista_produto()
    nome_produto = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_por_nome(nome_produto)

    if(produto is not None):
      novos_dados_produto = self.__tela_produto.pega_dados_produto()

      supermercado = self.__controlador_supermercado.pega_supermercado_por_estabelecimento(novos_dados_produto["supermercado"])
      while (supermercado is None):
        print("Insira o nome de um dos supermercados cadastrados na lista acima")   
        novos_dados_produto = self.__tela_produto.pega_dados_produto()   
        supermercado = self.__controlador_supermercado.pega_supermercado_por_estabelecimento(novos_dados_produto["supermercado"])

      categoria = self.__controlador_categoria.pega_categoria_por_titulo(novos_dados_produto["categoria"])
      while (categoria is None):  
        print("Insira o nome de um das categorias cadastrados na lista acima")   
        novos_dados_produto = self.__tela_produto.pega_dados_produto() 
        categoria = self.__controlador_categoria.pega_categoria_por_titulo(novos_dados_produto["categoria"])
      
      dados_qualificador = self.__tela_produto.pega_dados_qualificador()
      qualificador = Qualificador(dados_qualificador["titulo"], dados_qualificador["descricao"], usuario_logado)

      dados_preco = self.__tela_produto.pega_dados_preco()
      preco = Preco(dados_preco["data"], dados_preco["valor"], usuario_logado)    

      produto.nome = novos_dados_produto["nome"]
      produto.descricao = novos_dados_produto["descricao"]
      produto.categoria = categoria
      produto.qualificador = qualificador
      produto.preco = preco
      produto.supermercado = supermercado
      produto.usuario = usuario_logado
      self.lista_produto()
    else:
      self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_produto(self):
    for produto in self.__produtos:
      self.__tela_produto.mostra_produto({"nome": produto.nome, "descricao": produto.descricao, "usuario": produto.usuario, "categoria_titulo": produto.categoria.titulo_categoria, "qualificador_titulo": produto.qualificador.titulo, "qualificador_descricao": produto.qualificador.descricao, "preco_data": produto.preco.data, "preco_valor": produto.preco.valor, "supermercado": produto.supermercado.estabelecimento})

  def excluir_produto(self):
    self.lista_produto()
    nome_produto = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_por_nome(nome_produto)

    if(produto is not None):
      self.__produtos.remove(produto)
      self.lista_produto()
      self.__tela_produto.mostra_mensagem("Produto excluído")
    else:
      self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_produto, 2: self.alterar_produto, 3: self.lista_produto, 4: self.excluir_produto, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_produto.tela_opcoes()]()