#!/usr/bin/python3

def generate_combi(arr, n, r, start, op = ""):
#    print("start %s op %s" %(str(start),op))
    if len(op) == r:
        print(op)
        return
    
    end = start + r
    if (end > n):
        end = n

    for i in range(start,end):
        new_c = op + arr[i]
        generate_combi(arr,n,r,i+1,new_c) 


arr = ['1','2','3','4','5']
n = 5
r = 3

generate_combi(arr,n,r,0)
