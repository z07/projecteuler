from time import time

def d(n):
    div_list = []
    for i in range(1,n):
        if n%i == 0:
            div_list.append(i)
    return sum(div_list)

ami_list = []
for i in range(1,10000):
    if i == d(d(i)) and i != d(i):
        ami_list.append(i)

print sum(ami_list)
