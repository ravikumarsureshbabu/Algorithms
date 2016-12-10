#!/usr/bin/python3
import random

def rand5():
    return (random.randint(0,5))

def rand7():
    return int(rand5()/5 * 7)


while True:
    ip = input()
    if ip == "e":
        break
    else:
        print (rand7())
    

