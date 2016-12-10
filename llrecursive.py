

class Node:
    def __init__(self,data):
        self.data = data
        self.nextt = None


def insert_ll(head,data):
    if head == None:
        head = Node(data)
    else:
        head.nextt = insert_ll(head.nextt,data)

    return head

def print_ll(head):
    if head == None:
        return
    print(head.data,end =" ")
    print_ll(head.nextt)

def delete_node(head,data):
    if head == None:
        return head
    
    if int(head.data) == data:
        head = head.nextt
    else:
        head.nextt = delete_node(head.nextt,data)

    return head

def add_node(head,data,pos,count = 1):
    if count == pos:
        newnode = Node(data)
        newnode.nextt = head
        head = newnode     
    else:
        head.nextt = add_node(head.nextt,data,pos,count + 1) 

    return head

inp = input().split()
head = None
for each in inp:
    head = insert_ll(head,each)
print_ll(head)
"""
head = delete_node(head,1)
print()
print_ll(head)
head = add_node(head,9,3)
print()
print_ll(head)
"""

