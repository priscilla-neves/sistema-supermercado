from view.SupermercadoView import TelaSupermercado
from view.UsuarioView import TelaUsuario
from model.Supermercado import Supermercado

class ControladorSupermercado():

  def __init__(self, controlador_sistema, controlador_usuario):
    self.__supermercado = []
    self.__tela_supermercado = TelaSupermercado()
    self.__controlador_sistema = controlador_sistema
    self.__controlador_usuario = controlador_usuario

  def pega_supermercado_por_estabelecimento(self, estabelecimento: str):
    for supermercado in self.__supermercado:
      if(supermercado.estabelecimento == estabelecimento):
        return supermercado
    return None

  def incluir_supermercado(self):
    usuario_logado = self.__controlador_usuario.usuario_logado
    dados_supermercado = self.__tela_supermercado.pega_dados_supermercado()
    supermercado = Supermercado(dados_supermercado["estabelecimento"], dados_supermercado["endereco"], usuario_logado)
    self.__supermercado.append(supermercado)

  def alterar_supermercado(self):
    usuario_logado = self.__controlador_usuario.usuario_logado    
    self.lista_supermercado()
    estabelecimento_supermercado = self.__tela_supermercado.seleciona_supermercado()
    supermercado = self.pega_supermercado_por_estabelecimento(estabelecimento_supermercado)

    if(supermercado is not None):
      novos_dados_supermercado = self.__tela_supermercado.pega_dados_supermercado()
      supermercado.estabelecimento = novos_dados_supermercado["estabelecimento"]
      supermercado.endereco = novos_dados_supermercado["endereco"]
      supermercado.usuario = usuario_logado
      self.lista_supermercado()
    else:
      self.__tela_supermercado.mostra_mensagem("ATENCAO: Supermercado não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_supermercado(self):
    for supermercado in self.__supermercado:
      self.__tela_supermercado.mostra_supermercado({"estabelecimento": supermercado.estabelecimento, "endereco": supermercado.endereco, "usuario": supermercado.usuario})

  def excluir_supermercado(self):
    self.lista_supermercado()
    estabelecimento_supermercado = self.__tela_supermercado.seleciona_supermercado()
    supermercado = self.pega_supermercado_por_estabelecimento(estabelecimento_supermercado)

    if(supermercado is not None):
      self.__supermercado.remove(supermercado)
      self.lista_supermercado()
      self.__tela_supermercado.mostra_mensagem("Supermercado excluído")
    else:
      self.__tela_supermercado.mostra_mensagem("ATENCAO: Supermercado não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_supermercado, 2: self.alterar_supermercado, 3: self.lista_supermercado, 4: self.excluir_supermercado, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_supermercado.tela_opcoes()]()