"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?

137846528820
"""

import math

def LatticePath(down, right):
    
    if(down == 0 or right == 0):
        return 1
    
    else:
        return LatticePath(down -1, right) + LatticePath(down, right -1)
    
    
def LatticePath_v2(down, right):
	numPaths = 0
    
	return math.factorial(down + right) / (math.factorial(down)**2)
    
	
print LatticePath(2,2)


print LatticePath_v2(20,20)
