from time import time

start = time()
l_dic = {}
for i in range(3,1000000):
    s = i
    s_list = [s]
    while s != 1:
        if s%2 == 0:
            s = s/2
        else:
            s = 3*s + 1
        s_list.append(s)
    l_dic[i] = len(s_list)

print sorted(l_dic.items(), key=lambda x:x[1], reverse = True)[0]
print "1 : Seconds", time() - start
