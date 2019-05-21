import numpy as np


board=np.append(np.ones(200),np.zeros(10)).reshape(21,10)
counter=0

class Mask:
    I0 = (np.array([[1, 1, 1, 1],
                    [1j, 1j, 1j, 1j]]), 4,"I",0)

    I1 = (np.array([[1],
                    [1],
                    [1],
                    [1],
                    [1j]]), 1,"I",1)

    L0 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3,"L",0)

    L1 = (np.array([[1, 0],
                    [1, 0],
                    [1, 1],
                    [1j, 1j]]), 2,"L",1)

    L2 = (np.array([[1, 1, 1],
                    [1, 1j, 1j],
                    [1j, 0, 0]]), 3,"L",2)

    L3 = (np.array([[1, 1],
                    [1j, 1],
                    [0, 1],
                    [0, 1j]]), 2,"L",3)

    J0 = (np.array([[1, 1, 1],
                    [1j, 1j, 1],
                    [0, 0, 1j]]), 3,"J",0)

    J1 = (np.array([[0, 1],
                    [0, 1],
                    [1, 1],
                    [1j, 1j]]), 2,"J",1)

    J2 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3,"J",2)

    J3 = (np.array([[1, 1],
                    [1, 1j],
                    [1, 0],
                    [1j, 0]]), 2,"J",3)

    S0 = (np.array([[0, 1, 1],
                    [1, 1, 1j],
                    [1j, 1j, 0]]), 3,"S",0)

    S1 = (np.array([[1, 0],
                    [1, 1],
                    [1j, 1],
                    [0, 1j]]), 2,"S",1)

    Z0 = (np.array([[1, 1, 0],
                    [1j, 1, 1],
                    [0, 1j, 1j]]), 3,"Z",0)

    Z1 = (np.array([[0, 1],
                    [1, 1],
                    [1, 1j],
                    [1j, 0]]), 2,"Z",1)
    O = (np.array([[1,1],
                  [1,1],
                  [1j,1j]]), 2 ,"O",0)

    T0 = (np.array([[0,1,0],
                 [1,1,1],
                 [1j,1j,1j]]), 3,"T",0)

    T1 = (np.array([[1,0],
                 [1,1],
                 [1,1j],
                 [1j,0]]), 2 ,"T",1)

    T2 =(np.array([[1,1,1],
                  [1j,1,1j],
                  [0,1j,0]]), 3,"T",2)
    T3= (np.array([[0,1],
                   [1,1],
                   [1j,1],
                   [0,1j]]), 2 ,"T",3)




    mask_dir = {
                "I": list([I0, I1]),
                "L": list([L0, L1, L2, L3]),
                "J": list([J0, J1, J2, J3]),
                "S": list([S0, S1]),
                "Z": list([Z0, Z1]),
                "T": list([T0,T1,T2,T3]),
                "O": list([O])

                }


Board_width=10
Board_length=20

def height(num):
    return Board_length - num

    # vertical cut&& horizontal cut and use it to bit_match
def bit_match(slice, mask_kit):
    bit_match = np.multiply(slice, mask_kit[0]).sum()
    real = bit_match.real.sum()
    support_limit = mask_kit[1]
    support = np.abs(bit_match - real)
    if (support_limit > support and real == 4):
        return True
    return False

def get_mask_kit(type, rotation):
    return Mask.mask_dir.get(type)[rotation]

def get_shape( type, rotation):
    shape = get_mask_kit(type, rotation)[0].shape
    return (shape[0] - 1, shape[1])

def vertical_cut(board,mask_kit,x):
    mask_n=mask_kit[0].shape[1]
    slice=board[:,x:x + mask_n]
    return slice
def vertical_cut_range(mask):
   return range(0, Board_length - mask[0].shape[1])


def horizontal_cut(board,mask_kit,y):
    mask_m=mask_kit[0].shape[0]
    slice= board[height(y)-mask_m+1:height(y)+1,:]
    return slice

def horizontal_cut_range(mask,direction=1):
    if(direction==1):return range(0, Board_width - mask[0].shape[0] + 1)
    if(direction==-1):return range(Board_width - mask[0].shape[0] + 1,0)


def get_sub_matrix(board,mask_kit,x,y):
    return horizontal_cut(vertical_cut(board, mask_kit, x), mask_kit, y)

def replace_sub_matrix(board,mask_kit,x,y):

    board[height(y) - mask_kit[0].shape[0] + 1: height(y) + 1,x:x + mask_kit[0].shape[1]] -= mask_kit[0].real

def stk(board):
    board-=1
    board*=-1
    board+=0

    return np.append(board,np.zeros(10)).reshape(Board_length+1,Board_width)

def kts(board):
    board = board[:20, :]
    board = board - 1
    board *= -1
    return board + 0

#auto transfer board between kb and search
def wrap(board):
    if(board.shape[0]==Board_length+1): return kts(board)
    if(board.shape[0]==Board_length): return stk(board)
    return None
############################################


def clone(board):
    x=np.array([])
    np.copyto(board,x)
    return x


def valid_y(board,x,shape,rotation):
    mask_kit=get_mask_kit(shape,rotation)
    width=mask_kit[0].shape[1]
    if(width+x>Board_width or x<0):return -1
    slice=vertical_cut(board,mask_kit,x)
    for y in vertical_cut_range(mask_kit):
        area=horizontal_cut(slice,mask_kit,y)
        if(bit_match(area,mask_kit)):
            tmp=clone(board)
            replace_sub_matrix(tmp, mask_kit, x, y)

            return wrap(tmp)



class Kb:

    def __init__(self,controller):
        self.board=np.append(np.ones(220),np.zeros(10)).reshape(23,10)
        self.init_board = np.append(np.ones(220),np.zeros(10)).reshape(23,10)
        self.one_piece_board = np.append(np.ones(220),np.zeros(10)).reshape(23,10)
        #self.controller=controller
        self.controller=controller
        self.controller.push(board,0)


    def store_init_board(self):
        np.copyto(self.init_board,self.board)
    
    def store_one_piece_board(self):
        np.copyto(self.one_piece_board,self.board)

    def load_init_board(self):
        np.copyto(self.board,self.load_init_board)
    
    def load_one_piece_board(self):
        np.copyto(self.board,self.one_piece_board)




    def tell(self,result_kit):
        location=result_kit[2]
        mask_kits=Mask.mask_dir.get(result_kit[0])
        mask_kit=mask_kits[result_kit[1]]
        target = get_sub_matrix(self.board, mask_kit,location[1], location[0])
        if (bit_match(target, mask_kit)):
            replace_sub_matrix(self.board, mask_kit, location[1], location[0])


