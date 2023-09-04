# Pygame-каркас для нового проекта Pygame
import pygame as pg
from sys import exit

width = 1240
height = 600
fps = 30

# Задаем цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grind = (0, 128, 1)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (200, 0, 255)
cyan = (0, 200, 255)
orange = (250, 105, 25)

# Создаем игру и окно
pg.init()
# Инициализируем звук
pg.mixer.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Здесь название игры - Заголовок!")
clock = pg.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(fps)
    # Ввод процесса (события)
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        # проверяем на закрытие окна или нажатия ESC
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            running = False

    # Здесь пишем все, что должно обновляться каждый цикл

    # Рендеринг
    screen.fill(black)
    # После отрисовки всего, переворачиваем экран и только после этого - видим на экране:
    pg.display.flip()
    # Или обновляем какой-нибудь кусочек экрана:
    # pg.display.update((400, 300)) - например!

pg.quit()
exit()
