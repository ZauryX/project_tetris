import pygame

size = width, height = 450, 750
screen = pygame.display.set_mode(size)
pygame.init()
pygame.display.set_caption('Tetris')
running = True
position = []
clock = pygame.time.Clock()
pos = [225, 10]
list_pos = []


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

    def click_on(self, cell):
        position[cell[1]][cell[0]] = (position[cell[1]][cell[0]] + 1) % 2

    # def next_move(self):
    #     board_copy = copy.deepcopy(position)
    #     for i in range(self.width):
    #         for j in range(self.height):
    #             s = 0
    #             for di in [-1, 0, 1]:
    #                 for dj in [-1, 0, 1]:
    #                     if 0 <= i + di < self.width and 0 <= j + dj < self.height:
    #                         s += position[i + di][j + dj]
    #             s -= position[i][j]
    #             if s == 3:
    #                 board_copy[i][j] = 1
    #             if s < 2 or s > 3:
    #                 board_copy[i][j] = 0
    #     position = copy.deepcopy(board_copy)

    def mov_fig(self):
        for i in list_pos:
            if pos[1] < i and bool(list_pos):
                pos[1] += self.cell_size
                position.append(list(pos))
        if pos[1] < 560 and not bool(list_pos):
            pos[1] += self.cell_size
            position.append(list(pos))
        print(pos, position)


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

kvadrat = [[0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

pryamay = [[0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0], ]

pryamay2 = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

t_obraz = [[0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

t_obraz2 = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

t_obraz3 = [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

t_obraz4 = [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

zigzag = [[0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0], ]

zigzag2 = [[0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

zigzag3 = [[0, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

zigzag4 = [[0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v1 = [[0, 0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v12 = [[0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v13 = [[0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v14 = [[0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v2 = [[0, 0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v21 = [[0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v22 = [[0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

ygol_v23 = [[0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]

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
    board.mov_fig()
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
