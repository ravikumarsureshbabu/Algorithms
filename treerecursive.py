

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,node = None):
        self.root = node

    def insert_node(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root = self.__insert_node__(self.root,data)

    def __insert_node__(self,root,data):
        if root == None:
            root = Node(data)
            return root        

        if data <= root.data:
            root.left = self.__insert_node__(root.left,data)
        else:
            root. right = self.__insert_node__(root.right,data)
    
        return root


    def print_inorder(self):
        self.__print_inorder__(self.root)

    def __print_inorder__(self,root):
        if root == None:
            return 
        self.__print_inorder__(root.left)
        print(root.data, end = " ")
        self.__print_inorder__(root.right)


t = Tree()
inp = input().split()
for each in inp:
    t.insert_node(each)

t.print_inorder()


