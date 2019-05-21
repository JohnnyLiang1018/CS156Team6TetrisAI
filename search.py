from tetris_AI import *
import kb

class search:
    
    array = ["J","K",2]
    knowledge_base = None
    tetris_logic = None

    def __init__(self):
        self.knowledge_base = kb.kb()
        self.tetris_logic = Kb()

    def dfs(self,array,current_board,weight):
        current_array = array
        index = current_array[2]
        if(index == 2):
            self.initial_board = current_board
        if(index == 1):
            self.one_piece_board = current_board
        if(index == 0):
            self.tetris_logic.board = self.board
            return self.evaluate(current_board)
        print("index " + str(index))
        
        current_array[2] = index - 1
        piece = current_array[2-index]
        print("piece " + piece)
        min_weight = weight
        
        for k in range(4):
            for x in range(10):
                at_x_board = self.tetris_logic.valid_y(x,piece,k)
                if(at_x_board == -1).all():
                    break
                # y = reasoning.ask(piece)
                # output = self.tetris_ai.ask(piece)
                # y = output[0][2][1]
                # board = self.knowledge_base.kb_ask(["update_board",[piece,(j,0)]])
                at_x_weight = self.evaluate(at_x_board)
                if(at_x_weight > min_weight):
                    # perform cutoff
                    print("cutoff")
                    continue
                print("recursive")
                
                self.dfs(current_array,at_x_board,at_x_weight)
            
            
                
    
    def evaluate(self,board):
        height = len(board)
        width = len(board[0])
        # max_height = self.get_max_height(board)
        holes = 0
        pits = 0
        for j in range(height-2):
            count = 0
            for i in range(width-2):
                count = count + board[height-1-j][i]

                #check from the bottom to the top
                if(board[height-1-j][i] == 1 and board[height-2-j][i] == 0 and board[height-3-j][i] == 1):
                    holes += 1
                if(board[height-1-j][i] == 1 and board[height-1-j][i+1] == 0 and board[height-1-j][i+2] == 1):
                    pits += 1
                if(j == 0 and board[height-1][i] == 0 and board[height-2][i] == 1):
                    holes += 1
                if(i == 0 and board[height-1-j][i] == 0 and board[height-1-j][i+1] == 1):
                    pits += 1
                if(i == width - 3 and board[height-1-j][i+1] == 1 and board[height-1-j][i+2] == 0):
                    pits += 1
            # if the entire row is empty, this function is finished
            if(count == 0):
                print("eval finished")
                break
        weight = holes * 5 + pits * 2
        print(board)
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
                    
            

            