import tetris_original as game

def getAllPositions(center,currentShape,direction):
    currShape = currentShape.SHAPES_WITH_DIR[currentShape][direction]
    return [(cube[0]+center[0],cube[1]+center[1])for cube in currShape]


def getNewBoard(currentBoard,currentShape,center,station): # station = direction
    # copy the old board
    newBoard = [[None] * game.CubeNumX for i in range(game.CubeNumY)]
    for i in range(len(currentBoard)):
        for j in range(len(currentBoard[i])):
            newBoard = currentBoard[i][j]
    # put the piece, get new board
    possiblePositions = getAllPositions(center,currentShape,station)

    return newBoard


def getHeights(board):
    # assume the piece already fall
    heights = []
    tempBoard = board # board is the matrix (board) when the piece have not fall
    for i in range(len(tempBoard[1])):
        counter = 0
        j=0
        while(tempBoard[i][j]==None and j < game.CubeNumY):
            counter+=1
            j+=1
        heights.append(counter)
    return heights


def getLandingHeights(shape):
    return game.CubeNumY-1-shape.center[0]


def getNumFullLines(currrentShape,center,station):
    tempBoard = getNewBoard(center,station)
    completedLines = 0
    usedBlocks = 0
    possiblePositions = getAllPossiblePositions(center,currrentShape,station)
    for i in range(len(tempBoard)-1,0,1):
        cubeCounter = 0
        for j in range(len(tempBoard[1])):
            if tempBoard[i][j] is not None:
                cubeCounter+=1
        if cubeCounter == game.CubeNumX:
            completedLines+=1
            for k in range(len(tempBoard[1])):
                if [i,k] in possiblePositions:
                    usedBlocks +=1
        if cubeCounter ==0:
            break
    return 0


def getNumHoles(currentBoard):
    totalHoles = 0
    for j in range(len(currentBoard[1])):
        holeCounter = 0
        for i in range(len(currentBoard)):
            if currentBoard[i][j] == None:
                holeCounter += 1

        holeCounter += holeCounter
    return totalHoles


def getBumpiness(currentBoard):
    # 2 ways
    # simple way
    bumpiness = 0
    currentHeights = getHeights(currentBoard)
    for i in range(len(currentHeights)-1):
        bumpiness+=abs(currentHeights[i]-currentHeights[i+1])
    return bumpiness


def Evaluation(point,currentShape,currentBoard):
    # argument: structure or a board
    tempBoard = getNewBoard(currentBoard,currentShape,point['center'],point['station'])
    landingHeight = getLandingHeights(point['center'])
    clearLinesNum = getNumFullLines(tempBoard,point['center'],point['station'])
    holesNum = getNumHoles(tempBoard)
    bumpiness = getBumpiness(tempBoard)
    score = 0
    return score


def getAllPossiblePositions(shape, board):
    # board might be self
    tempBoard = board # board is the matrix (board) when the piece have not fall
    shapeNum = len(shape.SHAPES_WITH_DIR[shape]) # get the number of all possible direction piece
    possiblePositions = []
    for i in range(shapeNum):
        for j in range(len(tempBoard[1])):
            for k in range(len(tempBoard)-1):
                if shape.conflict([k+1,j],tempBoard,shape,i)==True and shape.conflict([k,j],tempBoard,shape,i) == False:
                    if{"center":[k,j],"station": i} not in possiblePositions:
                        possiblePositions.append({"center":[k,j],"station":i})
    return possiblePositions


def Search(currentShape,currentBoard):
    # 1 give the shape to the current board
    # 2 check the shape with a position in different direction, keep the info in a structure
    # with a temp board to evaluate
    # 3 evaluate the structure, give the score to the structure
    # or when loop, keep a "best decision" by comparing
    # 4 after loop, show the decision
    bestPosition = None
    bestScore = -1
    positions = getAllPossiblePositions(currentShape,currentBoard)
    for position in positions:
        score = Evaluation(position,currentShape,currentBoard)
        if score > bestScore:
            bestScore = score
            bestPosition = position
        # can add priority thing
    return bestPosition
