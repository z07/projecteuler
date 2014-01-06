num_list = []
for i in range(2,101):
    for j in range(2,101):
        num_list.append(i**j)

print len(list(set(num_list)))
