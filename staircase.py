#!/usr/bin/python3

sc_length = input()
sc_steps = input().split()
sc_steps = [ int(x) for x in sc_steps ]

class Res(object):
    def __init__(self):
        self.count = 0
        self.steps = []


def get_num_steps(maxl,step):
    count = 0
    while(maxl - step >= 0):
        count += 1
        maxl -= step
    return count,maxl


m = [ [ Res() for x in range(int(sc_length) + 1)] for y in range(len(sc_steps) + 1) ]

lengths = range( 1, int(sc_length) + 1 )
for i in range(len(sc_steps)):
    for j in range(len(lengths)):
        count,rem = get_num_steps(lengths[j],sc_steps[i])
        m[i+1][j+1].count = count
        m[i+1][j+1].steps.extend([sc_steps[i]] * count)
        if rem != 0:
            m[i+1][j+1].count += m[sc_steps[i-1]][rem].count
            m[i+1][j+1].steps.extend(m[sc_steps[i-1]][rem].steps)

print (m[-1][-1].count)
print (m[-1][-1].steps)            
    
