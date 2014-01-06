import sys
from time import time
import random

def is_prime(q,k=2000):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False

    return True

start = time()
max_n = int(sys.argv[1],10)
p_list = []
n = 1
while len(p_list) == 0 or n < max_n:
    if is_prime(n) == True:
        p_list.append(n)
    else:
        pass
    n += 1

print str(p_list[-1])
print str(sum(p_list))
print "1 : Seconds", time() - start
