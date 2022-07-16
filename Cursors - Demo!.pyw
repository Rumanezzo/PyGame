import pygame

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

pygame.init()

fnt = pygame.font.SysFont('Special Elite', 42, bold=True)

# Берем разрешение экрана
info = pygame.display.Info()

# Выставляем размер окна = разрешению экрана
width, height = info.current_w, info.current_h

txt = fnt.render(f'Здесь вы видите Полный Экран с разрешением {width}x{height}', True, white, grey)
screen0 = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

txt_r = txt.get_rect()
txt_r.centerx = screen0.get_rect().centerx
txt_r.centery = screen0.get_rect().centery

pygame.display.set_caption("Меняем вид курсора по клику мыши")
pygame.mouse.set_visible(False)

done = False
mouse_down = False
clock = pygame.time.Clock()

Cursor = pygame.image.load('./res/Cursor_normal_.png')
Cursor_Clicked = pygame.image.load('./res/Cursor_clicked_.png')
screen0.fill(grey)
screen0.blit(txt, txt_r)


def draw_cursor(screen, x, y):
    if mouse_down:
        screen.blit(Cursor_Clicked, (x, y - 48))
    else:
        screen.blit(Cursor, (x, y - 48))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

    pos = pygame.mouse.get_pos()
    x0, y0 = pos[0], pos[1]
    draw_cursor(screen0, x0, y0)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
