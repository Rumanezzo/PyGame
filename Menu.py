import pygame as pg

pg.init()
pg.display.set_caption('Интерактивный ввод в Pygame')
icon = pg.image.load('./res/icon.ico')
pg.display.set_icon(icon)

# Берем разрешение экрана
info = pg.display.Info()

# Выставляем размер окна = разрешению экрана
width0, height0 = info.current_w, info.current_h
w0, h0 = width0 // 2, height0 // 2
screen0 = pg.display.set_mode((w0, h0), 0, 32)
color_inactive = pg.Color('dark green')
color_active = pg.Color('light green')

txt = []
step_h = 10  # отступ от верхнего края окна и зазор между областями ввода
h_inp = 36  # высота области ввода
step_w = 10  # отступ от левого края окна

font = pg.font.SysFont('Special Elite', h_inp, bold=False)


class InputBox:
    def __init__(self, x, y, w, h, text='Здесь вводим текст'):
        self.rect = pg.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = font.render(self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.text = ''
            else:
                self.active = False

            self.color = color_active if self.active else color_inactive
        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_RETURN:

                pg.display.set_caption(self.text)
                txt.append(self.text)
                print(txt)

            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                # Перерисовываем текст
            self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Увеличиваем прямоугольник, если текст слишком длинный
        global w0, screen0
        width = max(10, self.txt_surface.get_width())
        if width > w0:
            w0 += 40

            screen0 = pg.display.set_mode((w0, h0), 0, 32)

        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x, self.rect.y))
        pg.draw.rect(screen, self.color, self.rect, 2)


def main():
    clock = pg.time.Clock()
    input_boxes = []
    n_rec = h0 // (h_inp + step_h)

    for _ in range(n_rec):
        input_boxes.append(InputBox(step_w, step_h + (h_inp + step_h) * _, 0, h_inp))

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen0.fill((133, 133, 133))
        for box in input_boxes:
            box.draw(screen0)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
