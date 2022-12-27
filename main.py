import os
import random
import pygame
import time

# terminal colors
from colorama import Fore

print(Fore.RED + 'python game')
# init
pygame.init()
# screen
screen = pygame.display.set_mode((1200, 800))
# title & icon
pygame.display.set_caption("World Domination")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
# run program
running = True

global show_ship1
global show_ship2
global show_ship3

global ship1
global ship2
global ship3

global ship1_x
global ship2_x
global ship3_x

global ship1_y
global ship2_y
global ship3_y

global matrix_x
global matrix_y

global font


# function game
def game():
    contor = 0
    ship_left = 3
    ship_left_cp = 3
    # image
    matrix_image = pygame.image.load('images/matrice_back.png')
    matrix_image = pygame.transform.scale(matrix_image, (498.6, 495))
    global matrix_x
    global matrix_y
    matrix_x = 70
    matrix_y = 100
    # 'X' pos
    pos_x = matrix_x + 15
    pos_y = matrix_y + 10
    pos = pygame.image.load('images/cancel.png')
    pos = pygame.transform.scale(pos, (40, 40))
    # 'X' not_here
    not_here_X = matrix_x + 15
    not_here_Y = matrix_y + 10
    not_here = pygame.image.load('images/nothing_here (2).png')
    not_here = pygame.transform.scale(not_here, (40, 40))
    # score
    global font
    font = pygame.font.Font('font/pixelated.ttf', 30)
    score = font.render("Hit : NO", True, (255, 255, 255))
    score_display = font.render("Scor user: " + str(3 - ship_left) + "Scor bot: " + str(3 - ship_left_cp), True,
                                (255, 255, 255))
    # matrix
    matrix = [[0 for j in range(10)] for i in range(10)]
    matrixcp = [[0 for j in range(10)] for i in range(10)]

    cell_size = 48.2
    # ships
    global ship1
    ship1 = pygame.image.load('images/ship1.png')
    ship1 = pygame.transform.scale(ship1, (40, 40))
    ship1_i = random.randint(0, 9)
    ship1_j = random.randint(0, 9)
    global ship1_x
    global ship1_y
    ship1_x = matrix_x + 15 + ship1_i * cell_size
    ship1_y = matrix_y + 10 + ship1_j * cell_size
    matrix[ship1_j][ship1_i] = 1

    ship1cp_i = random.randint(0, 9)
    ship1cp_j = random.randint(0, 9)
    ship1cp_x = matrix_x + 548.6 + 15 + ship1cp_i * cell_size
    ship1cp_y = matrix_y + 10 + ship1cp_j * cell_size
    matrixcp[ship1cp_j][ship1cp_i] = 1

    global ship2
    ship2 = pygame.image.load('images/ship2.png')
    ship2 = pygame.transform.scale(ship2, (40, 40))
    ship2_i = random.randint(0, 9)
    ship2_j = random.randint(0, 9)
    global ship2_x
    global ship2_y
    ship2_x = matrix_x + 15 + ship2_i * cell_size
    ship2_y = matrix_y + 10 + ship2_j * cell_size
    matrix[ship2_j][ship2_i] = 2

    ship2cp_i = random.randint(0, 9)
    ship2cp_j = random.randint(0, 9)
    ship2cp_x = matrix_x + 548.6 + 15 + ship2cp_i * cell_size
    ship2cp_y = matrix_y + 10 + ship2cp_j * cell_size
    matrixcp[ship2cp_j][ship2cp_i] = 2

    global ship3
    ship3 = pygame.image.load('images/ship3.png')
    ship3 = pygame.transform.scale(ship3, (40, 40))
    ship3_i = random.randint(0, 9)
    ship3_j = random.randint(0, 9)
    global ship3_x
    global ship3_y
    ship3_x = matrix_x + 15 + ship3_i * cell_size
    ship3_y = matrix_y + 10 + ship3_j * cell_size
    matrix[ship3_j][ship3_i] = 3

    ship3cp_i = random.randint(0, 9)
    ship3cp_j = random.randint(0, 9)
    ship3cp_x = matrix_x + 548.6 + 15 + ship3cp_i * cell_size
    ship3cp_y = matrix_y + 10 + ship3cp_j * cell_size
    matrixcp[ship3cp_j][ship3cp_i] = 3

    for x in matrixcp:
        print(x)

    global show_ship1
    show_ship1 = 0
    global show_ship2
    show_ship2 = 0
    global show_ship3
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
                    pos_x += cell_size
                    cursor_i += 1
                if event.key == pygame.K_LEFT:
                    pos_x -= cell_size
                    cursor_i -= 1
                if event.key == pygame.K_DOWN:
                    pos_y += cell_size
                    cursor_j += 1
                if event.key == pygame.K_UP:
                    pos_y -= cell_size
                    cursor_j -= 1
                if event.key == pygame.K_x:
                    contor = 1
                    if matrix[cursor_j][cursor_i] == 0:
                        score = font.render("Hit : NO", True, (255, 255, 255))
                        matrix[cursor_j][cursor_i] = -1

                    if matrix[cursor_j][cursor_i] == 1:
                        score = font.render("Hit : YES 1", True, (255, 255, 255))
                        show_ship1 = 1
                        ship_left -= 1
                        matrix[cursor_j][cursor_i] = -1

                    if matrix[cursor_j][cursor_i] == 2:
                        score = font.render("Hit : YES 2", True, (255, 255, 255))
                        show_ship2 = 1
                        ship_left -= 1
                        matrix[cursor_j][cursor_i] = -1

                    if matrix[cursor_j][cursor_i] == 3:
                        score = font.render("Hit : YES 3", True, (255, 255, 255))
                        show_ship3 = 1
                        ship_left -= 1
                        matrix[cursor_j][cursor_i] = -1

                    if matrix[cursor_j][cursor_i] == -1:
                        score = font.render("Hit : NO", True, (255, 255, 255))

        if contor == 1:
            temp = bot(matrixcp)
            if temp == 1:
                ship_left_cp -= 1
                ship1cp_x = 0
                print(1)
            if temp == 2:
                ship_left_cp -= 1
                ship2cp_x = 0
                print(2)
            if temp == 3:
                ship_left_cp -= 1
                ship3cp_x = 0
                print(3)
            contor = 0

        if pos_x < (matrix_x + 15):
            pos_x = matrix_x + 15
            cursor_i = 0
        if pos_x > (matrix_x + 15 + cell_size * 9):
            pos_x = matrix_x + 15 + cell_size * 9
            cursor_i = 9
        if pos_y < (matrix_y + 10):
            pos_y = matrix_y + 10
            cursor_j = 0
        if pos_y > (matrix_y + 10 + cell_size * 9):
            pos_y = matrix_y + 10 + cell_size * 9
            cursor_j = 9

        screen.fill((0, 0, 50))
        screen.blit(matrix_image, (matrix_x, matrix_y))
        screen.blit(matrix_image, (matrix_x + 548.6, matrix_y))
        screen.blit(score, (matrix_x + 800, matrix_y + 600))

        score_display = font.render("Scor user: " + str(3 - ship_left) + "    Scor bot: " + str(3 - ship_left_cp), True,
                                    (255, 255, 255))
        screen.blit(score_display, (0, 700))

        if ship2cp_x != 0:
            screen.blit(ship2, (ship2cp_x, ship2cp_y))
        if ship3cp_x != 0:
            screen.blit(ship3, (ship3cp_x, ship3cp_y))
        if ship1cp_x != 0:
            screen.blit(ship1, (ship1cp_x, ship1cp_y))

        i = 0
        for x in matrix:
            j = 0
            for y in x:
                if y == -1:
                    screen.blit(not_here, (matrix_x + 15 + cell_size * j, matrix_y + 10 + cell_size * i))
                j += 1
            i += 1

        i = 0
        for x in matrixcp:
            j = 0
            for y in x:
                if y == -1:
                    screen.blit(not_here, (matrix_x + 548.6 + 15 + cell_size * j, matrix_y + 10 + cell_size * i))
                j += 1
            i += 1

        screen.blit(pos, (pos_x, pos_y))

        #
        show_ship(show_ship1, show_ship2, show_ship3, ship_left, ship_left_cp)

        pygame.display.update()


