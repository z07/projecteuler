from math import *
fact_list = []
for i in range(6 * factorial(9)):
    str_i = str(i)
    dig_i = []
    for j in range(len(str_i)):
        dig_i.append(factorial(int(str_i[j],10)))
    if sum(dig_i) == i and i != 1 and i != 2:
        fact_list.append(i)

print fact_list
print sum(fact_list)
