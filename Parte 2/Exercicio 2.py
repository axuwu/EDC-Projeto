def euclides_mdc(dividendo, divisor):
    while divisor != 0:
        resto = divisor
        divisor = dividendo % divisor
        dividendo = resto
    return dividendo


def euler(n):
    resultado = 0

    for k in range(1, n + 1):
        if euclides_mdc(n, k) == 1:
            resultado += 1

    return resultado


n = [4, 5, 106, 107, 2016]
for i in range(len(n)):
    solucao = n[i]
    posicao = i

    while posicao > 0 and n[posicao - 1] > solucao:
        n[posicao] = n[posicao - 1]
        posicao -= 1

    n[posicao] = solucao
    print("φ","(",n[i],")","=",euler(solucao))


