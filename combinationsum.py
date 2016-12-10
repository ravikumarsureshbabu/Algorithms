

output = []

def combisum(arr,target,outer = 1):
    print(target)
    for each in arr:
        if target == each:
            newlist = []
            newlist.append(each)  
            if outer:
                if newlist in output:
                    continue
                else:
                    output.append(newlist)
            else:
                return newlist,True
        if target-each <= 0:
            return [],False
        else:
            arr_copy = arr.copy()
            arr_copy.remove(each)
            combi,res = combisum(arr_copy,target - each,0)
        if res:
            newlist = []
            newlist.append(each)  
            newlist += combi
            if outer:
                if newlist in output:
                    continue
                else:
                    output.append(newlist)
            else:
                return newlist,True
        else:
            if outer:
                continue
            else:
                return [],False


a = [1, 2, 7, 6, 1, 5]
combisum(a,8)
print(output)
