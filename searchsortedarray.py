

def search_in_sorted_array(array,data):
    first = array[0]

    search(array,first,data)


def search(array,first,data):
    mid = int( len(array) / 2 )

    if array[mid] == data:
        print("Found")
    else:
            
