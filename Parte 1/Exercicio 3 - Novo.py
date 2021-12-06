def Primo(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def PrimoAnterior(n):
    n -= 1
    while n > 2 and not Primo(n):
        n -= 1
    return n

def PrimoSeguinte(n, num):
    n += 1
    while n < num and not Primo(n):
        n += 1
    return n

numPar = 0
numeroPrimo1 = 2

while numPar <= 2:
    numPar = input("Digite um valor inteiro superior a 2: ")
    numPar = int(numPar)

numeroPrimo2 = PrimoAnterior(numPar)

while numeroPrimo1 <= numeroPrimo2:
    if (numeroPrimo1 + numeroPrimo2) < numPar:
        numeroPrimo1 = PrimoSeguinte(numeroPrimo1, numPar)
    elif (numeroPrimo1 + numeroPrimo2) > numPar:
        numeroPrimo2 = PrimoAnterior(numeroPrimo2)
    else:
        print("A conjectura de Goldbach verifica-se, sendo a soma do par de primos resultante:", numPar, "=", numeroPrimo1, "+", numeroPrimo2)
        break

