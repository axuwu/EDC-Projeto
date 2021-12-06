while True:
    num = input("Digite um valor: ")
    num = int(num)

    primos = []
    for k in range(2, num):
        for x in range(2, k):
            if k % x == 0:
                break
        else:
            primos.append(k)

    print("Lista de primos:", primos)

    for i in range(len(primos)):
        if (num - primos[i]) in primos:
            resultado = num - (num - primos[i])
            print("A conjectura de Goldbach verifica-se, sendo a soma do par de primos resultante:", num, "=", resultado, "+",
                  num - resultado)
            break
        else:
            print("A conjectura de Goldbach não se verifica, sendo que", num, "não resulta de um par de primos.")
            break

    voltar = input("Repetir processo - Digite 1 | Fechar - Digite 2: ")
    voltar = int(voltar)

    if voltar == 2:
        break