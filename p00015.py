from time import time
from math import *
grid = 20
grid2 = grid * 2
start = time()
print factorial(grid2)/(factorial(grid2-grid) * factorial(grid))
print "1 : Seconds", time() - start
