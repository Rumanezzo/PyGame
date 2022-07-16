import pygame as pg
import random
import math

vec2, vec3 = pg.math.Vector2, pg.math.Vector3

res = width, height = 1600, 900
num_stars = 1500
center = vec2(width // 2, height // 2)
colors = 'blue cyan SkyBlue purple magenta'.split()
z_distance = 140
alpha = 30


class Star:
    def __init__(self, app_):
        self.screen = app_.screen
        self.pos3d = self.get_pos3d()
        #  self.vel = random.uniform(0.05, 0.25)
        self.vel = random.uniform(0.45, 0.95)
        self.color = random.choice(colors)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    @staticmethod
    def get_pos3d(scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        #  radius = random.randrange(height // scale_pos, height) * scale_pos
        radius = random.randrange(height // 4, height // 3) * scale_pos
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return vec3(x, y, z_distance)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d

        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + center
        self.size = (z_distance - self.pos3d.z) / (0.2 * self.pos3d.z)
        # rotate xy
        self.pos3d.xy = self.pos3d.xy.rotate(0.2)
        # mouse
        # mouse_pos = CENTER - vec2(pg.mouse.get_pos())
        # self.screen_pos += mouse_pos

    def draw(self):
        s = self.size
        if (-s < self.screen_pos.x < width + s) and (-s < self.screen_pos.y < height + s):
            pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))


class StarField:
    def __init__(self, app_):
        self.stars = [Star(app_) for _ in range(num_stars)]

    def run(self):
        [star.update() for star in self.stars]
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res)
        self.alpha_surface = pg.Surface(res)
        self.alpha_surface.set_alpha(alpha)
        self.clock = pg.time.Clock()
        self.star_field = StarField(self)

    def run(self):
        while True:
            # self.screen.fill('black')
            self.screen.blit(self.alpha_surface, (0, 0))
            self.star_field.run()

            pg.display.flip()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
