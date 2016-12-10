

def sumarr(arr):
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])


a = input().split()
a = [int(x) for x in a]
print(sumarr(a))
