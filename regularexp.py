
def is_match(string,expression):

    str_index = 0
    index = 0
    while index < len(expression) and str_index < len(string):
        if expression[index] == ".":
            str_index += 1
            continue
        if expression[index] == "*":
            s = ""
            if index+1 < len(expression):
                s = expression[index+1]
                
            while(string[str_index] != s):
                str_index +=1
                if str_index >= len(string):
                    break
            index += 1
            continue

        if expression[index] == string[str_index]:
            str_index +=1
            index +=1
        else:
            index +=1 

    if str_index == len(string):
        return True
    else:
        return False

print(is_match("aaa","a*"))
