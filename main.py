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
score1 = font.render("Hit : NO", True, (255, 255, 255))
score2 = font.render("Hit : YES", True, (255, 255, 255))
score = score1
# ships
ship1 = pygame.image.load('ship1.png')
ship1 = pygame.transform.scale(ship1, (40, 40))
# matrix
matrix = [[0 for j in range(10)] for i in range(10)]
matrix[2][3] = 1
print(matrix)

cursor_X = 0
cursor_Y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move cursor
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                not_here_X += 48.2
                cursor_X += 1
            if event.key == pygame.K_LEFT:
                not_here_X -= 48.2
                cursor_X -= 1
            if event.key == pygame.K_DOWN:
                not_here_Y += 48.2
                cursor_Y += 1
            if event.key == pygame.K_UP:
                not_here_Y -= 48.2
                cursor_Y -= 1
            if event.key == pygame.K_KP_ENTER:
                if matrix[cursor_Y][cursor_X] != 0:
                    score = score2
                else:
                    score = score1

    if not_here_X < (matrix_X + 15):
        not_here_X = matrix_X + 15
        cursor_X = 0
    if not_here_X > (matrix_X + 15 + 48.2 * 9):
        not_here_X = matrix_X + 15 + 48.2 * 9
        cursor_X = 9
    if not_here_Y < (matrix_Y + 10):
        not_here_Y = matrix_Y + 10
        cursor_Y = 0
    if not_here_Y > (matrix_Y + 10 + 48.2 * 9):
        not_here_Y = matrix_Y + 10 + 48.2 * 9
        cursor_Y = 9

    # RGB
    screen.fill((0, 0, 50))
    screen.blit(matrix_image,(matrix_X, matrix_Y))
    screen.blit(matrix_image, (matrix_X + 548.6, matrix_Y))
    screen.blit(not_here, (not_here_X, not_here_Y))
    screen.blit(score, (matrix_X + 800, matrix_Y + 600))

    pygame.display.update()