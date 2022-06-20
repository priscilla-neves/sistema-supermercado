from view.SistemaView import TelaSistema
from controller.UsuariosController import ControladorUsuarios
from controller.ProdutosController import ControladorProdutos
from controller.CategoriaController import ControladorCategoria
from controller.SupermercadoController import ControladorSupermercado

class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_supermercado = ControladorSupermercado(self, self.__controlador_usuarios)
        self.__controlador_categoria = ControladorCategoria(self, self.__controlador_usuarios, self.__controlador_supermercado)
        self.__controlador_produtos = ControladorProdutos(self, self.__controlador_usuarios, self.__controlador_categoria, self.__controlador_supermercado)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_produtos(self):
        self.__controlador_produtos.abre_tela()

    def cadastra_usuarios(self):
        # Chama o controlador de Usuarios
        self.__controlador_usuarios.abre_tela()

    def login(self):
        # Chama o controlador de Usuarios
        self.__controlador_usuarios.verifica_usuario()

    def cadastra_categoria(self):
        self.__controlador_categoria.abre_tela()
        # Chama o controlador de categoria

    def cadastra_supermercado(self):
        self.__controlador_supermercado.abre_tela()
        # Chama o controlador de supermercado

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuarios, 2: self.login}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.cadastra_supermercado, 2: self.cadastra_categoria, 3: self.cadastra_produtos , 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_principal()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()            