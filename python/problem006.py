

def computes(n):
	susq=0
	sqsum=0
	
	for x in range(1,n+1):
		susq+=x
		sqsum+=x**2
	return str(susq**2-sqsum)
	


		


print(computes(100))

