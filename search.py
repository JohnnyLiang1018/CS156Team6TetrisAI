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
        index = array[2]
        if(index == 0):
            return self.evaluate()

        piece = array[index-2]
        # for k in range(4):
        for j in range(10):
            output = self.tetris_ai.ask(piece)
            y = output[0][2][1]
            self.knowledge_base.kb_ask(["update_board",[piece,(j,0)]])
            
            
                
    
    def evaluate(self):
        return None
            

            