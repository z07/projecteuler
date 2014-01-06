from time import time
from math import *
start = time()
power = 1000
digits = str(2**power)
d_list = []
for i in range(len(digits)):
    d_list.append(int(digits[i],10))

print sum(d_list)
print "1 : Seconds", time() - start
