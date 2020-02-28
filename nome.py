from functools import total_ordering

@total_ordering
class Tipo_Telefone:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return '({0})' .format(self.tipo)
    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo
    def __lt__(self, outro):
        return self.tipo < outro.tipo

class Telefone:
    def __init__(self, numero, tipo = None):
        self.numero = numero
        self.tipo = tipo
    def __str__(self):
        if self.tipo != None:
            tipo = self.tipo
        else:
            tipo = ''
        return '{0} {1}' .format(self.numero, tipo)
    def __eq__(self, outro):
        return self.numero ==outro.numero and ((self.tipo == outro.tipo) or (self.tipo == None or outro.tipo == None))

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__numero = valor




@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>" .format(id(self), self.nome, self.chave, type(self).__name__)
    def __eq__(self, outro):
        return self.nome == outro.nome
    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return  self.__nome
    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.Cria_chave(valor)
    @property
    def chave(self):
        return self.__chave
    @staticmethod
    def Cria_chave(nome):
        return nome.strip().lower()
