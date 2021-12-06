def primos(x):
    i = 2
    while i <= x:
        if (x % i) == 0:
            break
        i += 1
    if i == x:
        return 0
    else:
        return 1


num = input("Digite um valor: ")
num = int(num)

while (num % 2) != 0:
    print("Erro: Insira um número par.")
    num = input("Digite um valor: ")
    num = int(num)

b = 1
c = 1
for b in range(b, num):
    for c in range(c, num):
        j = primos(b)
        k = primos(c)
        if j == 0 and k == 0 and b + c == num and b <= c:
            print("A conjectura de Goldbach verifica-se, sendo a soma do par de primos resultante:", num, "=", b, "+",
                  c)
            break