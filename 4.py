"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

906609
"""

def p(num):
	return (str(num) == str(num)[::-1])


def largest(top,bot):
	palindrome = []
	for x in range(top,bot,-1):
		for y in range(top,bot,-1):
			temp = x*y
			if p(temp):
				palindrome.append(temp)
	return max(palindrome)

print largest(999,100)

"""
print max([(x*y) for x in range(100,1000) for y in range(100,1000) if p(x*y)])

result = [{x*y:(x,y)} for x in range(100,1000) for y in range(100,1000) if p(x*y)]
print result[result.index(max(result))]
"""
