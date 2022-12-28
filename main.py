import os
import random
import pygame
import time

# background sound
from pygame import mixer
# terminal colors
#from colorama import Fore

#print(Fore.RED + 'python game')
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

# global ships
global ship1
global ship2
global ship3
global show_ship1
global show_ship2
global show_ship3

# global X coord
global ship1_x
global ship2_x
global ship3_x
# global Y coord
global ship1_y
global ship2_y
global ship3_y

# global stuff
global matrix_x
global matrix_y
global font


# function game
def game():
    # add background music
    mixer.music.load('sound/background_mitopia_ost.wav')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)

    flag = 0
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
    initial_value_x = matrix_x + 15
    initial_value_y = matrix_y + 10
    not_here = pygame.image.load('images/nothing_here (2).png')
    not_here = pygame.transform.scale(not_here, (40, 40))
    # hit one part of boat
    hit_value_x = matrix_x + 15
    hit_value_y = matrix_y + 10
    hit_here = pygame.image.load('images/hitboat.png')
    hit_here = pygame.transform.scale(hit_here, (40, 40))
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
    ship1 = pygame.transform.scale(ship1, (160, 40))
    ship1_i = random.randint(0, 6)
    ship1_j = random.randint(0, 9)
    global ship1_x
    global ship1_y
    ship1_x = initial_value_x + ship1_i * cell_size
    ship1_y = initial_value_y + ship1_j * cell_size
    matrix[ship1_j][ship1_i] = 1
    matrix[ship1_j][ship1_i + 3] = 1
    matrix[ship1_j][ship1_i + 1] = 1
    matrix[ship1_j][ship1_i + 2] = 1

    ship1cp_i = random.randint(0, 6)
    ship1cp_j = random.randint(0, 9)
    ship1cp_x = initial_value_x + 548.6 + ship1cp_i * cell_size
    ship1cp_y = initial_value_y + ship1cp_j * cell_size
    matrixcp[ship1cp_j][ship1cp_i] = 1
    matrixcp[ship1cp_j][ship1cp_i + 1] = 1
    matrixcp[ship1cp_j][ship1cp_i + 2] = 1
    matrixcp[ship1cp_j][ship1cp_i + 3] = 1

    global ship2
    ship2 = pygame.image.load('images/ship2.png')
    ship2 = pygame.transform.scale(ship2, (120, 80))
    ship2_i = random.randint(0, 7)
    ship2_j = random.randint(0, 8)
    global ship2_x
    global ship2_y
    if matrix[ship2_j][ship2_i] != 0 or matrix[ship2_j][ship2_i + 1] !=0 or matrix[ship2_j][ship2_i + 2] != 0 or matrix[ship2_j + 1][ship2_i] != 0 or matrix[ship2_j + 1][ship2_i + 1] != 0 or matrix[ship2_j + 1][ship2_i + 2] != 0:
        while matrix[ship2_j][ship2_i] != 0 or matrix[ship2_j][ship2_i + 1] !=0 or matrix[ship2_j][ship2_i + 2] != 0 or matrix[ship2_j + 1][ship2_i] != 0 or matrix[ship2_j + 1][ship2_i + 1] != 0 or matrix[ship2_j + 1][ship2_i + 2] != 0:
            ship2_i = random.randint(0, 7)
            ship2_j = random.randint(0, 8)
    matrix[ship2_j][ship2_i] = 2
    matrix[ship2_j][ship2_i + 1] = 2
    matrix[ship2_j][ship2_i + 2] = 2
    matrix[ship2_j + 1][ship2_i] = 2
    matrix[ship2_j + 1][ship2_i + 1] = 2
    matrix[ship2_j + 1][ship2_i + 2] = 2
    ship2_x = initial_value_x + ship2_i * cell_size
    ship2_y = initial_value_y + ship2_j * cell_size


    ship2cp_i = random.randint(0, 7)
    ship2cp_j = random.randint(0, 8)
    if matrixcp[ship2cp_j][ship2cp_i] != 0 or matrixcp[ship2cp_j][ship2cp_i + 1] !=0 or matrixcp[ship2cp_j][ship2cp_i + 2] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i + 1] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i + 2] != 0:
        while matrixcp[ship2cp_j][ship2cp_i] != 0 or matrixcp[ship2cp_j][ship2cp_i + 1] !=0 or matrixcp[ship2cp_j][ship2cp_i + 2] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i + 1] != 0 or matrixcp[ship2cp_j + 1][ship2cp_i + 2] != 0:
            ship2cp_i = random.randint(0, 7)
            ship2cp_j = random.randint(0, 8)
    ship2cp_x = matrix_x + 548.6 + 15 + ship2cp_i * cell_size
    ship2cp_y = matrix_y + 10 + ship2cp_j * cell_size
    matrixcp[ship2cp_j][ship2cp_i] = 2
    matrixcp[ship2cp_j][ship2cp_i + 1] = 2
    matrixcp[ship2cp_j][ship2cp_i + 2] = 2
    matrixcp[ship2cp_j + 1][ship2cp_i] = 2
    matrixcp[ship2cp_j + 1][ship2cp_i + 1] = 2
    matrixcp[ship2cp_j + 1][ship2cp_i + 2] = 2

    global ship3
    ship3 = pygame.image.load('images/ship3.png')
    ship3 = pygame.transform.scale(ship3, (120, 40))
    ship3_i = random.randint(0, 7)
    ship3_j = random.randint(0, 9)
    global ship3_x
    global ship3_y
    if matrix[ship3_j][ship3_i] != 0 or matrix[ship3_j][ship3_i + 1] !=0 or matrix[ship3_j][ship3_i + 2] != 0:
        while matrix[ship3_j][ship3_i] != 0 or matrix[ship3_j][ship3_i + 1] !=0 or matrix[ship3_j][ship3_i + 2] != 0:
            ship3_i = random.randint(0, 7)
            ship3_j = random.randint(0, 9)
    ship3_x = initial_value_x + ship3_i * cell_size
    ship3_y = initial_value_y + ship3_j * cell_size
    matrix[ship3_j][ship3_i] = 3
    matrix[ship3_j][ship3_i + 1] = 3
    matrix[ship3_j][ship3_i + 2] = 3

    ship3cp_i = random.randint(0, 7)
    ship3cp_j = random.randint(0, 9)
    if matrixcp[ship3cp_j][ship3cp_i] != 0 or matrixcp[ship3cp_j][ship3cp_i + 1] !=0 or matrixcp[ship3cp_j][ship3cp_i + 2] != 0:
        while matrixcp[ship3cp_j][ship3cp_i] != 0 or matrixcp[ship3cp_j][ship3cp_i + 1] !=0 or matrixcp[ship3cp_j][ship3cp_i +2] != 0:
            ship3cp_i = random.randint(0, 7)
            ship3cp_j = random.randint(0, 9)

    ship3cp_x = initial_value_x + 548.6 + ship3cp_i * cell_size
    ship3cp_y = initial_value_y + ship3cp_j * cell_size
    matrixcp[ship3cp_j][ship3cp_i] = 3
    matrixcp[ship3cp_j][ship3cp_i + 1] = 3
    matrixcp[ship3cp_j][ship3cp_i + 2] = 3

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

    contor1 = 4
    contor1cp = 4
    contor2 = 6
    contor2cp = 6
    contor3 = 3
    contor3cp = 3

    global running

    while running:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                running = False
            # move cursor
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_RIGHT:
                    pos_x += cell_size
                    cursor_i += 1
                if action.key == pygame.K_LEFT:
                    pos_x -= cell_size
                    cursor_i -= 1
                if action.key == pygame.K_DOWN:
                    pos_y += cell_size
                    cursor_j += 1
                if action.key == pygame.K_UP:
                    pos_y -= cell_size
                    cursor_j -= 1
                if action.key == pygame.K_x:
                    flag = 1
                    # sound effect
                    press_hit_sound = mixer.Sound('sound/cross_sound.wav')
                    press_hit_sound.play()
                    if matrix[cursor_j][cursor_i] == 0:
                        score = font.render("Hit : NO", True, (255, 255, 255))
                        matrix[cursor_j][cursor_i] = -1

                    if matrix[cursor_j][cursor_i] == 1:
                        score = font.render("Hit : YES", True, (255, 255, 255))
                        contor1 -= 1
                        matrix[cursor_j][cursor_i] = -2

                    if matrix[cursor_j][cursor_i] == 2:
                        score = font.render("Hit : YES", True, (255, 255, 255))
                        contor2 -= 1
                        matrix[cursor_j][cursor_i] = -2

                    if matrix[cursor_j][cursor_i] == 3:
                        score = font.render("Hit : YES", True, (255, 255, 255))
                        contor3 -= 1
                        matrix[cursor_j][cursor_i] = -2

                    if matrix[cursor_j][cursor_i] == -1:
                        score = font.render("Hit : NO", True, (255, 255, 255))

                    if contor1 == 0:
                        show_ship1 = 1
                        ship_left -= 1
                        contor1 = -1

                    if contor2 == 0:
                        show_ship2 = 1
                        ship_left -= 1
                        contor2 = -1

                    if contor3 == 0:
                        show_ship3 = 1
                        ship_left -= 1
                        contor3 = -1

        if flag == 1:
            temp = bot(matrixcp)
            if temp == 1:
                contor1cp -= 1
            if temp == 2:
                contor2cp -= 1
            if temp == 3:
                contor3cp -= 1
            if contor1cp == 0:
                ship_left_cp -= 1
                ship1cp_x = 0
                contor1cp = -1
                print(1)
            if contor2cp == 0:
                ship_left_cp -= 1
                ship2cp_x = 0
                print(2)
                contor2cp = -1
            if contor3cp == 0:
                ship_left_cp -= 1
                ship3cp_x = 0
                contor3cp = -1
                print(3)
            flag = 0

        if pos_x < initial_value_x:
            pos_x = initial_value_x
            cursor_i = 0
        if pos_x > (initial_value_x + cell_size * 9):
            pos_x = initial_value_x + cell_size * 9
            cursor_i = 9
        if pos_y < initial_value_y:
            pos_y = initial_value_y
            cursor_j = 0
        if pos_y > (initial_value_y + cell_size * 9):
            pos_y = initial_value_y + cell_size * 9
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
                    screen.blit(not_here, (initial_value_x + cell_size * j, initial_value_y + cell_size * i))
                if y == -2:
                    screen.blit(hit_here, (hit_value_x + cell_size * j, hit_value_y + cell_size * i))
                j += 1
            i += 1

        i = 0
        for x in matrixcp:
            j = 0
            for y in x:
                if y == -1:
                    screen.blit(not_here, (initial_value_x + 548.6 + cell_size * j, initial_value_y + cell_size * i))
                if y == -2:
                    screen.blit(hit_here, (hit_value_x + 548.6 + cell_size * j, hit_value_y + cell_size * i))
                j += 1
            i += 1

        screen.blit(pos, (pos_x, pos_y))

        # verify
        show_ship(show_ship1, show_ship2, show_ship3, ship_left, ship_left_cp)
        # refresh display
        pygame.display.update()


