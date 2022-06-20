from view.CategoriaView import TelaCategoria
from model.Categoria import Categoria

from random import randint


# Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
class ControladorCategoria():

  def __init__(self, controlador_sistema, controlador_usuario, controlador_supermercado):
    self.__controlador_sistema = controlador_sistema
    self.__categoria = []
    self.__tela_categoria = TelaCategoria()
    self.__controlador_usuario = controlador_usuario
    self.__controlador_supermercado = controlador_supermercado

  def pega_categoria_por_titulo(self, titulo_categoria: int):
    for categoria in self.__categoria:
      if(categoria.titulo_categoria == titulo_categoria):
        return categoria
    return None

  def incluir_categoria(self):
    usuario_logado = self.__controlador_usuario.usuario_logado    
    self.__controlador_supermercado.lista_supermercado()
    supermercado = None
    while (supermercado is None):
      print("Insira o nome de um dos supermercados cadastrados na lista acima")    
      dados_categoria = self.__tela_categoria.pega_dados_categoria()    
      supermercado = self.__controlador_supermercado.pega_supermercado_por_estabelecimento(dados_categoria["supermercado"])

    categoria = Categoria(supermercado, dados_categoria["categoria"], randint(0, 100), usuario_logado)
    self.__categoria.append(categoria)

  def alterar_categoria(self):
    usuario_logado = self.__controlador_usuario.usuario_logado    
    self.lista_categoria()
    categoria_ident = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria_por_titulo(categoria_ident)

    if(categoria is not None):
      novos_dados_categoria = self.__tela_categoria.pega_dados_categoria()
      categoria.supermercado = novos_dados_categoria["supermercado"]
      categoria.titulo_categoria = novos_dados_categoria["categoria"]
      categoria.usuario = usuario_logado
      self.lista_categoria()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")    

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_categoria(self):
    for e in self.__categoria:
      self.__tela_categoria.mostra_categoria({"categoria": e.titulo_categoria,
                                                "codigo": e.codigo,
                                                "supermercado": e.supermercado.estabelecimento,
                                                "usuario": e.usuario})
                                                

  def excluir_categoria(self):
    self.lista_categoria()
    titulo_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria_por_titulo(titulo_categoria)

    if (categoria is not None):
      self.__categoria.remove(categoria)
      self.lista_categoria()
      self.__tela_categoria.mostra_mensagem("Categoria excluída")
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_categoria, 2: self.lista_categoria, 3: self.alterar_categoria, 4: self.excluir_categoria, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_categoria.tela_opcoes()]()
