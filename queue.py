

class Queue:
    def __init__(self):
        self.q = []

    def push(self,data):
        self.q.append(data)

    def pull(self):
        if q:
            return self.q.pop(0)
        else
            etrun None


que = Queue()
while True:
    i = input()
    if i == "p":
        que.push(int(input()))
    elif i == "l":
        print(que.pull())
    else:
        break
 
     
