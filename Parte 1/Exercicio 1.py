def implica_1(p, q):
 if p ==True and q==False:
     return False
 else:
     return True


def implica_2(p, q):
   return not p or q

p=[True, True, False, False]
q=[True, False, True, False]
i=0
while i<4:
    print (p[i],q[i],implica_1(p[i],q[i]),implica_2(p[i],q[i]))
    i=i+1