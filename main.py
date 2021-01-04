import pygame

size = width, height = 450, 650
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True
position = [[0] * 8] * 10


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 25
        self.top = 10
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, "white", [(self.left + (self.cell_size * i), self.top + (self.cell_size * j)),
                                                   (self.cell_size, self.cell_size)], 1)

    def cells_coord(self):
        interior_list = []
        for i in range(self.height):
            for j in range(self.width):
                coords = (self.cell_size * j + self.left, self.cell_size * i + self.top)
                interior_list.append(coords)
        return interior_list


board = Board(8, 10)
COORDS = board.cells_coord()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        board.render()
    pygame.display.flip()
pygame.quit()
