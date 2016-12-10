

class Stack:
    def __init__(self):
        self.l = []
        self.allocate()
        self.top_1 = 0
        self.top_2 = 1
        self.top_3 = 2
        self.top = [0,1,2]
        
    def allocate(self):
        for i in range(0,30):
            self.l.append('na') 

    def push_1(self,data,stack):
        self.l[self.top[stack]] = data
        self.top[stack] += 3
    
    def pop_1(self,stack):
        self.top[stack] -= 3
        return self.l[self.top[stack]]
    
s = Stack()        
