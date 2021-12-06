def inversof(n):
    n0 = 'abcdefghijlmnopqrstuvxz '
    se1n=[]
    for i in range (len(n)):
        for j in range(len(n0)):
            if n[i] == n0[j]:
                se1n.append(j)
                break
            else:
                continue
    print(se1n)

    s1n=[]
    for k in range (len(se1n)):
        s1n.append((-7*(se1n[k]+5)) % 24)
    print(s1n)
    s1=''
    for l in range (len(s1n)):
        for m in range (len(n0)):
            if s1n[l] == m:
                s1 = s1 + n0[m]
                break
            else:
                continue
    return s1

n = 'xmvnaucmxgpmhuzuchachuoux'
print(n,"descodificado será:", inversof(n))