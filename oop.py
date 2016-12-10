import random 

class Snakeladder:
    board = [x for x in range(1,101,3)]
    
    def __init__(self):
        self.position = 0

    def playdice(self):
        move = random.randint(1,7)
        print("dice value", move)
        self.position += move
        print("New position will be", self.position)

    def showboard(self):
        print(self.board)

    def hackboard(self):
        self.board.remove(5)               

player1 = Snakeladder()
player1.playdice()
player2 = Snakeladder()
player2.showboard()
player2.hackboard()
player2.showboard()
player1.showboard()


                
