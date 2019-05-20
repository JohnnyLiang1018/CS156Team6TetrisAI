############################
# Controller class
# Connect the game code with the AI code
# for delivering the current information of the board to the AI
# and getting the result back from AI
# Need to wait for the completion of the AI code to establish real connection
# and get it show on the board
############################
import kb

currentCube = None
screen_color_matrix = []
knowledge_base = kb.kb()
class Controller:
    def __init__(self):
        self.currentCube =None
        self.currentCube = None
        self.history=None

    def setCurrentCube(self,currentCube):
        currentCube = currentCube
        # print to check if the current piece object is get by the controller
        # prepare to send
        #print('get current cube', currentCube)
        knowledge_base.kb_ask(["display_board",""])

    def updateCurrentCube(self,x, y, dir):
        currentCube.dir = dir
        currentCube.center = (x, y)

    def getCurrentCube(self):
        return currentCube

    def setMatrix(self,matrix):
        screen_color_matrix = matrix
        # print('get current matrix', screen_color_matrix)

    def updateMatrix(self,):
        currentCube.draw()
        for cube in currentCube.get_all_gridpos():
            screen_color_matrix[cube[0]][cube[1]] = currentCube.color

    def getMatrix(self):
        # print to check if the current broad information is get by the controller
        # prepare to send
        print('get current matrix', screen_color_matrix)
        return screen_color_matrix

