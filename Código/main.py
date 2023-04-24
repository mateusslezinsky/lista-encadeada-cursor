# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva - 22102556

from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

# Colocando primeiro e último elementos
lista.inserirComoPrimeiro("Mario")
lista.inserirComoUltimo("Mateus")
lista.inserirComoUltimo("Augusto")
lista.inserirComoUltimo("DeLucca")


def testes1():
    # Avançando cursor pra primeira posição
    lista._irParaPrimeiro()
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
    lista._avancarKPosicoes(1)
    lista.inserirAposAtual("Chico")
    lista._avancarKPosicoes(1)
    lista._retrocederKPosicoes(1)
    lista.inserirNaPosicao(2, "Guilherme")
    lista.inserirNaPosicao(1, "Yasmim")
    lista._avancarKPosicoes(2)
    lista._irParaUltimo()
    lista._irParaPrimeiro()

    lista.listarElementos()

    print("Excluindo elemento 'Guilherme'")
    lista.excluirElemento("Guilherme")
    print("Excluindo da posição 1")
    lista.excluirDaPosicao(1)
    lista._irParaPrimeiro()
    lista.listarElementos()


testes1()
testes2()
