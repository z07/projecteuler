fif_list = []
for i in range(11,100):
    a = int(str(i)[0],10)
    b = int(str(i)[1],10)
    if i == a**5 + b**5:
        fif_list.append(i)

for i in range(101,1000):
    a = int(str(i)[0],10)
    b = int(str(i)[1],10)
    c = int(str(i)[2],10)
    if i == a**5 + b**5 + c**5:
        fif_list.append(i)

for i in range(1001,10000):
    a = int(str(i)[0],10)
    b = int(str(i)[1],10)
    c = int(str(i)[2],10)
    d = int(str(i)[3],10)
    if i == a**5 + b**5 + c**5 + d**5:
        fif_list.append(i)

for i in range(10001,100000):
    a = int(str(i)[0],10)
    b = int(str(i)[1],10)
    c = int(str(i)[2],10)
    d = int(str(i)[3],10)
    e = int(str(i)[4],10)
    if i == a**5 + b**5 + c**5 + d**5 + e**5:
        fif_list.append(i)

for i in range(100001,1000000):
    a = int(str(i)[0],10)
    b = int(str(i)[1],10)
    c = int(str(i)[2],10)
    d = int(str(i)[3],10)
    e = int(str(i)[4],10)
    f = int(str(i)[5],10)
    if i == a**5 + b**5 + c**5 + d**5 + e**5 + f**5:
        fif_list.append(i)

print fif_list
print sum(fif_list)

