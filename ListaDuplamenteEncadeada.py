# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva

from Node import Node


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0
        self.__tamanho_max = 0

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def cursor(self):
        return self.__cursor

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def tamanho_max(self):
        return self.__tamanho_max

    @tamanho_max.setter
    def tamanho_max(self, tamanho_max):
        self.__tamanho_max = tamanho_max

    def acessarAtual(self):
        if self.__cursor is not None:
            return self.__cursor.dados

    def inserirAntesDoAtual(self, elemento):
        # Se cursor está definido
        if self.__cursor is not None:
            # Instancia a classe do elemento
            node = Node(elemento)
            # Tem anterior?
            if self.__cursor.anterior is not None:
                # Antes de se adicionar, o cursor tem um elemento anterior já existente. O próximo dele deve ser o novo a adicionar
                self.__cursor.anterior.proximo = node
                # O anterior do elemento novo deve ser o antigo anterior do cursor
                node.anterior = self.__cursor.anterior
            else:
                # Caso não tenha anterior, será o primeiro elemento
                self.__primeiro = node
            # O próximo é o atual
            node.proximo = self.__cursor
            # O anterior do atual é o inserido
            self.__cursor.anterior = node
            # Aumenta o tamanho da lista
            self.__tamanho += 1

    def inserirAposAtual(self, elemento):
        # Se cursor está definido
        if self.__cursor is not None:
            # Instancia a classe do elemento
            node = Node(elemento)
            # Tem próximo?
            if self.__cursor.proximo is not None:
                # Antes de se adicionar, o cursor tem um elemento próximo já existente. O anterior dele deve ser o novo a adicionar
                self.__cursor.proximo.anterior = node
                # O próximo do elemento novo deve ser o antigo próximo do cursor
                node.proximo = self.__cursor.proximo
            else:
                # Caso não tenha próximo, será o último elemento
                self.__ultimo = node
            # O anterior é o atual
            node.anterior = self.__cursor
            # O próximo do atual é o inserido
            self.__cursor.proximo = node
            # Aumenta o tamanho da lista
            self.__tamanho += 1

    def inserirNaPosicao(self, k, novo):
        if k < 1 or k >= self.__tamanho - 1:
            raise ValueError("Posição inválida")
        elif k == 1:
            self.inserirAposAtual(novo)
        else:
            node = Node(novo)
            atual = self.__cursor
            for i in range(1, k):
                atual = atual.proximo
            node.anterior = atual
            node.proximo = atual.proximo
            atual.proximo.anterior = node
            atual.proximo = node
            self.__tamanho += 1

    def inserirComoPrimeiro(self, elemento):
        node = Node(elemento)
        if self.__primeiro is not None:
            self.__primeiro.anterior = node
            node.proximo = self.__primeiro
        else:
            self.__ultimo = node
        self.__primeiro = node
        self.__tamanho += 1

    def inserirComoUltimo(self, elemento):
        node = Node(elemento)
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

    def vazia(self):
        # Se o tamanho for igual a 0, está vazia.
        if self.__tamanho == 0:
            return True
        else:
            return False

    def cheia(self):
        # Se o tamanho for igual ao tamanho máximo, está cheia.
        if self.__tamanho == self.__tamanho_max:
            return True
        else:
            return False

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
