# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva - 22102556

from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

# Colocando primeiro e último elementos
lista.inserirComoPrimeiro("Dummy")
lista.inserirComoUltimo("Mateus")
lista.inserirComoUltimo("Augusto")
lista.inserirComoUltimo("DeLucca")
lista.irParaPrimeiro()


def listarElementos():
    for i in range(lista.tamanho):
        print(
            f"Elemento {i + 1}: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados if lista.cursor.anterior is not None else None}, Próximo: {lista.cursor.proximo.dados if lista.cursor.proximo is not None else None}")
        lista.avancarKPosicoes(1)
    print(f"\nQuantidade de elementos: {lista.tamanho}\n")


def testes1():
    # Avançando cursor pra primeira posição
    lista.irParaPrimeiro()
    print("------------------------")
    print(f"Imprimindo valor do cursor: {lista.cursor.dados}")
    print("------------------------")

    print(f"Primeiro: {lista.primeiro.dados}")
    lista.excluirPrimeiro()
    print(f"Após exclusão: {lista.primeiro.anterior}")

    print("------------------------")
    print(f"Valor do cursor após exclusão: {lista.cursor.dados}")
    print("------------------------")


def testes2():
    lista.inserirAposAtual("Marcos")
    lista.avancarKPosicoes(1)
    lista.inserirAposAtual("Chico")
    lista.avancarKPosicoes(1)
    lista.retrocederKPosicoes(1)
    lista.inserirNaPosicao(2, "Guilherme")
    lista.inserirNaPosicao(1, "Yasmim")
    lista.avancarKPosicoes(2)
    lista.irParaUltimo()
    lista.irParaPrimeiro()

    listarElementos()

    print("Excluindo elemento 'Guilherme'")
    lista.excluirElemento("Guilherme")
    lista.irParaPrimeiro()
    listarElementos()


testes1()
testes2()
