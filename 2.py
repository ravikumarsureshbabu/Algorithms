
def recur():
    recur.count = 0
    if recur.count == 10:
        return    

    recur.count += 1
    print(recur.count)
        
    recur()

recur()


