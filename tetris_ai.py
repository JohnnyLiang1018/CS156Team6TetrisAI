import numpy as np


board=np.append(np.ones(220),np.zeros(10)).reshape(23,10)


class Mask:
    I0 = (np.array([[1, 1, 1, 1],
                    [1j, 1j, 1j, 1j]]), 4,"I0")

    I1 = (np.array([[1],
                    [1],
                    [1],
                    [1],
                    [1j]]), 1,"I1")

    L0 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3,"L0")

    L1 = (np.array([[1, 0],
                    [1, 0],
                    [1, 1],
                    [1j, 1j]]), 2,"L1")

    L2 = (np.array([[1, 1, 1],
                    [1, 1j, 1j],
                    [1j, 0, 0]]), 3,"L2")

    L3 = (np.array([[1, 1],
                    [1j, 1],
                    [0, 1],
                    [0, 1j]]), 2,"L3")

    J0 = (np.array([[1, 1, 1],
                    [1j, 1j, 1],
                    [0, 0, 1j]]), 3,"J0")

    J1 = (np.array([[0, 1],
                    [0, 1],
                    [1, 1],
                    [1j, 1j]]), 2,"J1")

    J2 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3,"J2")

    J3 = (np.array([[1, 1],
                    [1, 1j],
                    [1, 0],
                    [1j, 0]]), 2,"J3")

    S0 = (np.array([[0, 1, 1],
                    [1, 1, 1j],
                    [1j, 1j, 0]]), 3,"S0")

    S1 = (np.array([[1, 0],
                    [1, 1],
                    [1j, 1],
                    [0, 1j]]), 2,"S1")

    Z0 = (np.array([[1, 1, 0],
                    [1j, 1, 1],
                    [0, 1j, 1j]]), 3,"Z0")

    Z1 = (np.array([[0, 1],
                    [1, 1],
                    [1, 1j],
                    [1j, 0]]), 2,"Z1")

    mask_dir = {"I": list([I0, I1]),

                "L": list([L0, L1, L2, L3]),

                "J": list([J0, J1, J2, J3]),

                "S": list([S0, S1]),

                "Z": list([Z0, Z1])
                }






Board_width=10
Board_length=22

def height(num):
    return Board_length - num


class Kb:


    def Rec_scanner(board, mask_kit, height, name):
        mask = mask_kit[0]
        num_of_support = mask_kit[1]

        boardwidth = board.shape[1]
        mask_n = mask.shape[1]
        result = list()
        for num in range(0, boardwidth - mask_n + 1):
            tmp = board[:, num:num + mask_n]

            bit_match = np.multiply(mask, tmp).sum()
            real = bit_match.real
            if (real == 4 and np.abs(bit_match - real) < num_of_support):
                result.append(tuple((name, (height, num))))
        return result


    def getValidPositions(board, shape):
        mask_kit = Mask.mask_dir.get(shape)
        result = list()

        for mask in mask_kit:
            name = mask[2]
            mask_m = mask[0].shape[0]
            mask_result = list()
            for num in range(0, Board_length - mask_m):
                slice = board[height(num) - mask_m + 1:height(num) + 1, :]

                sum = slice.sum()
                if (slice.size - sum != 0 and sum >= 4):
                    mask_result.extend(Kb.Rec_scanner(slice, mask, num, name))

            result.extend(mask_result)

        return result


board=np.append(np.random.randint(2, size=220),np.zeros(10)).reshape(23,10)
print(board)


print(Kb.getValidPositions(board,"L"))
