


# set the file root directory to  be current folder


live_cube = None
next_cube = None

# set the format of the text (for score

white = (0xff, 0xff, 0xff)
black = (0, 0, 0)
LineColor = (0x33, 0x33, 0x33)  # color of empty square's lines


# the color of pieces
ShapeColor = [
    (0xcc, 0x99, 0x99), (0xff, 0xff, 0x99), (0x66, 0x66, 0x99),
    (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
    (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (0xff, 0xff, 0x33),
    (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (0xff, 0x99, 0x00)
]

#####################
# Shape classes
# represent the operations of the pieces on the board
#####################
class Shape(object):
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
         [(-1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, 1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (1, 0)]]
    L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
         [(1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, -1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (-1, 0)]]
    O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
         [(1, -1), (1, 0), (0, 0), (0, 1)]]
    T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, -1)]]
    Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
         [(-1, 0), (0, 0), (0, -1), (1, -1)]]
    SHAPES_WITH_DIR = {
        'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z
    }

    def __init__(self):

        self.shapeId = random.randint(0, len(self.SHAPES) - 1)
        self.shape = self.SHAPES[self.shapeId]
        # the position of the piece
        self.center = (2, CubeNumX // 2) # [0]: Y [1]: X
        self.dir = random.randint(0, len(self.SHAPES_WITH_DIR[self.shape]) - 1)
        self.color = ShapeColor[random.randint(0, len(ShapeColor) - 1)]
        self.controller=None

    def get_all_gridpos(self, center=None):
        curr_shape = self.SHAPES_WITH_DIR[self.shape][self.dir]
        if center is None:
            center = [self.center[0], self.center[1]]

        return [(cube[0] + center[0], cube[1] + center[1])
                for cube in curr_shape]

    def conflict(self, center):
        for cube in self.get_all_gridpos(center):
            # exceed screen, illegal
            if cube[0] < 0 or cube[1] < 0 or cube[0] >= CubeNumY or \
                    cube[1] >= CubeNumX:
                return True

            # if None, already exists cubes, illegal
            if screen_color_matrix[cube[0]][cube[1]] is not None:
                return True

        return False

    def rotate(self):
        new_dir = self.dir + 1
        new_dir %= len(self.SHAPES_WITH_DIR[self.shape])
        old_dir = self.dir
        self.dir = new_dir
        if self.conflict(self.center):
            self.dir = old_dir
            return False

    def down(self):
        # import pdb; pdb.set_trace()
        center = (self.center[0] + 1, self.center[1])
        if self.conflict(center):
            return False

        self.center = center
        return True

    def left(self):
        center = (self.center[0], self.center[1] - 1)
        if self.conflict(center):
            return False
        self.center = center
        return True

    def right(self):
        center = (self.center[0], self.center[1] + 1)
        if self.conflict(center):
            return False
        self.center = center
        return True

    def draw(self):
        for cube in self.get_all_gridpos():
            pygame.draw.rect(screen, self.color,
                             (cube[1] * CubeWidth, cube[0] * CubeWidth,
                              CubeWidth, CubeWidth))
            pygame.draw.rect(screen, white,
                             (cube[1] * CubeWidth, cube[0] * CubeWidth,
                              CubeWidth, CubeWidth),
                             1)








# draw empty squares


# draw existed pieces to square
def draw_matrix():
    for i, row in zip(range(CubeNumY), screen_color_matrix):
        for j, color in zip(range(CubeNumX), row):
            if color is not None:
                pygame.draw.rect(screen, color,
                                 (j * CubeWidth, i * CubeWidth,
                                  CubeWidth, CubeWidth))
                pygame.draw.rect(screen, white,
                                 (j * CubeWidth, i * CubeWidth,
                                  CubeWidth, CubeWidth), 2)


def draw_score():
    show_text(screen, u'Score：{}'.format(score), 20, BoardWidth + AdditionalWidth // 2, 100)
    if(live_cube != None and next_cube != None):
        show_text(screen, u'Current shape:{}'.format(live_cube.SHAPES[live_cube.shapeId]), 20, BoardWidth + AdditionalWidth // 2, 120)
        show_text(screen, u'Next shape:{}'.format(next_cube.SHAPES[next_cube.shapeId]), 20, BoardWidth + AdditionalWidth // 2, 140)


def remove_full_line():
    global screen_color_matrix
    global score
    global level
    new_matrix = [[None] * CubeNumX for i in range(CubeNumY)]
    index = CubeNumY - 1
    n_full_line = 0
    for i in range(CubeNumY - 1, -1, -1):
        is_full = True
        for j in range(CubeNumX):
            if screen_color_matrix[i][j] is None:
                is_full = False
                continue
        if not is_full:
            new_matrix[index] = screen_color_matrix[i]
            index -= 1
        else:
            n_full_line += 1
    score += n_full_line
    level = score // 20 + 1
    screen_color_matrix = new_matrix


def show_welcome(screen):
    show_text(screen, u'TETRIS', 30, BoardWidth / 2, BoardHeight / 2)
    show_text(screen, u'press any key to start the game', 20, BoardWidth / 2, BoardHeight / 2 + 50)


# run the game
screen_color_matrix = [[None] * CubeNumX for i in range(CubeNumY)]

clock = pygame.time.Clock()  # time
FPS = 30  # speed

counter = 0
score = 0
level = 1

running = True
gameover = True



while running:
    clock.tick(FPS)

    Controller.setMatrix(screen_color_matrix)
    # set events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if gameover:  # game over is true in the beginning
                gameover = False
                if next_cube == None:
                    Controller.history
                    live_cube = Shape()
                else:
                    live_cube = next_cube
                next_cube = Shape()
                Controller.setCurrentCube(live_cube)
                # get new shape, send to control
                break
            if event.key == pygame.K_LEFT:
                live_cube.left()
            elif event.key == pygame.K_RIGHT:
                live_cube.right()
            elif event.key == pygame.K_DOWN:
                live_cube.down()
            elif event.key == pygame.K_UP:
                live_cube.rotate()
            elif event.key == pygame.K_SPACE:
                while live_cube.down() == True:
                    pass
            remove_full_line()

    # higher level, smaller FPS, faster speed
    if gameover is False and counter % (FPS // level) == 0:
        #  down() return false = exceed screen or conflict with prior cubes
        if live_cube.down() == False:

            for cube in live_cube.get_all_gridpos():
                screen_color_matrix[cube[0]][cube[1]] = live_cube.color

            live_cube = next_cube
            next_cube = Shape()
            Controller.setCurrentCube(live_cube)
            if live_cube.conflict(live_cube.center):
                gameover = True
                score = 0
                live_cube = None
                screen_color_matrix = [[None] * CubeNumX for i in range(CubeNumY)]

        remove_full_line()
        Controller.getMatrix()
    counter += 1
    # update screen
    screen.fill(black)
    draw_grids()
    draw_matrix()
    draw_score()
    if live_cube is not None:
        live_cube.draw()
    if gameover:
        show_welcome(screen)
    pygame.display.update()