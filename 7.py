"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
104743
"""

from math import *

def isPrime(num):
	lim = int(sqrt(num)) +1
	for i in xrange(2,lim):
		if(num%i == 0):
			return False
	return True

start = 1
count = 0
myList = []
while(count<10001):
	start+=1
	if(isPrime(start)):
		count+=1

print start
