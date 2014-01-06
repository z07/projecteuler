tri = {}
for i in range(3,1001):
    tri_i = []
    for j in range(i-2):
        for k in range(j,i-1):
            if i-j-k > 0 and j**2 + k**2 == (i-j-k)**2:
                tri_i.append([j,k,i-j-k])
    tri[i] = len(tri_i)

print sorted(tri.items(), key=lambda x:x[1], reverse=True)[0]
