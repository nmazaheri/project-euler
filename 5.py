"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

232792560
"""
import sys
import time

def checkRemainderB(num, limit):
	divs = [i for i in xrange(1,limit+1) if num%i==0]
	return (len(divs) == limit)


def checkRemainder(num, limit):
	counter = 0
	for i in xrange(1,limit+1):
		if ((num % i) != 0):
			return False
	return True


def smallestRemainder(limit):
	start = 2520
	while(True):
		if(checkRemainder(start, limit)):
			return start
		else:
			start += 2520

print(smallestRemainder(20))
