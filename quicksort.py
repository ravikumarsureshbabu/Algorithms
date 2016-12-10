#!/usr/bin/python3


def partition(arr, start, end):
    pivot = arr[start]
    for i in range(start+1,end+1):
        if 






def quick_sort(arr,start,end):
    if start >= end:
        return

    pivot_index = partition(arr,start,end)
    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)
