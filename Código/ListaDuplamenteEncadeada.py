# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva - 22102556

from Node import Node


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self):
        return self.__ultimo

    @property
    def cursor(self):
        return self.__cursor

    @property
    def tamanho(self):
        return self.__tamanho

    def _acessarAtual(self):
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

    def _avancarKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.proximo:
                break
            self.__cursor = self.__cursor.proximo

    def _retrocederKPosicoes(self, k):
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.anterior:
                break
            self.__cursor = self.__cursor.anterior

    def _irParaPrimeiro(self):
        self.__cursor = self.__primeiro

    def _irParaUltimo(self):
        self.__cursor = self.__ultimo

    def vazia(self):
        # Se o tamanho for igual a 0, está vazia.
        if self.__tamanho == 0:
            return True
        else:
            return False

    # MÉTODOS DE EXCLUSÃO

    # Este método fará a avaliação da posição do elemento na lista, aplicando o tratamento necessário caso esteja nas
    # extremidades ou no meio da lista. Ele utiliza outros métodos da classe para aumentar a reutilização de código
    def excluirAtual(self):
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.reset()
            return

        if self.__cursor == self.__ultimo:
            self.excluirUltimo()
            return

        if self.__cursor == self.__primeiro:
            self.excluirPrimeiro()
            return

        if (self.__cursor.proximo is not None) and (self.__cursor.anterior is not None):
            proximo = self.__cursor.proximo
            anterior = self.__cursor.anterior
            self.__cursor = self.__cursor.anterior
            self.__cursor.proximo = proximo
            self._avancarKPosicoes(1)
            self.__cursor.anterior = anterior
            self.__tamanho -= 1
            return

    def excluirPrimeiro(self):
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.resetList()
            return
        else:
            if self.__cursor == self.__primeiro:
                self._avancarKPosicoes(1)
            self.__primeiro = self.__primeiro.proximo
            self.__primeiro.anterior = None
            self.__tamanho -= 1
            return

    def excluirUltimo(self):
        if self.vazia():
            return

        if self.__ultimo is self.__primeiro:
            self.resetList()
            return

        else:
            if self.__cursor == self.__ultimo:
                self._retrocederKPosicoes(1)
            self.__ultimo = self.__ultimo.anterior
            self.__primeiro.anterior = None
            self.__tamanho -= 1
            return

    # Este método busca a chave nos dados do elemento a ser excluído, guardando a posição do cursor para ser restaurada
    def excluirElemento(self, chave):
        if (chave is None) or (self.vazia()):
            return

        tempCursor = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.excluirAtual()
                break
            self._avancarKPosicoes(1)

        self.__cursor = tempCursor
        return

    # Este método exclui o elemento da lista, também guardando a posição do cursor para ser restaurada
    def excluirDaPosicao(self, posicao):
        if (0 > posicao) or (posicao is None) or self.vazia():
            return

        tempCursor = self.__cursor
        self._irParaPrimeiro()
        if posicao <= (self.__tamanho - 1):
            self._avancarKPosicoes(posicao)
            self.excluirAtual()

        self.__cursor = tempCursor
        return

    def buscarBool(self, chave):
        if (chave is None) or self.vazia():
            return False

        tempCursor = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.__cursor = tempCursor
                return True
            self._avancarKPosicoes(1)

        self.__cursor = tempCursor
        return False

    # Busca o elemento a partir da chave, retornando o elemento e preservando a posição do cursor para ser restaurada
    def buscar(self, chave):
        if (chave is None) or self.vazia():
            return False

        tempCursor = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                retorno = self.cursor.dados
                self.__cursor = tempCursor
                return retorno
            self._avancarKPosicoes(1)
        self.__cursor = tempCursor
        return None

    # Este método busca a posicao do elemento a partir da chave, guardando a posição do cursor para ser restaurada
    def buscarPosicao(self, chave):
        if (chave is None) or (self.vazia()):
            return

        tempCursor = self.__cursor
        self._irParaPrimeiro()
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dados):
                self.__cursor = tempCursor
                return i
            self._avancarKPosicoes(1)

        self.__cursor = tempCursor
        return

    def resetList(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanho = 0
        return

    def listarElementos(self):
        for i in range(self.tamanho):
            print(
                f"Elemento {i}: {self._acessarAtual()}, Anterior: {self.cursor.anterior.dados if self.cursor.anterior is not None else None}, Próximo: {self.cursor.proximo.dados if self.cursor.proximo is not None else None}")
            self._avancarKPosicoes(1)
        print(f"\nQuantidade de elementos: {self.tamanho}\n")

