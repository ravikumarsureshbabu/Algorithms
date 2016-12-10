#!/usr/bin/python3

a = ['2', '1', '3']
print(sorted(a))
d = {'1' : "Z",
     '3' : "X",
     '2' : "Y"   
    }
print(sorted(d))
print(sorted(d.values()))
for k in sorted(d):
    print("%s %s" %(k, d[k]))
