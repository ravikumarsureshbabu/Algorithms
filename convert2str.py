
d = {
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5'
    }

def converttostring(num):
    if num == 0:
        return ""
    return converttostring(int(num/10)) + d[num % 10]

print(converttostring(1234))

