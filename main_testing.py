import search
import numpy as np
from tetris_AI import *

board = np.append(np.ones(220),np.zeros(10)).reshape(23,10)
search = search.search()
search.dfs(["T","T",2],board,5)
#kb= Kb()
#kb.tell(("T",0,(0,0)))
#x = kb.valid_y(2,"T",0)
#print(x)