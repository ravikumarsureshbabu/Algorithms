#!/usr/bin/python3

a = [int(x) for x in input().split() ]

b = a.copy()
m1 = a.pop(a.index(max(a)))

m2 = a.pop(a.index(min (a)))
maxu = max(m1,m2)
three = []

for each in a:

    if each > 0:
        if(m1 * each > maxu):
            maxu = m1*each
            three[:] = [] 
            three.append(m1)
            three.append(each)
    else:
        if(m2 * each > maxu):
            maxu = m2*each
            three[:] = [] 
            three.append(m2)
            three.append(each)

max3 = maxu
print(three)
if m1 not in three:
    a.append(m1)

for each in a:
    if each not in three:
        if each * maxu > max3:
            max3 = each*maxu

print (max3)

 


