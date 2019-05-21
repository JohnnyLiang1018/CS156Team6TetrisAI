############################
# Controller class
# Connect the game code with the AI code
# for delivering the current information of the board to the AI
# and getting the result back from AI
# Need to wait for the completion of the AI code to establish real connection
# and get it show on the board
############################
import kb
import tetromino
from tetris_AI import *


class Controller:
    def __init__(self):
        self.boards=list()
        self.current_board=None
        self.blocks=list()
        self.current_block=None

    def push(self,item,num):
        if(num==0): self.boards.append(item)
        if(num==1): self.blocks.append(item)

    def pop(self, num):
        if (num == 0):
            if (len(self.boards) != 0): self.current_board = self.boards.pop(0)
            return self.current_board
        if (num == 1):
            if (len(self.blocks) != 0): self.current_block = self.blocks.pop(0)
            return self.current_block


controller=Controller()
kb=Kb(controller)

game=tetromino.game(controller)
game.main()




