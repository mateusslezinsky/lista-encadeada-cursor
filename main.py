from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

lista.inserirComoPrimeiro(1)
lista.irParaPrimeiro()

lista.inserirComoUltimo(2)
lista.inserirComoUltimo(3)
lista.inserirComoUltimo(4)
lista.inserirComoUltimo(5)

lista.irParaPrimeiro()

for x in range(lista.tamanho):
    print(lista.cursor.dados)
    lista.avancarKPosicoes(1)