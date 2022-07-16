import pygame as pg
import pymunk.pygame_util
from random import randrange

pymunk.pygame_util.positive_y_is_up = False

res = width, height = 1366, 768
fps = 60

pg.init()
surface = pg.display.set_mode(res)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000


def create_ball(space_, pos):
    ball_mass, ball_radius = 1000, 60
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    space_.add(ball_body, ball_shape)


segment_shape = pymunk.Segment(space.static_body, (0, height), (width, height), 20)
segment_shape.elasticity = 0.9
segment_shape.friction = 0.4
space.add(segment_shape)

box_mass, box_size = 10, (60, 40)
for x in range(120, width - 60, box_size[0]):
    for y in range(height // 2, height - 20, box_size[1]):

        box_moment = pymunk.moment_for_box(box_mass, box_size)
        box_body = pymunk.Body(box_mass, box_moment)
        box_body.position = x, y
        box_shape = pymunk.Poly.create_box(box_body, box_size)
        box_shape.elasticity = 0.6
        box_shape.friction = 0.4
        box_shape.color = [randrange(256) for i in range(4)]
        space.add(box_body, box_shape)

while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_ball(space, i.pos)

    space.step(1 / fps)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(fps)
