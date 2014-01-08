n = 1001
a = 1
sq_list = [1]
for i in range(1,1+(n-1)/2):
    for j in range(4):
        a += 2*i
        sq_list.append(a)
    a = sq_list[-1]

print sum(sq_list)
