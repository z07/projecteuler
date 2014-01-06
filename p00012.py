import sys
from time import time
start = time()
n_list = []
for i in range(2,10000):
    n_list.append(sum(range(1,i)))

d_list_list = []
for i in range(len(n_list)):
    d_list = []
    for j in range(n_list[i]):
        if n_list[i]%(n_list[i]-j) == 0:
            d_list.append(n_list[i] - j)
    d_list_list.append(d_list)
    if len(d_list_list[-1]) >= 500:
        print n_list[i],d_list, len(d_list)
        sys.exit()

print "1 : Seconds", time() - start
