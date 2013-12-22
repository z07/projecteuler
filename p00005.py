from time import time
from sympy import *

start = time()

fact_dic = {}

for i in range(1,21):
    i_dic = factorint(i)
    for j in range(len(i_dic)):
        factor = i_dic.keys()[j]
        if factor not in fact_dic.keys():
            fact_dic.update({factor:i_dic[factor]})
        elif factor in fact_dic.keys() and i_dic[factor] > fact_dic[factor]:
            fact_dic.pop(factor)
            fact_dic.update({factor:i_dic[factor]})

a = 1
for i in range(len(fact_dic)):
    factor = fact_dic.keys()[i]
    a = a * (factor ** fact_dic[factor])

print a
print "1 : Seconds", time() - start
