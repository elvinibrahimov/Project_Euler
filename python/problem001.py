#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#    Tərcümə
#10 dan kiçik  3 və 5-ə bölünən natural ədədlər 3,5 , 6, 9 dur.
#Bu ədədlərin cəmi 23 edir.
#1000 dın kiçik 3 və 5 ə bölünən natural ədədlərin cəmini tap.

def sum():
	result=0
	for x in range(1000):
		if (x%3==0 or x%5==0):
			result+=x
	return result

print(sum())

