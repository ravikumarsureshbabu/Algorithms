#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.a = []

    def pop(self):
        if self.a:
            return self.a[-1]
        else:
            return None
    
    def push(self,value):
        self.a.append(value)

    
db = {'(':')', '{':'}', '[':']'}
open_braces = ['(','{','[']
close_braces = [')','}','[']

inp = input()
inp = list(inp)
s = Stack()
for each in inp:
    if each in open_braces:
        s.push(each)
    elif each in close_braces:
        element = s.pop()
        if element and element == open_braces[close_braces.index(each)]:
            continue
        else:
            print("Invalid sentence")
            break
if s.pop == None:
    print("valid sentence")        
else:
    print("Invalid sentence")
                
            


        
    
