

def remove_duplicates(array):
    track = array[0]
    for each in array[1:]:
        if track == each:
            array.remove(each)
        else:
            track = each

    return array,len(array)

a = [1,1,2,4,4,6,7,7]
print(remove_duplicates(a))