# bot function for hitting
def bot(matrix):
    while True:
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        if matrix[i][j] == 0:
            matrix[i][j] = -1
            return 0

        if matrix[i][j] == 1:
            matrix[i][j] = -2
            return 1

        if matrix[i][j] == 2:
            matrix[i][j] = -2
            return 2

        if matrix[i][j] == 3:
            matrix[i][j] = -2
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
        mixer.music.stop()
        win_menu()
        time.sleep(3)
        # exit()
        running = 0
    if ship_remain_bot == 0:
        score = font.render("COMPUTER WINS", True, (255, 255, 255))
        screen.blit(score, (matrix_x + 400, matrix_y + 600))
        pygame.display.update()
        mixer.music.stop()
        game_over_menu()
        time.sleep(3)
        # exit()
        running = 0


# display game_over window
def game_over_menu():
    time.sleep(0.2)
    game_over_sound = mixer.Sound('sound/lost_game.wav')
    game_over_sound.play()
    image1 = pygame.image.load('images/game_over.png')
    image1 = pygame.transform.scale(image1, (520, 338))
    image2 = pygame.transform.scale(image1, (560, 364))
    image3 = pygame.transform.scale(image1, (600, 390))
    run = 1
    ok = 0
    while run:
        screen.fill((0, 0, 50))
        pygame.display.update()
        screen.blit(image1, (340, 231))
        pygame.display.update()
        time.sleep(0.3)
        screen.fill((0, 0, 50))
        screen.blit(image2, (320, 218))
        pygame.display.update()
        time.sleep(0.3)
        screen.fill((0, 0, 50))
        screen.blit(image3, (300, 205))
        pygame.display.update()
        time.sleep(0.3)
        ok += 1
        if ok == 6:
            run = 0


