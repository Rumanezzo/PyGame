import pygame as pg
from math import pi

import pygame.image

pg.init()

# Определения некоторых цветов
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
grind = (0, 128, 1)
yellow = (255, 255, 0)
magenta = (200, 0, 255)
cyan = (0, 200, 255)
orange = (250, 105, 25)

colors = (black, white, blue, green, red, yellow, grey, grind, magenta, cyan, orange)

info = pg.display.Info()  # Берем разрешение экрана
ratio = 9, 10

size = width, height = ratio[0] * info.current_w // ratio[1], ratio[0] * info.current_h // ratio[1]
screen = pg.display.set_mode(size)

pg.display.set_caption("Демонстрация Графических Примитивов")
icon = pygame.image.load('./res/icon.ico')
pg.display.set_icon(icon)

# Loop until the user clicks the close button.
done = False
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            done = True

    screen.fill(grey)

    pg.draw.line(screen, green, [0, 0], [width, height], 10)
    pg.draw.line(screen, red, [width, 0], [0, height], 10)

    pg.draw.line(screen, grind, [0, 0], [0, height], 20)
    pg.draw.line(screen, grind, [width, 0], [width, height], 20)
    pg.draw.line(screen, grind, [0, 0], [width, 0], 20)

    for y_offset in range(0, height, 20):
        pg.draw.line(screen, blue, [0, 3 * y_offset], [width, height // 100 + y_offset], 2)
    draw_lst_rect = [20, 20, width - 40, height - 40]
    # Рисуем прямоугольник
    pg.draw.rect(screen, black, draw_lst_rect, 6)

    pg.draw.ellipse(screen, black, draw_lst_rect, 12)
    pg.draw.ellipse(screen, magenta, [width // 6, height // 6, width // 6, height // 6], 10)
    pg.draw.ellipse(screen, yellow, [width - 2 * width // 6, height // 6, width // 6, height // 6], 10)
    pg.draw.ellipse(screen, blue, [width // 2 - width // 12, 3 * height // 4, width // 6, height // 6], 10)
    pg.draw.ellipse(screen, grind, [5 * width // 12, 5 * height // 12, width // 6, height // 6], 10)

    draw_lst_arc = [80, 80, width - 160, height - 160]
    for _ in range(4):
        pg.draw.arc(screen, colors[_ + 2], draw_lst_arc, _ * pi / 2, (_ + 1) * pi / 2, 8)

    pg.draw.polygon(screen, orange, [[width // 2, 10], [10, height - 10], [width - 10, height - 10]], 12)

    for _ in range(11):
        font = pg.font.SysFont('SpecialElite', 88 - 8 * _, True, False)
        text = font.render(f"Настроечная Таблица №{_ + 1}", True, cyan)
        text_w = text.get_width()
        text_start_x = (width - text_w) / 2

        screen.blit(text, [text_start_x, height // (1.5 + _)])

    pg.display.flip()

    clock.tick(60)
pg.quit()
