import kb
import tetirs_AI

class search:
    
    array = ["J","K",2]
    knowledge_base = None
    tetris_ai = None

    def __init__(self):
        self.knowledge_base = kb.kb()
        self.tetris_ai = tetirs_AI.Kb()

    def dfs(self,array):
        current_array = array
        index = current_array[2]
        if(index == 0):
            return self.evaluate()
        current_array[2] = current_array - 1
        piece = array[index-2]
        max_weight = 0
        
        for k in range(4):
        
            all_x_board = getXBoard(piece,k+1)
            y = reasoning.ask(piece)
            # output = self.tetris_ai.ask(piece)
            # y = output[0][2][1]
            board = self.knowledge_base.kb_ask(["update_board",[piece,(j,0)]])
            if(self.evaluate(board)>max_weight):
                max_weight = self.evaluate(board)
            self.dfs(current_array)
            
            
                
    
    def evaluate(self):
        return None
            

            