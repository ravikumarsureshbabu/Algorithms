
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        return self.q.pop(0)
    
    def isempty(self):
        return True if not self.q else False

class BinTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.que = Queue()
            self.que.enqueue(self.root)
            self.root = self.__insert__(value)

    def __insert__(self, value):
        item = self.que.dequeue()
        if item.left == None:
            item.left = Node(value)
        elif item.right == None:
            item.right = Node(value)
        else
            self.que.enqueue(item.left) 
            self.que.enqueue(item.right)
            self.__insert(value)

    def find_common_ansister(self, node1, node2):
        res, num = self.__find_common_ansister(node1,node2, self.root)
        if res:
            return num
        else
            return -1

    def __find_common_ansister__(self,node1, node2, root):
        if root == None:
            return False, None
        if root.data == node1 or root.data == node2:
            return True, None

        resl, numl = self.__find_common_ansister__(node1,node2,root.left)
        resr, numr = self.__find_common_ansister__(node1,node2,root.right)
         
        if resl == resr:
            if resl:
                return resl, root.data
            else
                return resl, None

        else:
            if resl:
                return resl, numl
            else:
                return resr, numr



        
