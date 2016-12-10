#!/usr/bin/python3


def permu(string, k, n):
    if k == n:
        print(string)
    else:
        for i in range(k,n):
            tmp = string[i]
            string[i] = string[k]
            string[k] = tmp
            permu(string, k+1, n)
            tmp = string[i]
            string[i] = string[k]
            string[k] = tmp


string = "aaabcd"
string = list(string)
permu(string,0,len(string))
