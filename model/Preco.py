class Preco:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, data: str, valor: str, usuario: str):
    self.__data = data
    self.__valor = valor
    self.__usuario = usuario

  @property
  def data(self):
    return self.__data

  @data.setter
  def data(self, data: str):
    self.__data = data

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self, valor: str):
    self.__valor = valor

  @property
  def usuario(self):
      return self.__usuario
  
  @usuario.setter
  def usuario(self, usuario: str):
      self.__usuario = usuario