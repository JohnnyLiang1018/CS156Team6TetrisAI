import numpy as np


board=np.append(np.ones(220),np.zeros(10)).reshape(23,10)
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
Board_length=22

def height(num):
    return Board_length - num


class Kb:

    def __init__(self):
        self.board=None

        # cut slice into small rectangle
        # slice: an m x n submatrix from getValidPosition
        #### ###################
        #### ###################
        #### ###################
        # ^
        # |
        #target rectangle:  this shape is equal to the shape of mask

    def Rec_scanner(self,board, mask_kit, height, name,type):
        boardwidth = board.shape[1]
        mask_n = mask_kit[0].shape[1]

        for num in range(0, boardwidth - mask_n +1):
            tmp = board[:, num:num + mask_n]
            if (Kb.bit_match(self,tmp,mask_kit)):
                return tuple((name,type, (height, num)))

        return None







    #cut board into slices
        #######################
        #######################
        #######################  <= unseen part of board
        #######################
        #######################

        # slice: an m x n submatrix
              #   n
        #######################
   #m   #######################   <- target slice
        #######################
        # m= m of mask shape
    def getValidPositions(self,board, shape):
        mask_kit = Mask.mask_dir.get(shape)
        result = list()
        for mask in mask_kit:
            name = mask[2]
            type = mask[3]
            mask_m = mask[0].shape[0]

            for num in range(0, Board_length - mask_m):
                slice = board[height(num) - mask_m + 1:height(num) + 1, :]
                sum = slice.sum()
                if (board.size - sum != 0 and sum >= 4):
                        shape=Kb.Rec_scanner(self,slice, mask, num, name,type)
                        if(shape != None):
                            result.append(shape)
                            break
        return result
        # is support && have space

    def ask(self,shape):
        if (self.board.sum() != 0):
            return Kb.getValidPositions(self, board, shape)

    def tell(self,result_kit):
        loca=result_kit[2]
        mask_kits=Mask.mask_dir.get(result_kit[0])
        mask_kit=mask_kits[result_kit[1]]
        target=self.board[height(loca[0]) - mask_kit[0].shape[0]+1: height(loca[0])+1, loca[1]:loca[1] + mask_kit[0].shape[1]]
        if(Kb.bit_match(self,target,mask_kit)):
            self.board[height(loca[0]) - mask_kit[0].shape[0] + 1: height(loca[0]) + 1,loca[1]:loca[1] + mask_kit[0].shape[1]]=target-mask_kit[0].real


    def bit_match(self,slice,mask_kit):
        bit_match = np.multiply(slice,mask_kit[0]).sum()
        real = bit_match.real.sum()
        support_limit = mask_kit[1]
        support = np.abs(bit_match - real)
        if( support_limit >support and real == 4):
            return True



class searchEngine:

    #number of hole
    consistent_heuristic=0





kb=Kb()
kb.board=board


kb.tell(("I",0,(0,0)))
print(kb.board)
print()
kb.tell(("J",1,(1,0)))
print(kb.board)
print()
kb.tell(("S",1,(0,5)))
print(kb.board)
print()
kb.tell(("T",1,(2,2)))
print(kb.board)
print()
print(kb.ask("T"))

