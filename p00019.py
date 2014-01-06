from time import time
from calendar import weekday
start = time()
sunday_counter = 0
for i in range(1901,2001):
    for j in range(1,13):
        if weekday(i,j,1) == 6:
            sunday_counter += 1

print sunday_counter
print "1 : Seconds", time() - start
