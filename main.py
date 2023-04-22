from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

lista.inserirComoPrimeiro(1)
lista.inserirComoUltimo(2)
lista.irParaPrimeiro()
print(lista.acessarAtual())
lista.avancarKPosicoes(1)
print(lista.acessarAtual())
lista.inserirAntesDoAtual(3)
lista.retrocederKPosicoes(1)
print(lista.acessarAtual())
