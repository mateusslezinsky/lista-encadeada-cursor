# Mateus Slezinsky Pereira - 21200422
# Augusto Teixeira da Silva

from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

# Colocando primeiro e último elementos
lista.inserirComoPrimeiro(1)
lista.inserirComoUltimo(5)

# Avançando cursor pra primeira posição
lista.irParaPrimeiro()

# Imprimindo o valor da primeira posição + posição dela na lista
print(
    f"Primeiro: {lista.primeiro.dados}, Anterior: {lista.primeiro.anterior}, Próximo: {lista.primeiro.proximo.dados}")

lista.inserirAposAtual(2)
lista.avancarKPosicoes(1)
print(
    f"Elemento 2: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados}, Próximo: {lista.cursor.proximo.dados}")

lista.inserirAposAtual(3)
lista.avancarKPosicoes(1)
print(
    f"Elemento 3: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados}, Próximo: {lista.cursor.proximo.dados}")

lista.retrocederKPosicoes(1)
lista.inserirNaPosicao(2, 4)
lista.avancarKPosicoes(2)
print(
    f"Elemento 4: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados}, Próximo: {lista.cursor.proximo.dados}")


lista.irParaUltimo()
# Imprimindo último elemento
print(
    f"Último: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados}, Próximo: {lista.cursor.proximo}")

print(f"\nQuantidade: {lista.tamanho}\n")
lista.irParaPrimeiro()
for i in range(lista.tamanho):
    print(f"Elemento {i+1}: {lista.acessarAtual()}, Anterior: {lista.cursor.anterior.dados if lista.cursor.anterior is not None else None}, Próximo: {lista.cursor.proximo.dados if lista.cursor.proximo is not None else None}")
    lista.avancarKPosicoes(1)
