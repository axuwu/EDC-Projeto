def insertion_Sort(lista):
    print("Lista =", lista)

    for i in range(1, len(lista)):

        valoratual = lista[i]
        posicao = i

        while posicao > 0 and lista[posicao - 1] > valoratual:
            lista[posicao] = lista[posicao - 1]
            posicao = posicao - 1

        lista[posicao] = valoratual

    print("Lista ordenada por ordem crescente =", lista)


lista1 = [3, 2, 5, 17, 1]
insertion_Sort(lista1)

import random
lista2 = random.sample(range(1000), 200)
insertion_Sort(lista2)


