#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def factor(n):
	print(n)
	for x in range(111,int(n/71)):	
		if n%x==0:
			print(n/x)
			print(x)


factor(600851475143)