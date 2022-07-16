import pygame
from random import randint
from copy import deepcopy

res = width, height = 1540, 760
tile = 4
w, h = width // tile, height // tile
fps = 10
gen = 0
white = (255, 255, 255)

pygame.init()
surface = pygame.display.set_mode(res)
clock = pygame.time.Clock()

pygame.display.set_caption('Клеточные Автоматы - модель "Жизнь" Джона Конвея - "Conway\'s Game of Life"')
title_font = pygame.font.SysFont('Special Elite', 78)

next_field = [[0 for i in range(w)] for j in range(h)]
# non-random
# cur_field = [[1 if i == w // 2 or j == h // 2 else 0 for i in range(w)] for j in range(h)]
# cur_field = [[1 if not i % 9 else 0 for i in range(w)] for j in range(h)]
# cur_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(w)] for j in range(h)]
# cur_field = [[1 if not (i * j) % 22 else 0 for i in range(w)] for j in range(h)]
# random
cur_field = [[randint(0, 1) for _ in range(w)] for __ in range(h)]
# cur_field = [[1 if not i % 7 else randint(0, 1) for i in range(w)] for j in range(h)]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:

    if gen == 0:
        surface.fill(pygame.Color('forestgreen'))
        text = title_font.render('Игра Джона Конвея "Жизнь"', True, white)

        surface.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)

    surface.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.delay(500)
        if event.type == pygame.MOUSEBUTTONUP:
            exit()

    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, height)) for x in range(0, width, tile)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (width, y)) for y in range(0, height, tile)]
    # draw life
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if cur_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
            next_field[y][x] = check_cell(cur_field, x, y)

    cur_field = deepcopy(next_field)
    gen += 1
    pygame.display.set_caption(f'Клеточные Автоматы - модель "Жизнь" Джона Конвея {gen}-е поколение')

    pygame.display.flip()
    clock.tick(fps)
