
class Usuario:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, telefone: str, documento: int, tipo_documento: str, usuario: str):
    #if isinstance(nome, str):    
      self.__nome = nome
    #if isinstance(telefone, str):  
      self.__telefone = telefone
      self.__documento = documento
      self.__tipo_documento =tipo_documento
      self.__usuario = usuario

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone: str):
    self.__telefone = telefone

  @property
  def documento(self):
    return self.__documento

  @documento.setter
  def documento(self, documento: int):
    self.__documento = documento

  @property
  def tipo_documento(self):
    return self.__tipo_documento

  @tipo_documento.setter
  def tipo_documento(self, tipo_documento: str):
    self.__tipo_documento = tipo_documento

  @property
  def usuario(self):
      return self.__usuario
  
  @usuario.setter
  def usuario(self, usuario: str):
      self.__usuario = usuario