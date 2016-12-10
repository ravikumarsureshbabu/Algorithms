#!/usr/bin/python3

d = {'1' : "A",
     '2' : "B",
     '3' : "C"
    }


num = input()

for level in range(0,len(num)):
    i = 0
    while ( (i + level) <= (len(num)-1)):
        s = ""
        for j in range(i,i+level+1):
            s += d[num[j]]
        print(s)
        i += 1

      
