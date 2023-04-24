# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva - 22102556

from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

# Colocando primeiro e último elementos
lista.inserirComoPrimeiro(0)
lista.inserirComoUltimo(1)
lista.inserirComoUltimo(5)
lista.irParaPrimeiro()


def testes1():
    # Avançando cursor pra primeira posição
    lista.irParaPrimeiro()
    print("------------------------")
    print(f"Imprimindo valor do cursor: {lista.cursor.dados}")
    print("------------------------")

    print(f"Primeiro: {lista.primeiro.proximo.anterior.dados}")
    lista.excluirPrimeiro()
    print(f"Após exclusão: {lista.primeiro.anterior}")

    print("------------------------")
    print(f"Valor do cursor após exclusão: {lista.cursor.dados}")
    print("------------------------")


def testes2():
    lista.inserirAposAtual(2)
    lista.avancarKPosicoes(1)
    lista.inserirAposAtual(3)
    lista.avancarKPosicoes(1)
    lista.retrocederKPosicoes(1)
    lista.inserirNaPosicao(2, 4)
    lista.avancarKPosicoes(2)
    lista.irParaUltimo()
    lista.irParaPrimeiro()

    for i in range(lista.tamanho):
        print(f"Elemento {i+1}: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados if lista.cursor.anterior is not None else None}, Próximo: {lista.cursor.proximo.dados if lista.cursor.proximo is not None else None}")
        lista.avancarKPosicoes(1)

    print(f"\nQuantidade de elementos: {lista.tamanho}\n")


testes1()
testes2()
