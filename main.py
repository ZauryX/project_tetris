import pygame
import random

size = width, height = 450, 650
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True
flag = None
flag_movr = True
flag_movl = True
clock = pygame.time.Clock()
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
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 3), (255, 0, 3), (255, 0, 3), (255, 7, 3)]]

kvadrat = [[[1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]
pryamay = [[[0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]]

t_obraz = [[[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ],

           [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ], ]

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
# figyry = [pryamay, pryamay, pryamay, pryamay, pryamay, pryamay, pryamay]
figyry_colors = [(255, 215, 0), (63, 0, 255), (255, 0, 0), (255, 0, 0), (0, 255, 0), (77, 70, 255), (255, 69, 0)]


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
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], ]
    # [(255, 0, 3), (255, 0, 3), (255, 0, 3), (0, 0, 0), (255, 0, 3), (255, 0, 3), (255, 0, 3), (255, 7, 3)]]
    for i in range(len(position)):
        for j in range(len(position[i])):
            if (j, i) in occupied:
                a = occupied[(j, i)]
                position[i][j] = a

    return position


class Game(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

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
c1 = []


def formatting(figyra, coords):
    global count, c1
    c = []
    positions = []
    nomer = figyry.index(figyra)
    color = figyry_colors[nomer]
    a, b = coords

    for i, line in enumerate(format):
        for j, column in enumerate(line):
            if column == 1:
                positions.append((a + 50 * j, b + 50 * i))
                if count != 4:
                    count += 1
                    c.append((((a + 50 * j) - 25) // 50, ((b + 50 * i) - 10) // 50))
                    c1 = c

    count = 0
    return drawing(c, color)


def drawing(coord, color):
    for i in coord:
        occupied[i] = color
    sozdanie_polya(occupied)
    return occupied


def emptiness(position):
    global c1, flag_movr, flag_movl
    global change_fig
    flag_movl = True
    flag_movr = True
    for i in c1:
        if i[0] < 6 and i[0] > 0:
            if position[i[1]][i[0] + 1] != (0, 0, 0) and (i[0] + 1, i[1]) not in c1:
                flag_movr = False
            if position[i[1]][i[0] - 1] != (0, 0, 0) and (i[0] - 1, i[1]) not in c1:
                flag_movl = False
        if i[0] == 0:
            flag_movl = False
        if i[0] == 7:
            flag_movr = False
        if i[1] == 11:
            change_fig = True
            return True
        if i[1] != 11:
            if position[i[1] + 1][i[0]] != (0, 0, 0) and (i[0], i[1] + 1) not in c1:
                change_fig = True
                return True

    return False


def clearing_rows():
    count111 = 0

    for i in range(len(position) - 1, -1, -1):
        row = position[i]
        if (0, 0, 0) not in row:
            count111 += 1
            ind = i
            for j in range(len(row)):
                try:
                    del occupied[(j, i)]
                    del dict_of_occ[(j, i)]
                except:
                    continue

    if count111 > 0:
        for key in sorted(list(occupied), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + count111)
                occupied[newKey] = occupied.pop(key)
                dict_of_occ[newKey] = dict_of_occ.pop(key)



def cleaning(position):
    for i in dict_of_occ:
        if i[1] == 0:
            dict_of_occ[i] = (0, 0, 0)
        if i[1] == 1:
            dict_of_occ[i] = (0, 0, 0)


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
# print(COORDS)

coords2 = [175, -90]
flag_to_lose = False


def moving():
    global coords2
    if not emptiness(position):
        coords2[1] += 10

    return coords2


def mov_xr():
    global coords2
    if coords2[0] >= 25 and coords2[0] != 475 and flag_movr:
        coords2[0] += 50


def mov_xl():
    global coords2
    if coords2[0] >= 25 and coords2[0] <= 475 and flag_movl:
        coords2[0] -= 50


def povorot():
    global format
    global count_pov
    if count_pov < len(figyra) - 1:
        count_pov += 1
    else:
        count_pov = 0
    for i in c1:
        if figyra == pryamay:
            if i[0] < 5:
                if flag_movl:
                    format = figyra[count_pov]
            if i[0] > 4:
                if i[0] != 7 and i[0] != 6 and i[0] != 8:
                    if flag_movr:
                        format = figyra[count_pov]
        else:
            if i[0] < 5:
                if flag_movl:
                    format = figyra[count_pov]
            if i[0] > 3:
                if flag_movr:
                    format = figyra[count_pov]
    # format = figyra[count_pov]


figyra = kvadrat
dict_of_occ = {}
change_fig = True
fall_time = 0
count_pov = 0
count_lost = 0

while running:
    count_fix_try = 0
    occupied = {}

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            pass
        if key[pygame.K_LEFT]:
            mov_xl()
        if key[pygame.K_RIGHT]:
            mov_xr()
        if key[pygame.K_UP]:
            povorot()

    if change_fig == True:
        cleaning(position)
        count_fix_try += 1
        nomer = figyry.index(figyra)
        color = figyry_colors[nomer]
        for i in c1:
            dict_of_occ[i] = color
        occupied.update(dict_of_occ)
        figyra = random.choice(figyry)
        if position[2][3] != (0, 0, 0) and position[2][4] != (0, 0, 0):
            flag_to_lose = True
        format = figyra[0]
        clearing_rows()
        coords2 = [175, -90]
        position = sozdanie_polya(formatting(figyra, moving()))
        change_fig = False
    else:
        occupied.update(dict_of_occ)
        position = sozdanie_polya(formatting(figyra, moving()))
    if flag_to_lose:
        break
    board.render()
    clock.tick(20)
    pygame.display.flip()
pygame.quit()
