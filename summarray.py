#!/usr/bin/python3

import math

class res:
    def __init__(self,value):
        self.value = value
        self.arr = []

def get_max_sum_array(a, summ):
    m = [[ res(float("nan")) for y in range(summ +1)] for x in range(len(a)+ 1)]

    for x in range(len(a)):
        for y in range(1,summ + 1):
            if a[x] < 0:
                continue
            rem = y - a[x]
            if rem == 0:
                m[x+1][y].value = 1
                m[x+1][y].arr.append(a[x])
            elif rem > 0:    
                if not math.isnan(m[x][rem].value):
                   m[x+1][y].value = m[x][rem].value + 1
                   m[x+1][y].arr.append(a[x])            
                   m[x+1][y].arr += m[x][rem].arr 
    return m[-1][-1].arr 


a = [1,4,-3,2,6,7,8]
summ = 5
print (get_max_sum_array(a, summ))
