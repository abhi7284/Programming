a = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6),(11,15),(13,22),(21,23)]

import copy

temp = a[0]

l = []

for i in a:

    if i[0] >= temp[0] and i[0]<=temp[1]:
        temp = (min(temp[0],i[0]),max(temp[1],i[1])) 
        
    else:
        l.append(copy.deepcopy(temp))
        temp = i

l.append(copy.deepcopy(temp))

print(l)
