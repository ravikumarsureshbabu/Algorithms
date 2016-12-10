
class Tree:
    def __init__(self):
        self.tree = {}

    def construct(self,node1,node2): # edge as as input
        if node1 in self.tree:
            self.tree[node1].append(node2)
        else:
            child = []
            child.append(node2)
            self.tree[node1] = child

    def printtreeasitis(self):
        print(self.tree)

    def printdfs(self):
        self.__printdfs__()

t = Tree()
while True:
    ip = input().split()
    if ip == 'e':
        break
    ip = [int(x) for x in ip]
    t.construct(ip[0],ip[1])
    t.construct(ip[1],ip[0])
    
    t.printtreeasitis() 
