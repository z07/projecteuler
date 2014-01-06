import sys
from math import *
from time import time
start = time()
n_list = []
for i in range(10000,15000):
    n_list.append(sum(range(1,i)))

d_list_list = []
for i in range(len(n_list)):
    d_list = []
    for j in range(1,int(sqrt(n_list[i]))):
        if n_list[i]%j == 0:
            d_list.append(j)
    d_list_list.append(d_list)
    if len(d_list_list[-1])*2 >= 500:
        print n_list[i],len(d_list)
        sys.exit()

print "1 : Seconds", time() - start
