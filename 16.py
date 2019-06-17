"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

result = 2 ** 1000
stringResult = str(result)

mysum = 0
for number in stringResult:
	mysum += int(number)
print mysum
