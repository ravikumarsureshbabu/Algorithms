#!/usr/bin/python3
l = []

while True:
    tup = input().split()
    if len(tup) == 0:
        break
    tup = [int(x) for x in tup]
    l.append(tuple(tup))

print (l)
sor = sorted(l,key = lambda x: x[1])
print (sor)
print (sor[-1])
print (sor[:-1])
