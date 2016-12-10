#!/usr/bin/python3


def find_duplicate(lis):
    lis.sort()

    for index in range(len(lis)):
        if lis[index] == lis[index+1]:
            return lis[index]
    
    return 0

def find_duplicate2(lis):
    h = {}
    for each in lis:
        if each in h.keys():
            return each
        else:
            h[each] = 1

    return 0

def find_duplicate3(lis):
    lis = [ int(x) for x in lis ]

    for each in lis:
        if lis[abs(each)] > 0:
            lis[abs(each)] = -lis[abs(each)]
        else:
            return abs(each)

lis = [1,2,3,4,5,6,4]

print(find_duplicate3(lis))
