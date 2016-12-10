#!/usr/bin/python3

tot_w = int(input())

a = input().split()

w = []
v = []
while a:
    w.append(int(a[0]))
    v.append(int(a[1]))
    
    a = input().split()

def knapsack(w, v, total_weight,m,i,j):
    if i == 0 or j == 0:
        m[i][j] = 0
    else:
        count = int(total_weight / w[i-1])
        rem = total_weight % w[i-1]
        if count == 0:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(v[i-1]*count + m[i-1][rem], m[i-1][j])
    
    
    if (j == total_weight):
        if (i == len(w)):
            return m
        else:
            i += 1
            j = 0
    else:
        j += 1


    m = knapsack(w,v,total_weight,m,i,j)
    print("for i = %s j = %s" %(i,j))
    print(m)
    return m

m = [[0 for y in range(tot_w+1)] for x in range(len(w)+1)]
knapsack(w,v,tot_w,m,0,0)
print (m[-1][-1])
        
    
    
