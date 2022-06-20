from model.PessoaFisica import PessoaFisica
from model.PessoaJuridica import PessoaJuridica
from view.UsuarioView import TelaUsuario

class ControladorUsuarios():
  
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.usuario_logado = None
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema

  def pega_usuario_por_documento(self, documento: int):
    for usuario in self.__usuarios:
      if(usuario.documento == documento):
        return usuario
    return None

  def incluir_usuario_pf(self):
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = PessoaFisica(dados_usuario["nome"], dados_usuario["telefone"], dados_usuario["documento"], "CPF", "")
    self.__usuarios.append(usuario)
  
  def incluir_usuario_pj(self):  
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = PessoaJuridica(dados_usuario["nome"], dados_usuario["telefone"], dados_usuario["documento"], "CNPJ", "")
    self.__usuarios.append(usuario)

  def alterar_usuario(self):
    usuario_logado = self.__controlador_usuario.usuario_logado    
    self.lista_usuarios()
    documento_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_documento(documento_usuario)

    if(usuario is not None):
      novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      usuario.nome = novos_dados_usuario["nome"]
      usuario.telefone = novos_dados_usuario["telefone"]
      usuario.documento = novos_dados_usuario["documento"]
      usuario.usuario = usuario_logado
      self.lista_usuarios()
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_usuarios(self):
    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "telefone": usuario.telefone, "documento": usuario.documento, "tipo_documento": usuario.tipo_documento})

  def excluir_usuario(self):
    self.lista_usuarios()
    documento_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_documento(documento_usuario)

    if(usuario is not None):
      self.__usuarios.remove(usuario)
      self.lista_usuarios()
      self.__tela_usuario.mostra_mensagem("Usuario excluído")
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_usuario_pf,2: self.incluir_usuario_pj,  3: self.alterar_usuario, 4: self.lista_usuarios, 5: self.excluir_usuario, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_usuario.tela_opcoes()]()

  def verifica_usuario(self):
    documento_usuario = self.__tela_usuario.verifica_usuario()
    usuario = self.pega_usuario_por_documento(documento_usuario)
    if (usuario == None):
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__tela_usuario.mostra_mensagem("Login Realizado com sucesso!")
      self.usuario_logado = usuario.documento
      self.__controlador_sistema.abre_tela_opcoes()