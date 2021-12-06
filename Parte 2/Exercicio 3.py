def congruencia(n, a):
    for x in range(1, n):
        if (a * x - 1) % n == 0:
            return x
        else:
            continue

n = [7, 26, 232]
a = [5, 7, 89]

print("5𝑥 ≡ 1 (mod 7), para x =", congruencia(n[0], a[0]))
print("7𝑥 ≡ 1 (mod 26), para x =", congruencia(n[1], a[0]))
print("89𝑥 ≡ 1 (mod 232), para x =", congruencia(n[2], a[0]))

