#!/usr/bin/python3

def generate_binary(n, k = 1,arr = ""):
    if (k > n):
        print(arr)
        return 

    for i in range(0,2):
        new = arr + str(i)
        generate_binary(n,  k+1, new)


generate_binary(3)

