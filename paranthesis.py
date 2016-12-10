

openers = ['(', '{', '[']
closers = [')', '}', ']']

class Stack:
    def __init__(self):
        self.s = []
    
    def pop(self,):
        return self.s.pop()

    def push(self,data):
        self.s.append(data)


def check_paran(string):
    stk = Stack()
    for each in string:
        if each in openers:
            stk.push(each)
        else:
            c = stk.pop()
            if c in openers and openers.index(c) == closers.index(each):
                continue
            else:
                return False

    return True

print(check_paran("()[}]"))
                
                
