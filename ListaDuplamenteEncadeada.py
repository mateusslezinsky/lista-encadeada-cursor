from Node import Node


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0

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

    def avancarCursor(self, posicoes):
        for i in range(posicoes):
            self.__cursor = self.__cursor.proximo
        return self.__cursor
