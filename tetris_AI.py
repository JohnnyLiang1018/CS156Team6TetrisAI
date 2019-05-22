import numpy as np
import random
import copy
import math

board_1 = np.append(np.ones(200), np.zeros(10)).reshape(21, 10)


class Mask:
    I0 = (np.array([[1, 1, 1, 1],
                    [1j, 1j, 1j, 1j]]), 4, "I", 0)

    I1 = (np.array([[1],
                    [1],
                    [1],
                    [1],
                    [1j]]), 1, "I", 1)

    L0 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3, "L", 0)

    L1 = (np.array([[1, 0],
                    [1, 0],
                    [1, 1],
                    [1j, 1j]]), 2, "L", 1)

    L2 = (np.array([[1, 1, 1],
                    [1, 1j, 1j],
                    [1j, 0, 0]]), 3, "L", 2)

    L3 = (np.array([[1, 1],
                    [1j, 1],
                    [0, 1],
                    [0, 1j]]), 2, "L", 3)

    J0 = (np.array([[1, 1, 1],
                    [1j, 1j, 1],
                    [0, 0, 1j]]), 3, "J", 0)

    J1 = (np.array([[0, 1],
                    [0, 1],
                    [1, 1],
                    [1j, 1j]]), 2, "J", 1)

    J2 = (np.array([[0, 0, 1],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3, "J", 2)

    J3 = (np.array([[1, 1],
                    [1, 1j],
                    [1, 0],
                    [1j, 0]]), 2, "J", 3)

    S0 = (np.array([[0, 1, 1],
                    [1, 1, 1j],
                    [1j, 1j, 0]]), 3, "S", 0)

    S1 = (np.array([[1, 0],
                    [1, 1],
                    [1j, 1],
                    [0, 1j]]), 2, "S", 1)

    Z0 = (np.array([[1, 1, 0],
                    [1j, 1, 1],
                    [0, 1j, 1j]]), 3, "Z", 0)

    Z1 = (np.array([[0, 1],
                    [1, 1],
                    [1, 1j],
                    [1j, 0]]), 2, "Z", 1)
    O = (np.array([[1, 1],
                   [1, 1],
                   [1j, 1j]]), 2, "O", 0)

    T0 = (np.array([[0, 1, 0],
                    [1, 1, 1],
                    [1j, 1j, 1j]]), 3, "T", 0)

    T1 = (np.array([[1, 0],
                    [1, 1],
                    [1, 1j],
                    [1j, 0]]), 2, "T", 1)

    T2 = (np.array([[1, 1, 1],
                    [1j, 1, 1j],
                    [0, 1j, 0]]), 3, "T", 2)
    T3 = (np.array([[0, 1],
                    [1, 1],
                    [1j, 1],
                    [0, 1j]]), 2, "T", 3)

    mask_dir = {
        "I": list([I0, I1]),
        "L": list([L0, L1, L2, L3]),
        "J": list([J0, J1, J2, J3]),
        "S": list([S0, S1]),
        "Z": list([Z0, Z1]),
        "T": list([T0, T1, T2, T3]),
        "O": list([O])

    }


Board_width = 10
Board_length = 20


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


def get_shape(type, rotation):
    shape = get_mask_kit(type, rotation)[0].shape
    return (shape[0] - 1, shape[1])


def vertical_cut(board, mask_kit, x):
    mask_n = mask_kit[0].shape[1]
    slice = board[:, x:x + mask_n]
    return slice


def vertical_range(mask):
    return range(0, Board_length - mask[0].shape[0])


def horizontal_cut(board, mask_kit, y):
    mask_m = mask_kit[0].shape[0]
    slice = board[height(y) - mask_m + 1:height(y) + 1, :]
    return slice


def horizontal_range(mask):
    return range(0, Board_width - mask[0].shape[1] + 1)


def get_sub_matrix(board, mask_kit, x, y):
    return horizontal_cut(vertical_cut(board, mask_kit, x), mask_kit, y)


def replace_sub_matrix(board, mask_kit, x, y):
    board[height(y) - mask_kit[0].shape[0] + 1: height(y) + 1, x:x + mask_kit[0].shape[1]] -= mask_kit[0].real


def stk(board):
    board -= 1
    board *= -1
    board += 0

    return np.append(board, np.zeros(10)).reshape(Board_length + 1, Board_width)


def kts(board):
    board = board[:20, :]
    board = board - 1
    board *= -1
    return board + 0


# auto transfer board between kb and search
def wrap(board):
    if (board.shape[0] == Board_length + 1): return kts(board)
    if (board.shape[0] == Board_length): return stk(board)
    return None


############################################


def clone(board):
    x = np.zeros(board.size).reshape(21, 10)

    np.copyto(x, board)
    return x


def valid_y_1(board, x, shape, rotation):
    mask_kit = get_mask_kit(shape, rotation)
    width = mask_kit[0].shape[1]
    slice = vertical_cut(board, mask_kit, x)
    for y in vertical_range(mask_kit):
        area = horizontal_cut(slice, mask_kit, y)
        if (bit_match(area, mask_kit)):
            result = board
            replace_sub_matrix(result, mask_kit, x, y)
            return wrap(result)


def valid_y(board, x, mask_kit):
    slice = vertical_cut(board, mask_kit, x)
    for y in vertical_range(mask_kit):
        area = horizontal_cut(slice, mask_kit, y)
        if (bit_match(area, mask_kit)):
            result = clone(board)

            replace_sub_matrix(result, mask_kit, x, y)
            return result


def not_valid_x(x, shape, rotation):
    mask_kit = get_mask_kit(shape, rotation)
    width = mask_kit[0].shape[1]
    if (width + x > Board_width or x < 0):
        return True

    return False

def remove_full_line(board):

    for num in range(0,20):
        x=board[num:num+1, :]

        if x.sum() == 0:
            print("enter")
            board=np.delete(board,num,axis=0)
            board=np.insert(board, 0, np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0)
    return board










def depth_first_limit(types, board, weight):
    max_height = 0
    min_height = 0

    def get_max_height(board):
        height = len(board)
        width = len(board[0])
        max_height = 0
        for j in range(height):
            for i in range(width):
                if (board[j][i] == 0):
                    max_height = height - j
                    return max_height
        return max_height

    def valid_y(board, x, mask_kit):
        slice = vertical_cut(board, mask_kit, x)
        for y in vertical_range(mask_kit):
            area = horizontal_cut(slice, mask_kit, y)
            if (bit_match(area, mask_kit)):
                result = clone(board)

                replace_sub_matrix(result, mask_kit, x, y)
                return result

    def evaluate(board):
        height = Board_length
        width = Board_width
        max_height = get_max_height(board)
        holes = 0
        pits = 0
        for j in range(height - 2):
            count = 0
            for i in range(width - 2):
                count = count + board[height - 1 - j][i]

                # check from the bottom to the top
                if (board[height - 1 - j][i] == 0 and board[height - 2 - j][i] == 1 and board[height - 3 - j][i] == 0):
                    holes += 1
                if (board[height - 1 - j][i] == 0 and board[height - 1 - j][i + 1] == 1 and board[height - 1 - j][
                    i + 2] == 0):
                    pits += 1
                if (j == 0 and board[height - 1][i] == 1 and board[height - 2][i] == 0):
                    holes += 1
                if (i == 0 and board[height - 1 - j][i] == 1 and board[height - 1 - j][i + 1] == 0):
                    pits += 1
                if (i == width - 3 and board[height - 1 - j][i + 1] == 0 and board[height - 1 - j][i + 2] == 1):
                    pits += 1
            # if the entire row is empty, this function is finished
            if (count == 10):
                break
        weight = holes * 5 + pits * 2 + math.exp(max_height)/25

        return weight

    class Best:
        def __init__(self, weight):
            self.route = list()
            self.global_minimize_weight = weight

        def update(self, newweight, new_route):
            if (self.global_minimize_weight > newweight):
                self.global_minimize_weight = newweight
                self.route = copy.deepcopy(new_route)

    best = Best(weight)

    route = list()

    def helper(types, board, weight, route, best):

        # at the end of the tree try to update route,
        # if it is the best route then update success, other wise keep current best route
        if (len(types) == 0):
            best.update(weight, route)
            return
        else:
            shapes = Mask.mask_dir.get(types[0])
            for shape in shapes:
                for x in horizontal_range(shape):
                    new_board = valid_y(board, x, shape)
                    new_weight = evaluate(new_board)

                    # like your said, cutoff
                    if (new_weight < weight):
                        route.append(new_board)
                        helper(types[1:], new_board, new_weight, route, best)
                        route.pop()

    helper(types, board, weight, route, best)
    # return best next move
    return best.route[0]


class Kb:
    def __init__(self, controller):
        self.controller = controller
        self.depth = 2
        self.board = board_1

    def notify(self):
        lst = list()
        count = 0
        for block in self.controller.blocks:
            if (count == self.depth):
                break
            lst.append(self.controller.pop(1))
            count += 1
        self.board = depth_first_limit(lst, self.board, 1000)
        self.board=remove_full_line(self.board)

        self.controller.push(self.board, 0)


board_2 = np.zeros(210).reshape(21, 10)


x=remove_full_line(board_2)
print(x)