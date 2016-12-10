

output = []
def combisum(arr,target,l = []):
    for each in arr:
        if each == target:
            l_new = l.copy()
            l_new.append(each)
            #print(target, l_new)
            l_new = sorted(l_new)
            if l_new not in output:    
                output.append(l_new)
        else:
            if target - each >= 0:

                arr_new = arr.copy()
                #arr_new.remove(each)
                l_new = l.copy()
                l_new.append(each)
            
                combisum(arr_new, target - each, l_new)

a = [10, 1, 2, 7, 6, 1, 5]
combisum(a,8)
print(output)            
