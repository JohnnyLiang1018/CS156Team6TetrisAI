from tetris_AI import *
import kb

class search:
    
    array = ["J","K",2]
    knowledge_base =  Kb()


    def __init__(self):
        self.kb=Kb()


    def dfs(self,array,current_board,weight):
        current_array = array
        index = current_array[2]
        if(index == 0):
            return self.evaluate(current_board)
        current_array[2] = index - 1
        piece = array[index-2]
        min_weight = weight
        
        for k in range(4):
            for x in range(10):

                at_x_board = valid_y(kb.board,x,piece,k)
                if(at_x_board.all() == -1):
                    break
                
                # y = reasoning.ask(piece)
                # output = self.tetris_ai.ask(piece)
                # y = output[0][2][1]
                # board = self.knowledge_base.kb_ask(["update_board",[piece,(j,0)]])
                at_x_weight = self.evaluate(at_x_board)
                if(at_x_weight > min_weight):
                    # perform cutoff
                    break
                
                self.dfs(current_array,at_x_board,at_x_weight)
            
            
                
    
    def evaluate(self,board):
        height = len(board)
        width = len(board[0])
        # max_height = self.get_max_height(board)
        holes = 0
        pits = 0
        for j in range(height-2):
            for i in range(width-2):
                if(board[j][i] == 1 and board[j+1][i] == 0 and board[j+2][i] == 1):
                    holes += 1
                if(board[j][i] == 1 and board[j][i+1] == 0 and board[j][i+2] == 1):
                    pits += 1
                if(j == height - 3 and board[j+1][i] == 1 and board[j+2][i] == 0):
                    holes += 1
                if(i == 0 and board[j][i] == 0 and board[j][i+1] == 1):
                    pits += 1
                if(i == width - 3 and board[j][i+1] == 1 and board[j][i+2] == 0):
                    pits += 1
        weight = holes * 5 + pits * 2
        print(str(weight))
        return weight

                    
    
    def get_max_height(self,board):
        height = len(board)
        width = len(board[0])
        max_height = 0
        for j in range(height):
            for i in range(width):
                if (board[j][i] == 1):
                    max_height = height - j
                    return max_height
        return max_height
                    
            

            