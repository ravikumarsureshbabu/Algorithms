#!/usr/bin/python3

def get_value(tup, capacity):
    count = 0
    if tup[0] == 0:
        return 0,capacity
    while capacity - tup[0] >= 0:
        count += 1
        capacity -= tup[0]

    value = count * tup[1]
    return value,capacity

def max_duffel_bag_value(tuples,capacity):
    if capacity == 0:
        return 0
    m = [[0 for i in range(capacity+1)] for j in range(len(tuples)+1)]
    for i in range(len(tuples)):
        for j in range(1,capacity+1):
            value,rem = get_value(tuples[i],j)
            m[i+1][j] += value 
            if rem != 0:
                m[i+1][j] += m[i][rem]
            m[i+1][j] = max(m[i+1][j],m[i][j])
    return m[-1][-1]

cake_tuples = [(7, 160), (0, 0), (2, 15)]
capacity    = 20

print (max_duffel_bag_value(cake_tuples, capacity))


