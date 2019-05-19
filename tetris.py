import pygame
import module

# set up window
pygame.init()

# setwindow size
width = 400
height = 800
screen = pygame.display.set_mode((width, height))

# set window name
pygame.display.set_caption("Tetris AI")

# set up game grids
cube_width = 40
grid_width = int(width / cube_width)
grid_height = int(height / cube_width)
line_color = (128,128,128)
def draw_grids():
    for i in range (grid_width):
        pygame.draw.line(screen, line_color,(i*cube_width,0),(i*cube_width,height))
    for i in range (grid_height):
        pygame.draw.line(screen, line_color,(0, i * cube_width), (height, i * cube_width))


clock = pygame.time.Clock()
FPS = 30

running = True
while running:
    clock.tick(FPS)
    draw_grids()

    pygame.display.update()

    #set quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False