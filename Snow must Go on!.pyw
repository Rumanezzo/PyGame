import pygame as pg
from random import randint

pg.init()
pg.mouse.set_visible(False)

info = pg.display.Info()  # Берем разрешение экрана

width, height = info.current_w, info.current_h  # Выставляем размер окна = разрешению экрана
fps = 60

window = pg.display.set_mode((width, height), pg.FULLSCREEN)
pg.display.set_caption('Падающий снег...')

clock = pg.time.Clock()

snow = []
count = 1000
max_size = 5
cur_size = 75

for i in range(count):
    x, y = randint(0, width), randint(0, height)
    size = randint(1, max_size)
    snow.append([x, y, size])

play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            play = False
    mx, my = pg.mouse.get_pos()

    for obj in snow:
        x, y = obj[0], obj[1]
        size = obj[2]
        d = ((mx - x) ** 2 + (my - y) ** 2)
        if d < cur_size ** 2:
            obj[0] += (x - mx) * 0.3
            obj[1] += (y - my) * 0.2

        obj[1] += obj[2]
        if y > height + size:
            obj[0] = randint(0, width)
            obj[1] = -randint(10, 100)

    window.fill(pg.Color('black'))
    for obj in snow:
        x, y = obj[0], obj[1]
        size = obj[2]

        c = 55 + 200 // max_size * size
        color = (c, c, c)

        pg.draw.circle(window, color, (x, y), size)
    pg.draw.circle(window, pg.Color('yellow'), (mx, my), cur_size)
    pg.display.update()
    clock.tick(fps)
pg.quit()
