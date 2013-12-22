from time import time
start = time()
r_list = []
for i in range(1,1000):
	if i % 3 == 0 or i % 5 == 0:
		r_list.append(i)

print sum(r_list)
print "1 : Seconds", time() - start

start = time()
print sum(list(set(range(0,1000,3))|set(range(0,1000,5))))
print "2 : Seconds", time() - start

start = time()
print sum(list(set(range(0,1000,3))|set(range(0,1000,5))))
print "3 : Seconds", time() - start

start = time()
print sum([i for i in range(1000) if (not i%3) or (not i%5)])
print "4 : Seconds", time() - start

start = time()
print sum(filter(lambda n : (n % 3 == 0) or (n % 5 == 0), range(1000)))
print "5 : Seconds", time() - start

