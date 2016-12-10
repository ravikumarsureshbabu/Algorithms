#!/usr/bin/python3

#staircase_length = input("enter the stair case lenght")
#steps = input("enter the stair case steps")
steps = input().split()
#steps = map(int, steps)
steps = [ int(x) for x in steps ]
print (sum(steps))
print(steps)
i = 0
for each in steps:
    print ("number =" + str(each))
    i += 1
    print ("i =" + str(i))
    

for i in range(0,3):
    print (i)
#print "staircase_length :" + staircase_length + " steps :" + steps[2]
