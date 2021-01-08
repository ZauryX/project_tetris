import pygame
import random

size = width, height = 450, 650
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True
position = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
clock = pygame.time.Clock()
# pos = [225, 10]
# list_pos = []

kvadrat = [[[0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

pryamay = [[[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

t_obraz = [[[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

zigzag1 = [[[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

zigzag2 = [[[0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

ygol_v1 = [[[0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

ygol_v2 = [[[0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

figyry = [kvadrat, pryamay, t_obraz, zigzag1, zigzag2, ygol_v1, ygol_v2]
figyry_colors = [(255, 215, 0), (63, 0, 255), (255, 0, 0), (255, 0, 0), (255, 255, 25), (34, 34, 34), (255, 69, 0)]


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 25
        self.top = 10
        self.cell_size = 50

        fg = random.choice(figyry)
        self.povorot = 0
        self.color = figyry_colors[figyry.index(fg)]

    def create_grid(locked_positions={}):
        position = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(len(position)):
            for j in range(len(position[i])):
                if (j, i) in locked_positions:
                    c = locked_positions[(j, i)]
                    position[i][j] = c
        return position









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


class Game(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    # def render(self):
    #     for i in range(len(position)):
    #         for j in range(len(position[i])):
    #             if position[i][j] == 1:
    #                 pygame.draw.rect(screen, "green",
    #                                  [(self.left + (self.cell_size * j), self.top + (self.cell_size * i)),
    #                                   (self.cell_size, self.cell_size)])
    #             if position == 0:
    #                 pygame.draw.rect(screen, "black",
    #                                  [(self.left + (self.cell_size * j), self.top + (self.cell_size * i)),
    #                                   (self.cell_size, self.cell_size)])
    #             pygame.draw.rect(screen, "white",
    #                              [(self.left + (self.cell_size * j), self.top + (self.cell_size * i)),
    #                               (self.cell_size, self.cell_size)], 1)


    # def mov_fig(self):
    #     for i in list_pos:
    #         if pos[1] < i and bool(list_pos):
    #             pos[1] += self.cell_size
    #             position.append(list(pos))
    #     if pos[1] < 560 and not bool(list_pos):
    #         pos[1] += self.cell_size
    #         position.append(list(pos))
    #     print(pos, position)


board = Game(8, 12)
coords = board.cells_coord()
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []

for i in coords:
    if i[1] == 10:
        list1.append(i)
    if i[1] == 60:
        list2.append(i)
    if i[1] == 110:
        list3.append(i)
    if i[1] == 160:
        list4.append(i)
    if i[1] == 210:
        list5.append(i)
    if i[1] == 260:
        list6.append(i)
    if i[1] == 310:
        list7.append(i)
    if i[1] == 360:
        list8.append(i)
    if i[1] == 410:
        list9.append(i)
    if i[1] == 460:
        list10.append(i)
    if i[1] == 510:
        list11.append(i)
    if i[1] == 560:
        list12.append(i)

COORDS = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            pass
        if key[pygame.K_LEFT]:
            pass
        if key[pygame.K_RIGHT]:
            pass
        if key[pygame.K_SPACE]:
            pass
    board.render()
    # board.mov_fig()
    clock.tick(5)
    pygame.display.flip()
pygame.quit()
