

class Queue:
    def __init__(self):
        self.q = []

    def push(self, value):
        self.q.append(value)

    def pop(self):
        return self.q.pop(0)

    def clear(self):
        self.q = []

class Bintree:
    def __init__(self):
        self.tree = {}
        self.root = None
        self.queue = Queue()

    def insert(self,value):
        if self.root is None:
            self.root = value
            self.tree[value] = []

        else:
            self.queue.push(self.root)
            self.__insert__(value)
            self.queue.clear()

    def __insert__(self, value):
        root = self.queue.pop()
        if len(self.tree[root]) == 2:     # if root has 2 children already   
            for each in self.tree[root]:  # 
                self.queue.push(each)

            self.__insert__(value)
        else:
            self.tree[root].append(value)
            self.tree[value] = []

    def printall(self):
        print(self.tree)

    def find_common_ansister(self, node1, node2):
        return self.__find_common_ansister__(node1,node2,self.root)
        
    def __find_common_ansister__(self, node1, node2, root):
        if root == None:
            return False, None 
        if root == node1 or root == node2:
            return True,None
        d = {}
        for each in self.tree[root]:
            d[each].res, d[each].num = self.__find_common_ansister__(node1,node2, each)
 
        if resl == resr:
            if resl:
                return True, root
            else:
                return False,None
        else:
            if resl:
                return True, numl
            else:
                return True, numr  
            

bt = Bintree()
ip = input().split()
for each in ip:
    bt.insert(each)


bt.printall()
bt.find_common_ansister(3,5)
    
          
