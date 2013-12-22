from time import time
from sympy import *
start = time()
print max(factorint(600851475143).keys())
print "1 : Seconds", time() - start
