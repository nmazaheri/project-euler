"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

142913828922
"""

from math import *

def isPrime(num):
	limit = int(sqrt(num))+1
	for i in xrange(2,limit):
		if(num%i == 0):
			return False
	return True		

limit = 2000000
total = 0
for i in xrange(2,limit):
	if(isPrime(i)):
		total += i
print total
