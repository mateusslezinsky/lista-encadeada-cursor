class Node:
    def __init__(self, dados=None):
        self.dados = dados
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.cursor = None
        self.tamanho = 0

    def acessarAtual(self):
        if self.cursor is not None:
            return self.cursor.dados

    def inserirComoPrimeiro(self, novo):
        node = Node(novo)
        if self.primeiro is not None:
            self.primeiro.anterior = node
            node.proximo = self.primeiro
        else:
            self.ultimo = node
        self.primeiro = node
        self.tamanho += 1

    def inserirComoUltimo(self, novo):
        node = Node(novo)
        if self.ultimo is not None:
            self.ultimo.proximo = node
            node.anterior = self.ultimo
        else:
            self.primeiro = node
        self.ultimo = node
        self.tamanho += 1
