############################
# Controller class
# Connect the game code with the AI code
# for delivering the current information of the board to the AI
# and getting the result back from AI
# Need to wait for the completion of the AI code to establish real connection
# and get it show on the board
############################
import tetromino
import tetris_AI

currentCube = None
screen_color_matrix = None
class Controller:
    def __init__(self):
        self.blocks=list()
        self.boards=list()

    def push(self,item,num):
        if(num==0): self.boards.append(item)
        if(num==1): self.blocks.append(item)
        print(item)

    def pop(self,num):
        if (num == 0): return self.boards.pop(0)
        if (num == 1): return self.blocks.pop(0)




controller=Controller()
kb=tetris_AI.Kb(controller)

game=tetromino.game(controller)
game.main()




