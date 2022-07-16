import pygame as pg
from datetime import datetime
from math import cos, sin, radians, pi

pg.init()
# Берем разрешение экрана
info = pg.display.Info()

# Выставляем размер окна = разрешению экрана
res = width, height = info.current_w, info.current_h

screen0 = pg.display.set_mode((width, height))

fps = 20
h_width, h_height = width // 2, height // 2
radius = h_height - 50
radius_list = {'sec': radius - 10, 'min': radius - 55, 'hour': radius - 100, 'digit': radius - 30}
radius_arc = radius + 8

surface = pg.display.set_mode(res)
pg.display.set_caption('Часики механические, действующие!')
clock = pg.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pg.font.SysFont('FreeMono', 60, 'bold')
img = pg.image.load('./res/circ.png').convert_alpha()
bg = pg.image.load('./res/bg1.jpg').convert()

bg_rect = bg.get_rect()
bg_rect.center = width, height
img_rect = img.get_rect()
img_rect.center = width // 2, height // 2
dx, dy = 1, 1


def get_clock_pos(clock_dict, clock_hand, key):
    x = h_width + radius_list[key] * cos(radians(clock_dict[clock_hand]) - pi / 2)
    y = h_height + radius_list[key] * sin(radians(clock_dict[clock_hand]) - pi / 2)
    return x, y


while True:
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            exit()

    dx *= -1 if bg_rect.left > 0 or bg_rect.right < width else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < height else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    surface.blit(bg, bg_rect)
    surface.blit(img, img_rect)

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    pg.draw.circle(surface, pg.Color('DarkSlateGray'), (h_width, h_height), radius)

    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pg.draw.circle(surface, pg.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)

    pg.draw.line(surface, pg.Color('orange'), (h_width, h_height), get_clock_pos(clock60, hour, 'hour'), 15)
    pg.draw.line(surface, pg.Color('green'), (h_width, h_height), get_clock_pos(clock60, minute, 'min'), 7)
    pg.draw.line(surface, pg.Color('magenta'), (h_width, h_height), get_clock_pos(clock60, second, 'sec'), 4)

    pg.draw.circle(surface, pg.Color('white'), (h_width, h_height), 8)

    time_render = font.render(f'{t:%H:%M:%S}', True, pg.Color('ForestGreen'))
    surface.blit(time_render, (0, 0))
    surface.blit(time_render, (width - time_render.get_width(), 0))
    surface.blit(time_render, (0, height - time_render.get_height()))
    surface.blit(time_render, (width - time_render.get_width(), height - time_render.get_height()))

    sec_angle = -radians(clock60[t.second]) + pi / 2
    pg.draw.arc(surface, pg.Color('magenta'),
                (h_width - radius_arc, (h_height - radius_arc), 2 * radius_arc, 2 * radius_arc),
                pi / 2, sec_angle, 8)

    pg.display.flip()
    clock.tick(fps)
