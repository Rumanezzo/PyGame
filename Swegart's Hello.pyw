import pygame
import sys
from pygame.locals import *

pygame.init()
width = 1360
height = 660

window = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Привет от книги "Учим Python, делая крутые игры"!')

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

font = pygame.font.SysFont('SpecialElite', 42, bold=True)
#  Готовим текст к выводу на экран
txt = font.render('Самая первая PyGame-программа по версии одной книжки', True, white, grey)
# Получаем размеры прямоугольника, в который вписан текст
txt_r = txt.get_rect()
txt_r.centerx = window.get_rect().centerx
txt_r.centery = window.get_rect().centery
window.fill(gray)

pygame.draw.polygon(window, grind, ((width // 2, 0), (width, height // 3),
                                    (3 * width // 4, height), (width // 2, 3 * height // 4),
                                    (width // 4, height), (0, height // 3)), 10)

pygame.draw.line(window, blue, (60, 60), (width - 60, 60), 16)
pygame.draw.line(window, blue, (width - 60, 60), (60, height - 60), 10)
pygame.draw.line(window, blue, (60, height - 60), (width - 60, height - 60), 4)

pygame.draw.circle(window, yellow, (width // 2, height // 2), 200, 18)
pygame.draw.circle(window, orange, (width // 2, height // 2), 220, 10)
pygame.draw.ellipse(window, red, (0, 0, width, height), 10)

pygame.draw.rect(window, green, (txt_r.left - 10,
                                 txt_r.top - 10,
                                 txt_r.width + 20,
                                 txt_r.height + 20), 4)
#  Выводим подготовленный текст на экран
window.blit(txt, txt_r)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
            pygame.quit()
            sys.exit()
