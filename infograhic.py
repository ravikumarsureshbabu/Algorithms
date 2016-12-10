#!/usr/bin/python3

import re

inp = input()
inp = re.findall('\w+', inp)

cloud = {}
for each in inp:
    if each in cloud:
        cloud[each] += 1
    else:
        cloud[each] = 1

for key in cloud.keys():
    print("key %s , value %s" %(key,cloud[key]))
