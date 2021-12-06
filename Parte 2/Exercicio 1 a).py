def f(n):
    n0 = 'abcdefghijlmnopqrstuvxz '
    sn = []
    for i in range(len(n)):
        for j in range(len(n0)):
            if n[i] == n0[j]:
                sn.append(j)
                break
            else:
                continue
    print(sn)

    sne=[]
    for k in range (len(sn)):
        sne.append((17*sn[k]-5) % 24)
    print(sne)
    se=''
    for l in range (len(sne)):
        for m in range (len(n0)):
            if sne[l] == m:
                se = se + n0[m]
                break
            else:
                continue
    return se

n = 'serra da estrela'
print(n,"codificado será",f(n))
