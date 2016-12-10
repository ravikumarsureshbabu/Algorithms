#!/usr/bin/python3

a = input().split()
a = [ int(x) for x in a ]

op2 = [1 for x in a]
op1 = [1 for x in a]

for index in range(0,len(a) -1):
    op1[index + 1] = op1[index] * a[index]

for index in range(len(a)-2,-1,-1):
    print(index)
    op2[index] = op2[index+1] * a[index+1]

op = [a*b for a,b in zip(op1,op2)]
print(op1)
print(op2)
print(op) 
