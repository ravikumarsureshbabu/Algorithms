

def decimal2bin(num):
    if num == 1:
        return "1"

    rem = num % 2
    return decimal2bin(int(num/2)) + str(rem)

print(decimal2bin(16))
