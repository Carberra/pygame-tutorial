from collections import deque
from enum import Enum

import pygame as pg

import snek


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


DIRECTION_MAPPING = {
    pg.K_UP: (Direction.UP, Direction.DOWN),
    pg.K_DOWN: (Direction.DOWN, Direction.UP),
    pg.K_LEFT: (Direction.LEFT, Direction.RIGHT),
    pg.K_RIGHT: (Direction.RIGHT, Direction.LEFT),
}


class Snek:
    __slots__ = ("part", "body", "maxlen", "direction", "speed", "movement_delay", "direction_changed")

    def __init__(self, part):
        self.part = part

        w = self.part.get_width()
        h = self.part.get_height()
        x = round((snek.WINDOW_WIDTH / 2) / w) * w
        y = round((snek.WINDOW_HEIGHT / 2) / h) * h

        self.body = deque(
            [snek.Sprite(self.part, x, y), snek.Sprite(self.part, x - w, y)]
        )
        self.maxlen = 2
        self.direction = Direction.RIGHT
        self.speed = 10
        self.movement_delay = 0.
        self.direction_changed = False

    @property
    def movement_interval(self):
        return 1 / self.speed

    def change_direction(self, key):
        if not self.direction_changed:
            for k, (d, o) in DIRECTION_MAPPING.items():
                if key == k:
                    if self.direction != o:
                        self.direction = d
                        self.direction_changed = True
                        break

    def shift(self, x, y):
        self.body.appendleft(snek.Sprite(self.part, x, y))
        if len(self.body) > self.maxlen:
            self.body.pop()

    def extend(self):
        self.maxlen += 1
        self.speed += 1

    def move(self, delta):
        if self.movement_delay < self.movement_interval:
            self.movement_delay += delta
            return

        head = self.body[0]
        movement = [
            (head.x, head.y - head.h),
            (head.x, head.y + head.h),
            (head.x - head.w, head.y),
            (head.x + head.w, head.y)
        ][self.direction.value]

        self.shift(*movement)
        self.movement_delay = 0
        self.direction_changed = False
