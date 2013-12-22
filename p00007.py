#coding:utf-8
from time import time
import random

def is_prime(q,k=50):
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
p_list = []
counter = 1
max_counter = 10001
while len(p_list) < max_counter:
    if is_prime(counter) == True:
        p_list.append(counter)
    else:
        pass
    counter += 1

print len(p_list)
print p_list[max_counter-1]
print "1 : Seconds", time() - start
