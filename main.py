import pygame

size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
