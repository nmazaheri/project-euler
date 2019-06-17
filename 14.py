"""
The following iterative sequence is defined for the set of positive integers:

n > n/2 (n is even)
n > 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

837799
"""

def iterUp(num, count = 1 ):
	while num>1:
		count += 1
		if(num %2 == 0):
			num = num/2
		else:
			num = num*3 + 1
	return count
	
maxCount = [0,0]
for i in range (1000000):
	tempLength = iterUp(i)
	if tempLength > maxCount[1]:
		maxCount[0] = i
		maxCount[1] = tempLength
		
print maxCount[0]
