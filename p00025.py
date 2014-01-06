from time import time
start = time()

n = 10 ** (1000-1)
a,b = 1,1
fib_list = [a,b]
while b <= n:
    a,b = b, a+b
    fib_list.append(b)

print len(fib_list)
print "1 : Seconds", time() - start
