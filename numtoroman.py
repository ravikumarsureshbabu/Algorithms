
d = {
            1 :   'I',
            5 :   'V',
            10:   'X',
            50:   'L',
            100:  'C',
            500:  'D',
            1000: 'M'             

    }


e = {
        'I':    1,
        'V':    5,
        'X':    10,
        'L':    50,
        'C':    100,
        'D':    500,
        'M':    1000
}  

def convert2roman(num,rom = ""):
    
    if num == 0:
        return rom

    digits = len(str(num))
    multiple = 10 ** (digits -1)
    
    cur = int(num / multiple)
    cur = cur * multiple
    num = num % multiple

    halfway = 5 * multiple
    fullway = 10 * multiple

    if cur + multiple == halfway:
        rom += d[multiple] + d[halfway]
    elif cur + multiple == fullway:
        rom += d[multiple] + d[fullway]
    else:
        if cur >= halfway:
            cur -= halfway
            rom += d[halfway]
        if cur > 0:
            rom += d[multiple] * int(cur / multiple)
    return convert2roman(num,rom)
    

def convert2numeral(rom):

    cur = 0
    num = 0
        
    while cur < len(rom):
        if cur+1 == len(rom):
            num += e[rom[cur]]
        elif e[rom[cur]] > e[rom[cur+1]]:
            num += e[rom[cur]]
            cur += 1
        elif e[rom[cur]] < e[rom[cur+1]]:
            num += (e[rom[cur + 1]] - e[rom[cur]])
            cur += 2
    return num


a = convert2roman(499)
print(a)
a = convert2numeral(a)
print(a) 
