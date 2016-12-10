
def serialize(strings):
    output = ""
    for each in strings:
        output += str(len(each)) + each

    return output

def deserilaze(string):
    output = []
    start = 0
    while(start < len(string)):
        print(start)
        l = int(string[start])
        start += 1
        end = start + l 
        new = string[start:end]
        output.append(new)
        start = end 
    return output

a = [ 'a' , 'bb', 'ccc', 'dddd' ]
o = serialize(a)
print(o)
print(deserilaze(o))
