import numpy as np

x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(x)
print()
x = np.delete(x, (0), axis=0)
print(x)
print()
x = np.delete(x,(0), axis=0)
print(x)
x=np.insert(x,0,np.array([1,1,1]),0)


print()
print(x)


def remove_full_line(board):
    for num in range(0,20):
        row=board[num,:]
        if(row.sum()==0):
            np.delete(board,(num),axis=0)
            board=np.insert(x,0,np.array([1,1,1,1,1,1,1,1,1,1]),0)
        return board