from model.Usuario import Usuario

class PessoaJuridica(Usuario):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, telefone: str,  documento: int, tipo_documento: str, usuario: str):
    super().__init__(nome, telefone,  documento, tipo_documento, usuario)
