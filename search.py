import kb


class search:
    
    array = ["J","K",2]
    knowledge_base = None
    tetris_ai = None

    # def __init__(self):
    #    self.knowledge_base = kb.kb()
    #    self.tetris_ai = tetirs_AI.Kb()

    # def dfs(self,array):
    #    current_array = array
    #    index = current_array[2]
    #    if(index == 0):
    #        return self.evaluate()
    #    current_array[2] = current_array - 1
    #    piece = array[index-2]
    #    max_weight = 0
    #    
    #    for k in range(4):
    #    
    #        all_x_board = getXBoard(piece,k+1)
    #        y = reasoning.ask(piece)
    #        # output = self.tetris_ai.ask(piece)
            # y = output[0][2][1]
    #        board = self.knowledge_base.kb_ask(["update_board",[piece,(j,0)]])
    #        if(self.evaluate(board)>max_weight):
    #            max_weight = self.evaluate(board)
    #        self.dfs(current_array)
            
            
                
    
    def evaluate(self,board):
        height = len(board)
        width = len(board[0])
        max_height = self.get_max_height(board)
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
        print(str(max_height))
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
                    
            

            