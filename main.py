from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()

lista.inserirComoPrimeiro(1)
lista.irParaPrimeiro()

lista.inserirComoUltimo(2)
lista.inserirComoUltimo(3)
lista.inserirComoUltimo(4)
lista.inserirComoUltimo(5)

lista.irParaPrimeiro()
print("------------------------")
print(lista.cursor.dados)
print("------------------------")

print(lista.primeiro.proximo.anterior)
lista.excluirPrimeiro()
print(lista.primeiro.anterior)

print("------------------------")
print(lista.cursor.dados)
print("------------------------")

# print(lista.primeiro.dados)

for x in range(lista.tamanho):
    print(lista.cursor.dados)
    lista.avancarKPosicoes(1)