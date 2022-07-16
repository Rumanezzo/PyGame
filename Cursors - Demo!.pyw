import pygame as pg

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
grey = (140, 140, 140)

#  Частота обновления экрана - кадры в секунду
fps = 60

pg.init()

fnt = pg.font.SysFont('Special Elite', 42, bold=True)

# Берем разрешение экрана
info = pg.display.Info()

# Выставляем размер окна = разрешению экрана
width, height = info.current_w, info.current_h

txt = fnt.render(f'Здесь вы видите Полный Экран с разрешением {width}x{height}', True, white, grey)
screen0 = pg.display.set_mode((width, height))

txt_r = txt.get_rect()
txt_r.centerx = screen0.get_rect().centerx
txt_r.centery = screen0.get_rect().centery

pg.display.set_caption("Меняем вид курсора по клику мыши")
pg.mouse.set_visible(False)

done = False
mouse_down = False
clock = pg.time.Clock()

Cursor = pg.image.load('./res/Cursor_normal_.png')
Cursor_Clicked = pg.image.load('./res/Cursor_clicked_.png')
screen0.fill(grey)
screen0.blit(txt, txt_r)


def draw_cursor(screen, x, y):
    if mouse_down:
        screen.blit(Cursor_Clicked, (x, y - 48))
    else:
        screen.blit(Cursor, (x, y - 48))


while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pg.MOUSEBUTTONUP:
            mouse_down = False

    pos = pg.mouse.get_pos()
    x0, y0 = pos[0], pos[1]
    draw_cursor(screen0, x0, y0)
    pg.display.flip()
    clock.tick(fps)

pg.quit()
