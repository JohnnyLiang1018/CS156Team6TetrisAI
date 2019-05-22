############################
# Controller class
# Connect the game code with the AI code
# for delivering the current information of the board to the AI
# and getting the result back from AI
# Need to wait for the completion of the AI code to establish real connection
# and get it show on the board
############################

import tetromino
from tetris_AI import *
import numpy as np

board_1=np.append(np.ones(200),np.zeros(10)).reshape(21,10)

class KB:
    def __init__(self):
        self.controller = Controller()
        self.board = np.append(np.ones(200),np.zeros(10)).reshape(21,10)

class Controller:
    def __init__(self):
        self.boards=list()
        self.current_board=None
        self.blocks=list() # list
        self.current_block=None
        self.kb = None
        self.game = None
        self.push(board_1,0) #push an empty board


    def push(self,item,num):
        print(item)
        if(num==0):
            self.boards.append(item)
            print("Boards:",len(self.boards))
        if(num==1):
            self.blocks.append(item)
            #print(self.blocks)
            # when push a block to the list, list size bigger than 2 (a limit number), use the current board in the controller
            # call AI function to get boards
            if(len(self.blocks)>2):
                tempBlocks = []
                tempBlocks.append(self.blocks.pop(1))
                bestBoards = depth_first_limit(tempBlocks, self.current_board, 1)
                self.push(bestBoards,0) # put the boars to the boards



    def pop(self, num):
        if (num == 0):
            if (len(self.boards) != 0):
                self.current_board = self.boards.pop(0)
            kb.board = self.current_board # update the current board
            return self.current_board
        if (num == 1):
            if (len(self.blocks) != 0):
                self.current_block = self.blocks.pop(0)
            return self.current_block



controller=Controller()
kb = KB()

controller.kb = kb # controller know the KB
controller.push(kb.board,0) # put a default board of the KB to the controller
kb.controller = controller # KB know the controller

game=tetromino.game(controller)
controller.game = game # controller know the game object
game.main()


