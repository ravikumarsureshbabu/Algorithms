#!/usr/bin/python3

def fibo(n,m):
    if m[n] == -1:
        if m[n-1] == -1:
            m = fibo(n-1,m) 
        if m[n-2] == -1:
            m = fibo(n-2,m)
        m[n] = m[n-1] + m[n-2]
    return m
    
        
n = int(input())
m = [ -1 for i in range(n+1)]
m[0] = 0
m[1] = 1
m = fibo(n,m)
print(m[-1])

