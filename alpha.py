#!/usr/bin/python3
words = [
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
]

ref = words[0]
start = 0
end = len(words)
print(end)
mid = int((start+end) / 2)
ref = words[0]
print("mid %s" %(mid))    
while (start < end ):
    if ref < words[mid] and ref < words[mid+1]:
        start = mid
    elif ref > words[mid] and ref > words[mid+1]:
        end = mid
    elif ref < words[mid] and ref > words[mid+1]:
        print("index is " + str(mid+1))
        break
    mid = int((start+end) / 2)
    if(mid == (len(words) -1) ):
        print("index is " + str(0))
        break
    
    print("mid %s" %(mid))    

