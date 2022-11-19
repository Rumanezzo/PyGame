import pygame as pg
import sys
import os

fontname = 'Special Elite.ttf'
pg.init()
pg.mouse.set_visible(False)

# Берем разрешение экрана
info = pg.display.Info()

# Выставляем размер окна = разрешению экрана
width, height = info.current_w, info.current_h

window = pg.display.set_mode((width, height), 0, 32)

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
gray = (160, 160, 160)
grind = (0, 128, 1)
yellow = (255, 255, 0)
magenta = (200, 0, 255)
cyan = (0, 200, 255)
orange = (250, 105, 25)


def txt_rndr(txt_str, font, flag=True, x=None, y=None):
    #  Готовим текст к выводу на экран, либо указанным цветом, либо цветом фона, в зависимости от флага flag
    txt = font.render(txt_str, True, black, gray) if flag else font.render(txt_str, True, gray, gray)
    # Получаем размеры прямоугольника, в который вписан текст
    txt_r = txt.get_rect()

    if x is not None:
        txt_r.centerx = x
    else:
        txt_r.centerx = window.get_rect().centerx
    if y is not None:
        txt_r.centery = y
    else:
        txt_r.centery = window.get_rect().centery
    return txt, txt_r


def greed():
    for i in range(1, height, 10):
        pg.draw.line(window, grey, (1, i), (width, i), 1)
    for i in range(1, width, 10):
        pg.draw.line(window, grey, (i, 1), (i, height), 1)


def draw_frm(k_w=1, k_h=1):
    pg.draw.circle(window, green, (k_w * width // 16, k_h * height // 8), height // 11, 10)
    pg.draw.circle(window, grind, (k_w * width // 16, k_h * height // 8), height // 12, 10)
    pg.draw.circle(window, magenta, (k_w * width // 16, k_h * height // 8), height // 40, 2)
    pg.draw.circle(window, cyan, (k_w * width // 16, k_h * height // 8), height // 25, 4)
    pg.draw.circle(window, red, (k_w * width // 16, k_h * height // 8), height // 50)


window.fill(gray)

pg.draw.ellipse(window, red, (0, 0, width, height), 20)
pg.draw.ellipse(window, orange, (20, 20, width - 40, height - 40), 10)

list_txt = []

if len(sys.argv) > 1:
    openfile = sys.argv[1]
else:
    for file in os.listdir("."):
        if file.endswith(".txt"):
            list_txt.append(os.path.join('', file))
    if len(list_txt):
        openfile = list_txt[0]
    else:
        openfile = None

if openfile:
    with open(openfile, 'r', encoding='utf8') as f:
        poem = f.read().split('\n')
else:
    poem = ['Ошибочка вышла!', 'Нечего выводить: нужен файл с текстом!', 'Положи его рядом с программой!']

#  Готовим текст для вывода на экран

start = 0

running = True
size_font = 68

font0 = pg.font.Font(fontname, size_font)
txt0, txt0_r = txt_rndr(poem[start], font0)
window.blit(txt0, txt0_r)

draw_frm()
draw_frm(15, 1)
draw_frm(1, 7)
draw_frm(15, 7)
greed()

pg.display.update()

while running:
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN or keys[pg.K_RETURN]:

            txt0, txt0_r = txt_rndr(poem[start], font0, False)

            window.blit(txt0, txt0_r)

            start %= len(poem) - 1
            start += 1

            size_font = int(56 + 10 * start % 30)
            font0 = pg.font.Font(fontname, size_font)
            txt0, txt0_r = txt_rndr(poem[start], font0)

            if txt0_r.width > width - 40:
                size_font = 56
                font0 = pg.font.Font(fontname, size_font)
                txt0, txt0_r = txt_rndr(poem[start], font0)

            window.blit(txt0, txt0_r)

            greed()

            pg.display.update()

pg.quit()
sys.exit()
