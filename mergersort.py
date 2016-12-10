#!/usr/bin/python3

def merge(arr, start, mid, end):

    c = [ 0 for x in range(start,end+1)]
    k = 0
    i = start
    j = mid + 1

    while(i <= mid and j <= end):
        if arr[i] < arr[j]:
            c[k] = arr[i]
            i += 1
            k += 1
        else:
            c[k] = arr[j]
            j += 1
            k += 1
    while ( i <= mid):
        c[k] = arr[i]
        k += 1
        i += 1
    while ( j <= end):
        c[k] = arr[j]
        k += 1
        j += 1
    
    j = start
    for i in range(len(c)):
        arr[j] = c[i]
        j += 1

def m_s(arr, start, end):
    if start == end:
        return
    
    mid = int( (start + end) / 2)
    
    m_s(arr,start,mid)
    m_s(arr,mid+1,end)
    merge(arr,start, mid, end)

a = [3, 2, 1]
m_s(a,0,len(a)-1)
print(a)

