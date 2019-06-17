"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

6857
"""

def pf(number):
	factors = []
	i = 2
	while(number > 1):
		while(number % i == 0 ):
			print i, number
			factors.append(i)
			number /= i
		i += 1
	return max(factors)

#print pf(13195)
#print pf(600851475143)
pf(9765)
