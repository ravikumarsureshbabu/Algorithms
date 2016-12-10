#!/usr/bin/python3

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, root, value):

        if value < root.data:
            if root.left != None:
                self.__insert(root.left, value)
            else:
                root.left = Node(value)
        else:
            if root.right != None:
                self.__insert(root.right, value)
            else:
                root.right = Node(value)

    def inorder_print(self):
        self.__inorder_print(self.root)

    def __inorder_print(self, root):
        
        if root == None:
            return
        self.__inorder_print(root.left)
        print(root.data)
        self.__inorder_print(root.right)
        
    def find_second_max(self):
        par = self.root
        tmp = par
        while(tmp.right != None):
            par = tmp
            tmp = tmp.right
        
        return par.data

    def printallpath(self):
        path = ""
        self.__printpathall(self.root,path)

    def __printpathall(self, root, path):
        if root == None:
            return
        path += str(root.data)
        if root.left == None and root.right == None:
            print(path)
    
        self.__printpathall(root.left,path)
        self.__printpathall(root.right,path)


tree = BST()
numbers = input().split()
numbers = [ int(x) for x in numbers ]

for each in numbers:
    tree.insert(each)

tree.inorder_print()
print ("second max is " + str(tree.find_second_max()))   

tree.printallpath()
        
