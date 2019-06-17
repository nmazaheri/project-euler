"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

76576500
"""
from math import *

def triangularCalc(num):
	total = 0
	for i in range(num+1):
		total += i
	return total
	
def primeList(n):
	myList = [1,n]
	for i in range(2,int(sqrt(n))+1):
		if n % i == 0:
			myList.append(i)
			myList.append(n/i)
	return myList


i = 0
size = 0
total = 0
while(size<500):
	i += 1
	total += i
	tempList = primeList(total)
	size = len(tempList)

print total
