import pygame
import random

size = width, height = 450, 650
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True
flag = None
clock = pygame.time.Clock()


kvadrat = [[[1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]],
pryamay = [[[1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

t_obraz = [[[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

zigzag1 = [[[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

zigzag2 = [[[1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

ygol_v1 = [[[1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

ygol_v2 = [[[1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

figyry = [kvadrat, pryamay, t_obraz, zigzag1, zigzag2, ygol_v1, ygol_v2]
figyry_colors = [(255, 215, 0), (63, 0, 255), (255, 0, 0), (255, 0, 0), (255, 255, 25), (77, 70, 255), (255, 69, 0)]


class Board:
    def __init__(self, width, height, figyra):
        self.width = width
        self.height = height
        self.left = 25
        self.top = 10
        self.cell_size = 50
        self.figyra = figyra
        fg = random.choice(figyry)
        self.povorot = 0
        self.color = figyry_colors[figyry.index(fg)]

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


def sozdanie_polya(occupied={}):
    position = [
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    for i in range(len(position)):
        for j in range(len(position[i])):
            if (j, i) in occupied:
                a = occupied[(j, i)]
                position[i][j] = a

    # position[]

    return position


class Game(Board):
    def __init__(self, width, height, figyra):
        super().__init__(width, height, figyra)

    def render(self):
        for i in range(len(position)):
            for j in range(len(position[i])):
                pygame.draw.rect(screen, position[i][j],
                                 [(self.left + (self.cell_size * j), self.top + (self.cell_size * i)),
                                  (self.cell_size, self.cell_size)])
                pygame.draw.rect(screen, "white",
                                 [(self.left + (self.cell_size * j), self.top + (self.cell_size * i)),
                                  (self.cell_size, self.cell_size)], 1)




count = 0


def formatting(figyra, coords):
    global count
    c = []
    positions = []
    # format = figyra.figyra[figyra.povorot % len(figyra.figyra)]
    format = figyra[2]
    nomer = figyry.index(figyra)
    color = figyry_colors[nomer]
    a, b = coords

    for i, line in enumerate(format):
        for j, column in enumerate(line):
            if column == 1:
                positions.append((a + 50 * j, b + 50 * i))
                if count != 4:
                    count += 1
                    c.append((((a + 50 * j) - 25) / 50, ((b + 50 * i) - 10) / 50))
    # # for i, pos in enumerate(positions):
    # #     positions[i] = (pos[0] - 2, pos[1] - 4)

    # drawing(c, color)
    count = 0
    return drawing(c, color)


def drawing(coord, color):
    for i in coord:
        occupied[i] = color
    sozdanie_polya(occupied)
    # print(occupied)
    return occupied


def emptiness(figyra, position):
    empty = []
    for i in range(12):
        for j in range(8):
            if position[i][j] == (0, 0, 0):
                empty.append(position[i][j])
    empty = [j for sub in empty for j in sub]
    formatted = formatting(figyra)

    for x in formatted:
        if x not in empty:
            if x[1] > -1:
                return False
    return True


# def mov_fig(self):
#     for i in list_pos:
#         if pos[1] < i and bool(list_pos):
#             pos[1] += self.cell_size
#             position.append(list(pos))
#     if pos[1] < 560 and not bool(list_pos):
#         pos[1] += self.cell_size
#         position.append(list(pos))
#     print(pos, position)


board = Game(8, 12, kvadrat)
# board.render()
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
# print(COORDS)

coords2 = [175, -90]


def moving():
    global coords2
    if coords2[1] <= 460:
        coords2[1] += 50

    return coords2

def mov_x():
    global coords2
    if coords2[0] >= 25 or coords2[0] != 425:
        coords2[0] += 50



while running:
    occupied = {}
    # occupied = drawing()

    # moving(coords2)
    # formatting(kvadrat, coords2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            pass
        if key[pygame.K_LEFT]:
            pass
        if key[pygame.K_RIGHT]:
            mov_x()
        if key[pygame.K_SPACE]:
            pass
    position = sozdanie_polya(formatting(ygol_v1, moving()))
    board.render()
    clock.tick(1)
    pygame.display.flip()
pygame.quit()
