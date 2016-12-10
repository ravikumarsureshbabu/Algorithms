
output = []

def generate(n, combi = "", opens = 0, closes = 0):

    if opens == n and closes == n:
        output.append(combi)
        return
    
    if opens < 3:
        newcombi = combi + "("
        generate(n,newcombi,opens+1,closes)
    if closes < opens:
        newcombi = combi + ")"
        generate(n,newcombi,opens,closes+1)


generate(3) 
print(output) 
