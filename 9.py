"""
Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3-2 + 4-2 = 9 + 16 = 2-5 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

31875000
"""


def sumTrip(num):
	for a in xrange(1,num):
		for b in xrange(1,num-a):
			c = num - a - b
			a2 = a*a
			b2 = b*b
			c2 = c*c
			if (a2+b2==c2):
				print a,b,c
				return a*b*c
				
print(sumTrip(1000))
