

def find_permu_of_small(big,smalls):
    smalls = sorted(smalls)
    pos = 0
    while pos < len(big):
        start,end = getindex(big[pos],smalls)
        if start is -1:
            return False
        for each in smalls[start:end]:
            l = len(each)
            if each == big[pos:l]:
                pos = l
                break
