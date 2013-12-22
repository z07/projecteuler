from time import time

start = time()

sum_list = []
for i in range(1,101):
    sum_list.append(i**2)

print((sum(range(1,101))**2) - sum(sum_list))
print "1 : Seconds", time() - start
