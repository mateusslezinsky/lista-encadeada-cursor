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

    lista.listarElementos()

    print("Excluindo elemento 'Guilherme'")
    lista.excluirElemento("Guilherme")
    print("Excluindo da posição 1")
    lista.excluirDaPosicao(1)
    lista.irParaPrimeiro()
    lista.listarElementos()


testes1()
testes2()
