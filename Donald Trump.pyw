import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Попрыгунчик Дональд Трамп')
walk_right = list([pygame.image.load(f'.//res//right_{_}.png') for _ in range(1, 7)])
walk_left = list([pygame.image.load(f'.//res//left_{_}.png') for _ in range(1, 7)])

player_stand = pygame.image.load('.//res//idle.png')
bg = pygame.image.load('.//res//bg.jpg')

clock = pygame.time.Clock()

width = 60
height = 71
x = 50
y = 500 - height - 5
speed = 5

is_jump = False
jump_count = 10

left = False
right = False
anim_count = 0
last_move = 'right'


class Ammunition:
    def __init__(self, x_, y_, radius, color, facing_):
        self.x = x_
        self.y = y_
        self.radius = radius
        self.color = color
        self.facing = facing_
        self.velocity = 8 * facing_

    def draw(self, win_):
        pygame.draw.circle(win_, self.color, (self.x, self.y), self.radius)


def draw_window():
    global anim_count
    win.blit(bg, (0, 0))

    if anim_count + 1 >= 30:
        anim_count = 0

    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(player_stand, (x, y))
        anim_count += 1
    for bullet_ in bullets:
        bullet_.draw(win)

    pygame.display.update()


run = True
bullets = []

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LALT]:
        if last_move == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(Ammunition(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        last_move = 'left'
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed
        left = False
        right = True
        last_move = 'right'
    else:
        left = False
        right = False
        anim_count = 0
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw_window()

pygame.quit()
