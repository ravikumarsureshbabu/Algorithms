
class Node:
    def __init__(self,data):
        self.data = data
        self.nextt = None

class Circulatll:
    def __init__(self,data,startofloop = 1):
        if data:
            self.head = Node(data)
            self. count = 1
        else:
            self.head = None
            self. count = 0

        self.loopstart = startofloop
        if startofloop = 1:
            self.loopstartnode = self.head
            if self.head != None:
                self.head.nextt = self.head
                self.inloop = True
        else:
            self.loopstartnode = None
                self.inloop = False
            

    def insert(self,data):
        if self.head = None:
            self.head = Node(data)
            self. count = 1
        else:
            tmp = self.head 
            if self.inloop:
                track_ptr = 0 
                while True:
                    while tmp.nextt != self.loopstartnode:
                        tmp = tmp.nextt
                    track_ptr += 1
                    if tack_ptr == 1:
                        tmp = tmp.nextt
                    else:
                        break 
            else:
                while(tmp.nextt != None):
                    tmp = tmp.nextt
    
            tmp.nextt = Node(data)
            self.count += 1

            if self.count == self.loopstart:
                self.inloop = True
            
            if self.inloop:
                tmp.nextt.nextt = self.loopstatnode



    def get_the_start_of_loop(self):
        
        
