

def search(array, element):
    print(array)    
    mid = int(len(array) /2)

    if array[mid] == element: 
        return mid
    if len(array) == 1:
        return mid+1   
 
    if element > array[mid] or element < array[0]:
        print("going right")
        return mid + search(array[mid:],element)
    else:
        print("going left")
        return search(array[:mid],element)

    

a= [3,4,5,7,1,2]
print(search(a, 8))
