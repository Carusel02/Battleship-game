import pygame
import random
# init
pygame.init()
# screen
screen = pygame.display.set_mode((1200, 800))
# title & icon
pygame.display.set_caption("World Domination")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

running = True
def game():
    # image
    matrix_image = pygame.image.load('matrice_back.png')
    matrix_image = pygame.transform.scale(matrix_image, (498.6, 495))
    matrix_X = 70
    matrix_Y = 100
    # 'X' pos
    pos_X = matrix_X + 15
    pos_Y = matrix_Y + 10
    pos = pygame.image.load('cancel.png')
    pos = pygame.transform.scale(pos, (40, 40))
    # 'X' not_here
    not_here_X = matrix_X + 15
    not_here_Y = matrix_Y + 10
    not_here = pygame.image.load('nothing_here (2).png')
    not_here = pygame.transform.scale(not_here, (40, 40))
    # score
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Hit : NO", True, (255, 255, 255))
    # matrix
    matrix = [[0 for j in range(10)] for i in range(10)]
    cell_size = 48.2
    # ships
    ship1 = pygame.image.load('ship1.png')
    ship1 = pygame.transform.scale(ship1, (40, 40))
    ship1_i = random.randint(0, 9)
    ship1_j = random.randint(0, 9)
    ship1_X = matrix_X + 15 + ship1_i * cell_size
    ship1_Y = matrix_Y + 10 + ship1_j * cell_size
    matrix[ship1_j][ship1_i] = 1

    ship2 = pygame.image.load('ship2.png')
    ship2 = pygame.transform.scale(ship2, (40, 40))
    ship2_i = random.randint(0, 9)
    ship2_j = random.randint(0, 9)
    ship2_X = matrix_X + 15 + ship2_i * cell_size
    ship2_Y = matrix_Y + 10 + ship2_j * cell_size
    matrix[ship2_j][ship2_i] = 2

    ship3 = pygame.image.load('ship3.png')
    ship3 = pygame.transform.scale(ship3, (40, 40))
    ship3_i = random.randint(0, 9)
    ship3_j = random.randint(0, 9)
    ship3_X = matrix_X + 15 + ship3_i * cell_size
    ship3_Y = matrix_Y + 10 + ship3_j * cell_size
    matrix[ship3_j][ship3_i] = 3

    show_ship1 = 0
    show_ship2 = 0
    show_ship3 = 0

    cursor_i = 0
    cursor_j = 0

    global running

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # move cursor
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pos_X += cell_size
                    cursor_i += 1
                if event.key == pygame.K_LEFT:
                    pos_X -= cell_size
                    cursor_i -= 1
                if event.key == pygame.K_DOWN:
                    pos_Y += cell_size
                    cursor_j += 1
                if event.key == pygame.K_UP:
                    pos_Y -= cell_size
                    cursor_j -= 1
                if event.key == pygame.K_x:
                    if matrix[cursor_j][cursor_i] == 0:
                        score = font.render("Hit : NO", True, (255, 255, 255))
                        matrix[cursor_j][cursor_i] = -1
                    if matrix[cursor_j][cursor_i] == 1:
                        score = font.render("Hit : YES 1", True, (255, 255, 255))
                        show_ship1 = 1
                    if matrix[cursor_j][cursor_i] == 2:
                        score = font.render("Hit : YES 2", True, (255, 255, 255))
                        show_ship2 = 1
                    if matrix[cursor_j][cursor_i] == 3:
                        score = font.render("Hit : YES 3", True, (255, 255, 255))
                        show_ship3 = 1
                    if matrix[cursor_j][cursor_i] == -1:
                        score = font.render("Hit : NO", True, (255, 255, 255))

        if pos_X < (matrix_X + 15):
            pos_X = matrix_X + 15
            cursor_i = 0
        if pos_X > (matrix_X + 15 + cell_size * 9):
            pos_X = matrix_X + 15 + cell_size * 9
            cursor_i = 9
        if pos_Y < (matrix_Y + 10):
            pos_Y = matrix_Y + 10
            cursor_j = 0
        if pos_Y > (matrix_Y + 10 + cell_size * 9):
            pos_Y = matrix_Y + 10 + cell_size * 9
            cursor_j = 9

        screen.fill((0, 0, 50))
        screen.blit(matrix_image, (matrix_X, matrix_Y))
        screen.blit(matrix_image, (matrix_X + 548.6, matrix_Y))
        screen.blit(score, (matrix_X + 800, matrix_Y + 600))

        i = 0
        for x in matrix:
            j = 0
            for y in x:
                if y == -1:
                    screen.blit(not_here, (matrix_X + 15 + cell_size * j, matrix_Y + 10 + cell_size * i))
                j += 1
            i += 1

        screen.blit(pos, (pos_X, pos_Y))

        if show_ship1 == 1:
            screen.blit(ship1, (ship1_X, ship1_Y))
        if show_ship2 == 1:
            screen.blit(ship2, (ship2_X, ship2_Y))
        if show_ship3 == 1:
            screen.blit(ship3, (ship3_X, ship3_Y))

        pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 60)
start = font.render("PRESS S", True, (0, 255, 255))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game()

    screen.fill((0, 0, 50))
    screen.blit(start, (500, 400))
    pygame.display.update()
