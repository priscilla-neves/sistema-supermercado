from model.Supermercado import Supermercado

class Categoria:
  def __init__(self, supermercado: Supermercado, titulo_categoria: str, codigo: int, usuario: str):
    if (isinstance(supermercado, Supermercado)):
        self.__supermercado = supermercado
    self.__titulo_categoria = titulo_categoria
    self.__codigo = codigo
    self.__usuario = usuario

  @property
  def supermercado(self):
    return self.__supermercado
 
  @supermercado.setter
  def supermercado(self, supermercado: Supermercado):
    if (isinstance(supermercado, Supermercado)):
        self.__supermercado = supermercado

  @property
  def titulo_categoria(self):
    return self.__titulo_categoria

  @titulo_categoria.setter
  def titulo_categoria(self, titulo_categoria: int):
    self.__titulo_categoria = titulo_categoria

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self, codigo):
    self.__codigo = codigo

  @property
  def usuario(self):
      return self.__usuario
  
  @usuario.setter
  def usuario(self, usuario: str):
      self.__usuario = usuario