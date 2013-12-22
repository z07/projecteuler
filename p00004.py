from time import time

start = time()

number_list = []
for i in range(100,1000):
    for j in range(100,1000):
        number_list.append(str(i*j))

palindrome = []
for i in range(len(number_list)):
    if len(number_list[i]) == 6 and number_list[i][0] == number_list[i][-1] and number_list[i][1] == number_list[i][-2] and number_list[i][2] == number_list[i][-3]:
        palindrome.append(number_list[i])

print max(palindrome)
print "1 : Seconds", time() - start
