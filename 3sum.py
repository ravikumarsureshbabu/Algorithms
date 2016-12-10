

def loadintodict(nums,start):
    d = {}
    index = start
    for each in nums[start:]:
        d[each] = index
        index += 1

    return d

def t3sum(nums):
    triplets = []

    for index,each in enumerate(nums):
        target = -1 * each
        d = loadintodict(nums,index+1)
        for key,value in d.items():
            if target - key in d:
                triplet = [each, key, target - key]
                triplets.append(triplet)

    return triplets
a = [-1, 0, 1, 2, -1, -4]            
print(t3sum(a))
