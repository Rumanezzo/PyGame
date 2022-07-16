import pygame
import math
import random

# Инициализация Pygame и Игрового окна

pygame.init()
width, height = 1240, 550
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Виселица - Hangman - основано на проекте с Youtube-канала "Tech with Yim"')

# Переменные для кнопок
radius = 30
gap = 12
symbols_in_string = 16

letters = []
start_x = round((width - (radius * 2 + gap) * symbols_in_string) / 2)
start_y = 400
a = ord('а')  # Коды латинского алфавита начинаются с 65

for i in range(32):
    x = start_x + gap * 2 + ((radius * 2 + gap) * (i % symbols_in_string))
    y = start_y + ((i // symbols_in_string) * (gap + radius * 2))
    letters.append([x, y, chr(a + i), True])

# Загружаем шрифты
letter_font = pygame.font.SysFont('comicSans', 40)
word_font = pygame.font.SysFont('comicSans', 66)
title_font = pygame.font.SysFont('comicSans', 66)

# Загружаем файлы спрайтов
images = []
for i in range(7):
    image = pygame.image.load('.//res//hangman' + str(i) + '.png')
    images.append(image)

# Игровые переменные
hangman_status = 0
words = ['приказ', 'заказ', 'паразит', 'физик', 'парапет', 'карантин',
         'каркас', 'крокодил', 'самолет', 'синхрофазотрон', 'циклотрон']
word = random.choice(words)
guessed = []

# Заготавливаем Цвета
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


def draw():
    win.fill(white)
    # Рисуем заголовок
    text = title_font.render('Учебный проект - Виселица', True, black)
    win.blit(text, (width / 2 - text.get_width() / 2, 20))
    # Рисуем слово
    display_word = ''
    for _ in word:
        if _ in guessed:
            display_word += _ + ' '
        else:
            display_word += '_ '
    text_ = word_font.render(display_word, True, black)
    win.blit(text_, (400, 200))
    # Рисуем кнопки
    for _ in letters:
        x_, y_, letter_, visible_ = _
        if visible_:
            pygame.draw.circle(win, black, (x_, y_), radius, 3)
            text_ = letter_font.render(letter_, True, black)
            win.blit(text_, (x_ - text_.get_width() / 2, y_ - text_.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message, color_back, color_font):
    pygame.time.delay(5000)
    win.fill(color_back)
    text = word_font.render(message, True, color_font)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global hangman_status
    # Организация игрового цикла
    fps = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                for letter_list in letters:
                    x_, y_, letter, visible = letter_list
                    if visible:
                        dis = math.sqrt((x_ - m_x) ** 2 + (y_ - m_y) ** 2)
                        if dis < radius:
                            letter_list[3] = False
                            guessed.append(letter)
                            if letter not in word:
                                hangman_status += 1
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message('Вы победили!', white, black)
            break
        if hangman_status == 6:
            display_message('Вы проиграли...', black, white)
            break


main()
pygame.quit()
