#!/usr/bin/python3

def perms(n):
    if not n:
        return

    for i in range(2**n):
        s = bin(i)[2:]
        print(s)
        s = "0" * (n-len(s)) + s
        yield s

def substitute_questionm(string):
    splits = string.split("?")
    
    for p in perms(len(splits)-1):
        new = ""
        k = 0
        for i in range(len(splits) -1 ):
            new += splits[i] + p[k]
            k += 1 
        new += splits[-1]
        print(new)
substitute_questionm("101?01?11")
