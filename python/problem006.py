#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def computes(n):
	susq=0
	sqsum=0
	
	for x in range(1,n+1):
		susq+=x
		sqsum+=x**2
	return str(susq**2-sqsum)
	

print(computes(100))

