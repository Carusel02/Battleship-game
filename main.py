import random
import pygame

# init
pygame.init()
# screen
screen = pygame.display.set_mode((1200, 800))
# title & icon
pygame.display.set_caption("World Domination")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# image
matrix_image = pygame.image.load('matrice_back.png')
matrix_image = pygame.transform.scale(matrix_image, (498.6, 495))
matrix_X = 70
matrix_Y = 100
# object
not_here_X = matrix_X + 15
not_here_Y = matrix_Y + 10
not_here = pygame.image.load('nothing_here.png')
not_here = pygame.transform.scale(not_here, (40, 40))
# score
font = pygame.font.Font('freesansbold.ttf', 32)
score = font.render("Hit : NO", True, (255, 255, 255))
# matrix
matrix = [[0 for j in range(10)] for i in range(10)]
cell_size = 48.2
print(matrix)
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

cursor_X = 0
cursor_Y = 0

running = True
while running:

    screen.fill((0, 0, 50))
    screen.blit(matrix_image, (matrix_X, matrix_Y))
    screen.blit(matrix_image, (matrix_X + 548.6, matrix_Y))
    screen.blit(not_here, (not_here_X, not_here_Y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move cursor
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                not_here_X += cell_size
                cursor_X += 1
            if event.key == pygame.K_LEFT:
                not_here_X -= cell_size
                cursor_X -= 1
            if event.key == pygame.K_DOWN:
                not_here_Y += cell_size
                cursor_Y += 1
            if event.key == pygame.K_UP:
                not_here_Y -= cell_size
                cursor_Y -= 1
            if event.key == pygame.K_x:
                if matrix[cursor_Y][cursor_X] == 0:
                    score = font.render("Hit : NO", True, (255, 255, 255))
                if matrix[cursor_Y][cursor_X] == 1:
                    score = font.render("Hit : YES 1", True, (255, 255, 255))
                if matrix[cursor_Y][cursor_X] == 2:
                    score = font.render("Hit : YES 2", True, (255, 255, 255))
                if matrix[cursor_Y][cursor_X] == 3:
                    score = font.render("Hit : YES 3", True, (255, 255, 255))

    if not_here_X < (matrix_X + 15):
        not_here_X = matrix_X + 15
        cursor_X = 0
    if not_here_X > (matrix_X + 15 + cell_size * 9):
        not_here_X = matrix_X + 15 + cell_size * 9
        cursor_X = 9
    if not_here_Y < (matrix_Y + 10):
        not_here_Y = matrix_Y + 10
        cursor_Y = 0
    if not_here_Y > (matrix_Y + 10 + cell_size * 9):
        not_here_Y = matrix_Y + 10 + cell_size * 9
        cursor_Y = 9

    screen.blit(score, (matrix_X + 800, matrix_Y + 600))
    screen.blit(ship1, (ship1_X, ship1_Y))
    screen.blit(ship2, (ship2_X, ship2_Y))
    screen.blit(ship3, (ship3_X, ship3_Y))

    pygame.display.update()
