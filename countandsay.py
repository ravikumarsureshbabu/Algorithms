def countandsay(n, k = 1, string = "1"):
    if k == n:
        return string

    count = 0
    prev = string[0]
    newstring = ""
    for each in string:
        if each == prev:
            count += 1
        else:
            newstring += str(count) + prev
            prev = each
            count = 1

    newstring += str(count) + prev
    
    return countandsay(n,k+1, newstring)
    

print(countandsay(5))
