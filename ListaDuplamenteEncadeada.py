from Node import Node


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0

    @property
    def cursor(self):
        return self.__cursor

    @property
    def tamanho(self):
        return self.__tamanho

    def acessarAtual(self):
        if self.__cursor is not None:
            return self.__cursor.dados

    def inserirComoPrimeiro(self, novo):
        node = Node(novo)
        if self.__primeiro is not None:
            self.__primeiro.anterior = node
            node.proximo = self.__primeiro
        else:
            self.__ultimo = node
        self.__primeiro = node
        self.__tamanho += 1

    def inserirComoUltimo(self, novo):
        node = Node(novo)
        if self.__ultimo is not None:
            self.__ultimo.proximo = node
            node.anterior = self.__ultimo
        else:
            self.__primeiro = node
        self.__ultimo = node
        self.__tamanho += 1

    def avancarKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.proximo:
                break
            self.__cursor = self.__cursor.proximo

    def retrocederKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.anterior:
                break
            self.__cursor = self.__cursor.anterior

    def irParaPrimeiro(self):
        self.__cursor = self.__primeiro

    def irParaUltimo(self):
        self.__cursor = self.__ultimo

    # MÉTODOS DE EXCLUSÃO

    def excluirAtual(self):
        if self.__tamanho == 0:
            return

        if self.__primeiro is self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
            self.__cursor = None
            self.__tamanho = 0
            return

        if self.__cursor == self.__ultimo:
            self.__cursor = self.__cursor.anterior
            self.__cursor.proximo = None
            self.__ultimo = self.__cursor
            self.__tamanho -= 1
            return

        if self.__cursor == self.__primeiro:
            self.__cursor = self.__cursor.proximo
            self.__cursor.anterior = None
            self.__primeiro = self.__cursor
            self.__tamanho -= 1
            return

        if (self.__cursor.proximo is not None) and (self.__cursor.anterior is not None):
            proximo = self.__cursor.proximo
            self.__cursor = self.__cursor.anterior
            self.__cursor.proximo = proximo
            self.__tamanho -= 1
            return
