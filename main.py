import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("BOx gAmE")

line_width = 6
markers = []
click = False
pos = []
player = 1
winner = 0
end = False
green = (0, 255, 0)
red = (255, 0, 0)


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)


for x in range(3):
    row = [0] * 3
    markers.append(row)


def draw_marker():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def check_winner():

    global winner
    global end

    y_pos = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            end = True
    for x in markers:
        if sum(x) == -3:
            winner = 2
            end = True
        if markers[0][y_pos] * markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            end = True
        if markers[0][y_pos] * markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            end = True
        y_pos += 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or  markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        end = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or  markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        end = True


run = True
while run:

    draw_grid()
    draw_marker()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if end == False:
            if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click = True
            if event.type == pygame.MOUSEBUTTONUP and click == True:
                click = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    pygame.display.update()

pygame.quit()
