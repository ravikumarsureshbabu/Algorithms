

phone = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
        }

output = []

def combi(keystrokes, combination = "", pos = 0):

    if len(combination) == len(keystrokes):
        output.append(combination)
        return

    for each in phone[keystrokes[pos]]:
        newcombi = combination + each
        combi(keystrokes, newcombi, pos+1)

combi("236")
print(output)     
