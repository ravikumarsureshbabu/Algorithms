#!/usr/bin/python3


class Node:
    
    def __init__(self,value):
        self.data = value
        self.nextt = None

def create_ll(head, value):
    if None == head:
        head = Node(value)
    else:
        tmp = head
        while None != tmp.nextt:
            tmp = tmp.nextt

        tmp.nextt = Node(value)

    return head

def reverse_ll(head):
    prev = None
    curr = head
    
    while(curr != None):
        tmp = curr.nextt
        curr.nextt = prev
        prev = curr
        curr = tmp

    return prev

def delete_last_nth_node(head, n):
    tmp = head
    prev = head
    tmp2 = head
    count = 1
    while tmp.nextt != None:
        print("main node %s" %(tmp.data))
        tmp = tmp.nextt
        if count >= n:
            prev = tmp2
            tmp2 = tmp2.nextt 
            print("follwer node %s" %(tmp2.data))
        count += 1
    
    if tmp2 == head:
        head = head.nextt
    else:
        prev.nextt = tmp2.nextt
    
    return head
    

def swapnodes(head):
    tmp = head
    while tmp != None and tmp.nextt != None:
        first = tmp
        second = tmp.nextt
        if first == head:
            head = second
        else:
            prev.nextt = second
        tmp = second.nextt
        second.nextt = first
        first.nextt = tmp
        prev = first

    return head  
     
    

def print_ll(head):
    while(head != None):
        print(head.data)
        head = head.nextt

head = None
ip = input().split()
for each in ip:
    head = create_ll(head, int(each))

#head = reverse_ll(head)

#print_ll(head)
        
#head = delete_last_nth_node(head,3)    
head = swapnodes(head)
print_ll(head)
        
