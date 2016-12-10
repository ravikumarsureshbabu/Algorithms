#!/usr/bin/python3

class Node:
    
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    
    def __init__(self):
        self.root = None
        self.parent = None

    def insert_node(par,value):
        parent = get_node(par)
        new = Node(value)
        parent.children.append(new)

    def get_node(value):
        return self.__get_node(value,self.root)

    def __get_node(value,root):
        if root.value == value:
            self.parent = root
            return
        if root == None:
            return     

        for child in root.children:
            __get_node(value,child)
         
    def print_all():
        self.__print_all(self.root)

    def __print_all(root):
        if root == None:
            return
        
        print(root.value)

        for child in root.children:
            __printall(child)    
