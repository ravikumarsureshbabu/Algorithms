

def loadintodict(nums,start):
    d = {}
    index = start
    for each in nums[start:]:
        d[each] = index
        index += 1

    return d

def t3sum(nums,ttarget):
    triplet = []
    dist = float("inf")

    for index,each in enumerate(nums):
        diff  = ttarget - each
        if diff < 0:
            diff *= -1
        
        for target in range(diff,-1,-1):
            d = loadintodict(nums,index+1)
            for key,value in d.items():
                if target - key == key:
                    continue
                if target - key in d:
                    total = each + target
                    if abs(ttarget - total) < dist:
                        triplet = [each, key, target - key]
                        dist = abs(ttarget - total)    
        diff *= -1           
        for target in range(diff,1):
            d = loadintodict(nums,index+1)
            for key,value in d.items():
                if target - key == key:
                    continue
                if target - key in d:
                    total = each + target
                    if abs(ttarget - total) < dist:
                        triplet = [each, key, target - key]
                        dist = abs(ttarget - total)

    return triplet
a = [-1, 2, 1, -4]            
print(t3sum(a,1))
