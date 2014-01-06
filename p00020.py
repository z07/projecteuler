from time import time
from math import *
start = time()
fac = str(factorial(100))
fac_digits = []
for i in range(len(fac)):
    fac_digits.append(int(fac[i],10))

print sum(fac_digits)
print "1 : Seconds", time() - start
