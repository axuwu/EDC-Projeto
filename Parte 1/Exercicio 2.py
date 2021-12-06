def implicacao(a,b):
	if a == True:
		return b
	else:
		return True

p, q, r = [True,True,True,True,False,False,False,False], [True,True,False,False,True,True,False,False], [True,False,True,False,True,False,True,False]	
i=0

print ("    p    | q     | r     | ~p    | pVq   | ~pVr  | (pVq)^(~pVr) | qVr   | (pVq)^(~pVr)->(qVr)")
print ("  ", "---"*30)

a = (p[i] or q[i]) and (not p[i] or r[i])
b = q[i] or r[i]

while i<8:
		if p[i] == True and q[i] == True and r[i] == True:
			print("  ",p[i]," |",q[i]," |",r[i]," |",not p[i],"|",p[i] or q[i]," |",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"        |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == True and q[i] == True and r[i] == False:
			print("  ",p[i]," |",q[i]," |",r[i],"|",not p[i],"|",p[i] or q[i]," |",not p[i] or r[i],"|",(p[i] or q[i]) and (not p[i] or r[i]),"       |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == True and q[i] == False and r[i] == True:
			print("  ",p[i]," |",q[i],"|",r[i]," |",not p[i],"|",p[i] or q[i]," |",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"        |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == True and q[i] == False and r[i] == False:
			print("  ",p[i]," |",q[i],"|",r[i],"|",not p[i],"|",p[i] or q[i]," |",not p[i] or r[i],"|",(p[i] or q[i]) and (not p[i] or r[i]),"       |",q[i] or r[i],"|",implicacao(a,b),)
		elif p[i] == False and q[i] == True and r[i] == True:
			print("  ",p[i],"|",q[i]," |",r[i]," |",not p[i]," |",p[i] or q[i]," |",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"        |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == False and q[i] == True and r[i] == False:
			print("  ",p[i],"|",q[i]," |",r[i],"|",not p[i]," |",p[i] or q[i]," |",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"        |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == False and q[i] == False and r[i] == True:
			print("  ",p[i],"|",q[i],"|",r[i]," |",not p[i]," |",p[i] or q[i],"|",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"       |",q[i] or r[i]," |",implicacao(a,b),)
		elif p[i] == False and q[i] == False and r[i] == False:
			print("  ",p[i],"|",q[i],"|",r[i],"|",not p[i]," |",p[i] or q[i],"|",not p[i] or r[i]," |",(p[i] or q[i]) and (not p[i] or r[i]),"       |",q[i] or r[i],"|",implicacao(a,b),)
		i=i+1
		
print ("\nComo se pode ver pela última coluna da tabela de verdade, é uma tautologia.")

