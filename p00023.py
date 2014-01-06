from time import time

def d(n):
    div_list = []
    for i in range(1,n):
        if n%i == 0:
            div_list.append(i)
    return sum(div_list)

abun_list = []
for i in range(1,28123):
    if i < d(i):
        abun_list.append(i)

abun_sum_list = []
for i in range(len(abun_list)):
    for j in range(len(abun_list)):
        if abun_list[i] + abun_list[j] <= 28123:
            abun_sum_list.append(abun_list[i] + abun_list[j])

abun_sum_set = set(abun_sum_list)
sol_set = set(range(1,28123)).difference(abun_sum_list)
print sum(list(sol_set))
