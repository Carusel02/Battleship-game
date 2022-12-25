import pygame
# init
pygame.init()
# screen
screen = pygame.display.set_mode((1200, 800))
# title & icon
pygame.display.set_caption("Love is war")
icon = pygame.image.load('warship.png')
pygame.display.set_icon(icon)

# image
matrix_image = pygame.image.load('matrice_background.png')
matrix_image = pygame.transform.scale(matrix_image, (443.2, 440))
matrix_X = 0
matrix_Y = 0



running = True
while running:
    # RGB
    screen.fill((0, 0, 50))
    screen.blit(matrix_image,(0 ,0))
    screen.blit(matrix_image, (450, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()