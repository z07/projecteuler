from time import time

start = time()
f_list = [1,2]
while f_list[-1]+f_list[-2] < 4000000:
    f_list.append(f_list[-1]+f_list[-2])

f_e_list = []
for i in range(len(f_list)):
    if f_list[i] % 2 == 0:
        f_e_list.append(f_list[i])

print sum(f_e_list)
print "1 : Seconds", time() - start
