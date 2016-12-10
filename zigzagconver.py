

def zigzagconvert(string,row):

    opt = [""] * row
    curr = 0
    zig = 1
    for each in string:
        opt[curr] += each
        
        if zig:
            curr += 1
            if curr == row:
                zig = 0
                curr -= 2
        else:
            curr -= 1
            if curr < 0:
                zig = 1
                curr += 2 
    final_string = ""    
    for each in opt:
        final_string += each

    return final_string

print(zigzagconvert("PAYPALISHIRING", 3))
        
