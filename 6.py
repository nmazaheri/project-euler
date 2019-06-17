"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

25164150
"""

def square(num):
	return (num*num)
	
def func(limit):
	squareSum = 0
	sums = 0
	for i in xrange(1,limit+1):
		sums += i
		squareSum += square(i)

	sums = square(sums)
	#print squareSum
	#print sums
	return (sums-squareSum)

print(func(10))
print(func(100))
