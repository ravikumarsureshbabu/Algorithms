

def first_missing_positive(arr):
    d = {}
    for each in arr:
        d[(each)] = 1

    count = 0
    for key in sorted(d.keys()):
        if key < 0:
            continue
        else:
            if count == 0:
                if key == 0 or key == 1:
                    count = key
                else:
                    return 1
            else:
                count += 1
                if key != count:
                    return count
    return count+1


a = [3,4,-1,1]
print(first_missing_positive(a))
