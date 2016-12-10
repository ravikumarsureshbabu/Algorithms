#!/usr/bin/python3

tree = {"w" : {"w" : {"w" : {} }} }

cases = int(input())

while cases:
    u = input()
    url = list(u)

    db = tree
    print(db)
    for each in url:
        if each in db:
            db = db[each]
        else:
            db[each] = {}
            db = db[each]
    print("current db is %s"%(tree))
    cases -= 1