def bot(matrixcp):
    while (1):
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        if matrixcp[i][j] == 0:
            matrixcp[i][j] = -1
            return 0

        if matrixcp[i][j] == 1:
            matrixcp[i][j] = -1
            return 1

        if matrixcp[i][j] == 2:
            matrixcp[i][j] = -1
            return 2

        if matrixcp[i][j] == 3:
            matrixcp[i][j] = -1
            return 3


# verify
def show_ship(see_ship1, see_ship2, see_ship3, ship_remain, ship_remain_bot):
    # global variables
    global running
    global ship1
    global ship2
    global ship3
    global font

    # check to display boat
    if see_ship1 == 1:
        screen.blit(ship1, (ship1_x, ship1_y))
    if see_ship2 == 1:
        screen.blit(ship2, (ship2_x, ship2_y))
    if see_ship3 == 1:
        screen.blit(ship3, (ship3_x, ship3_y))

    # check for ending game
    if ship_remain == 0:
        score = font.render("YOU WIN", True, (255, 255, 255))
        screen.blit(score, (matrix_x + 400, matrix_y + 600))
        pygame.display.update()
        time.sleep(3)
        # exit()
        running = 0
    if ship_remain_bot == 0:
        score = font.render("COMPUTER WINS", True, (255, 255, 255))
        screen.blit(score, (matrix_x + 400, matrix_y + 600))
        pygame.display.update()
        time.sleep(3)
        # exit()
        running = 0


# start menu
def start_menu():
    font = pygame.font.Font('font/pixelated.ttf', 40)
    start = font.render("PRESS S FOR START", True, (255, 255, 255))
    screen.fill((0, 0, 50))
    screen.blit(start, start.get_rect(center=screen.get_rect().center))
    vector_image = load_images('images')
    image = pygame.transform.scale(vector_image[0], (40, 40))
    test = pygame.image.load('images/cancel.png')
    screen.blit(image, (0, 0))


# load image
def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name)
        images.append(image)
    return images


# main function
while running:
    # catch an event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
        # press start => function game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game()

    # default customization start menu
    start_menu()
    # refresh display
    pygame.display.update()
