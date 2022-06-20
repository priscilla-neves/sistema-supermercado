from model.Categoria import Categoria
from model.Qualificador import Qualificador
from model.Preco import Preco
from model.Supermercado import Supermercado

class Produto:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, supermercado: Supermercado, categoria: Categoria, nome: str, descricao: str, usuario: str, qualificador: Qualificador, preco: Preco):
    if (isinstance(supermercado, Supermercado)):    
      self.__supermercado = supermercado         
    if (isinstance(categoria, Categoria)):    
      self.__categoria = categoria    
    self.__nome = nome
    self.__descricao = descricao
    self.__usuario = usuario
    if (isinstance(qualificador, Qualificador)):        
      self.__qualificador = qualificador
    if (isinstance(preco, Preco)):        
      self.__preco = preco

  @property
  def supermercado(self):
    return self.__supermercado
 
  @supermercado.setter
  def supermercado(self, supermercado: Supermercado):
    if (isinstance(supermercado, Supermercado)):
        self.__supermercado = supermercado     

  @property
  def categoria(self):
    return self.__categoria
 
  @categoria.setter
  def categoria(self, categoria: Categoria):
    if (isinstance(categoria, Categoria)):
        self.__categoria = categoria

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

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

  @property
  def qualificador(self):
    return self.__qualificador
 
  @qualificador.setter
  def qualificador(self, qualificador: Qualificador):
    if (isinstance(qualificador, Qualificador)):
        self.__qualificador = qualificador

  @property
  def preco(self):
    return self.__preco
 
  @preco.setter
  def preco(self, preco: Preco):
    if (isinstance(preco, Preco)):
        self.__preco = preco