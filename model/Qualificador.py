class Qualificador:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, titulo: str, descricao: str, usuario: str):
    self.__titulo = titulo
    self.__descricao = descricao
    self.__usuario = usuario

  @property
  def titulo(self):
    return self.__titulo

  @titulo.setter
  def titulo(self, titulo: str):
    self.__titulo = titulo

  @property
  def descricao(self):
    return self.__descricao

  @descricao.setter
  def descricao(self, descricao: str):
    self.__descricao = descricao

  @property
  def usuario(self):
      return self.__usuario
  
  @usuario.setter
  def usuario(self, usuario: str):
      self.__usuario = usuario