# display you_win window
def win_menu():
    time.sleep(0.2)
    win_sound = mixer.Sound('sound/win_game.wav')
    win_sound.play()
    image1 = pygame.image.load('images/win.png')
    image1 = pygame.transform.scale(image1, (520, 338))
    image2 = pygame.transform.scale(image1, (560, 364))
    image3 = pygame.transform.scale(image1, (600, 390))
    run = 1
    ok = 0
    while run:
        screen.fill((0, 0, 50))
        pygame.display.update()
        screen.blit(image1, (340, 231))
        pygame.display.update()
        time.sleep(0.3)
        screen.fill((0, 0, 50))
        screen.blit(image2, (320, 218))
        pygame.display.update()
        time.sleep(0.3)
        screen.fill((0, 0, 50))
        screen.blit(image3, (300, 205))
        pygame.display.update()
        time.sleep(0.3)
        ok += 1
        if ok == 6:
            run = 0


# start menu
def start_menu():
    font = pygame.font.Font('font/pixelated.ttf', 40)
    start = font.render("PRESS                FOR START", True, (255, 255, 255))
    font2 = pygame.font.Font('font/pixelated.ttf', 70)
    title = font2.render("WORLD DOMINATION", True, (255, 255, 255))
    screen.fill((0, 0, 50))
    screen.blit(start, (350, 570))
    screen.blit(title, (230, 320))
    vector_image = load_images('images')
    image1 = pygame.transform.scale(vector_image[3], (90, 90))
    image2 = pygame.transform.scale(vector_image[3], (100, 100))
    image3 = pygame.transform.scale(vector_image[3], (110, 110))

    test = pygame.image.load('images/cancel.png')
    # create GIF animation for keycap S
    screen.blit(image1, (530, 560))
    pygame.display.update()
    time.sleep(0.3)
    screen.blit(image2, (525, 555))
    pygame.display.update()
    time.sleep(0.3)
    screen.blit(image3, (520, 550))
    pygame.display.update()
    time.sleep(0.3)


# load image
def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name)
        images.append(image)
    return images


# first music
start_menu_sound = mixer.Sound('sound/start_menu.wav')
start_menu_sound.play()
# main function
while running:
    # default customization start menu
    start_menu()
    # refresh display
    pygame.display.update()

    # catch an event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
        # press start => function game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start_menu_sound.stop()
                time.sleep(0.3)
                game()
