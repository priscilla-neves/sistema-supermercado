class Supermercado:
    
    def __init__(self, estabelecimento: str, endereco: str, usuario: str):
        self.__estabelecimento = estabelecimento
        self.__endereco = endereco
        self.__usuario = usuario
        
    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @estabelecimento.setter
    def estabelecimento(self, estabelecimento: str):
        self.__estabelecimento = estabelecimento

    @property
    def endereco(self):
        return self.__endereco
   
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco
      
    @property
    def endereco(self):
        return self.__endereco
   
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def usuario(self):
        return self.__usuario
   
    @usuario.setter
    def usuario(self, usuario: str):
        self.__usuario = usuario