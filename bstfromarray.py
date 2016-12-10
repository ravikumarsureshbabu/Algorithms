
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LNode:
    def __init__(self, data):
        self.data = data
        self.nextt = None

class LL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert__(self.root, value)

    def __insert__(self, root, value):
        if root == None:
            root = LNode(value)
        else:
            root.nextt = self.__insert__(root.nextt, value)

        return root

    def printlist(self):
        self.__printlist__(self.root)

    def __printlist__(self, root):
        if root == None:
            return 
        print(root.data)
        self.__printlist__(root.nextt)

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        return self.q.pop(0)

    def isempty(self):
        return True if not self.q else False
              

class BST:
    def __init__(self):
        self.root = None

    def createBSTfromarray(self, array):
        self.root = self.__BSTfromarray__(array, self.root)

    def __BSTfromarray__(self,array,root):
        if not array:
            return None
    
        mid = int(len(array)/2)

        root = Node(array[mid])

        root.left = self.__BSTfromarray__(array[:mid], root.left)
        root.right = self.__BSTfromarray__(array[mid+1:], root.right)

        return root


    def printBST(self):
        self.__printBST__(self.root)

    def __printBST__(self, root):
        if root == None:
            return
        
        self. __printBST__(root.left)
        print(root.data)
        self. __printBST__(root.right)
    
    
    def findhieght(self):
        return self.__findhieght__(self.root)

    def __findhieght__(self, root):
        if root == None:
            return -1
        return max(self.__findhieght__(root.left),self.__findhieght__(root.right)) + 1
        
    def find_common_ansister(self, node1, node2):
        return self.__find_common_ansister__(node1, node2, self.root)    
        
    def __find_common_ansister__(self, node1, node2, root):
        if root == None:
            return -1
        if node1 <= root.data and node2 >= root.data:
            return root.data
        if node1 < root.data and node2 < root.data:
            return self.__find_common_ansister__(node1, node2, root.left)
        if node1 > root.data and node2 > root.data:
            return self.__find_common_ansister__(node1, node2, root.right)
        
        
    def printLevelorder(self):
        self.que = Queue()
        self.que.enqueue(self.root)
        self.que.enqueue("M")
        self.levellist = {}
        self.__printlevelorder__()
        for key,value in self.levellist.items():
            print("key = ", key)
            value.printlist()
        

    def __printlevelorder__(self, level = 0):
        
        if self.que.isempty():
            return

        item = self.que.dequeue()
        if level not in self.levellist:
            self.levellist[level] = LL()
        
        if item == 'M':
            print("level" , level)
            level += 1
            if not self.que.isempty():
                self.que.enqueue("M")
                
        else:
            print(item.data)
            self.levellist[level].insert(item.data)
            if item.left != None:
                self.que.enqueue(item.left)
            if item.right != None:
                self.que.enqueue(item.right)
            
        self.__printlevelorder__(level)

a = [1,2,3,4,5,6,7,8,9]
b = BST()
b.createBSTfromarray(a)
print("height = " , b.findhieght() )
b.printBST()
b.printLevelorder()
print("common ansister = ", b.find_common_ansister(1, 4))
