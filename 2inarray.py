#!/usr/bin/python3


arr = [int(x) for x in input().split()]
summ = int(input())

d= {}
for index,value in enumerate(arr):
    d[value] = index


for key in d.keys():
    another = summ - key
    if another in d:
        print("%s %s" %(key,another))
        break

