import pygame
from datetime import datetime
import math

res = width, height = 1200, 800
fps = 20
h_width, h_height = width // 2, height // 2
radius = h_height - 50
radius_list = {'sec': radius - 10, 'min': radius - 55, 'hour': radius - 100, 'digit': radius - 30}
radius_arc = radius + 8

pygame.init()

surface = pygame.display.set_mode(res)
pygame.display.set_caption('Часики механические, действующие!')
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pygame.font.SysFont('FreeMono', 60, 'bold')
img = pygame.image.load('img/1.png').convert_alpha()
bg = pygame.image.load('img/2.jpg').convert()

bg_rect = bg.get_rect()
bg_rect.center = width, height
dx, dy = 1, 1


def get_clock_pos(clock_dict, clock_hand, key):
    x = h_width + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = h_height + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    dx *= -1 if bg_rect.left > 0 or bg_rect.right < width else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < height else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    surface.blit(bg, bg_rect)
    surface.blit(img, (0, 0))

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    pygame.draw.circle(surface, pygame.Color('DarkSlateGray'), (h_width, h_height), radius)

    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)

    pygame.draw.line(surface, pygame.Color('orange'), (h_width, h_height), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), (h_width, h_height), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), (h_width, h_height), get_clock_pos(clock60, second, 'sec'), 4)

    pygame.draw.circle(surface, pygame.Color('white'), (h_width, h_height), 8)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('ForestGreen'))
    surface.blit(time_render, (0, 0))
    surface.blit(time_render, (width - time_render.get_width(), 0))
    surface.blit(time_render, (0, height - time_render.get_height()))
    surface.blit(time_render, (width - time_render.get_width(), height - time_render.get_height()))

    sec_angle = -math.radians(clock60[t.second]) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('magenta'),
                    (h_width - radius_arc, (h_height - radius_arc), 2 * radius_arc, 2 * radius_arc),
                    math.pi / 2, sec_angle, 8)

    pygame.display.flip()
    clock.tick(fps)
