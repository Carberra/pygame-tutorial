import random

import snek


class Sprite:
    __slots__ = ("surface", "rect")

    def __init__(self, surface, x, y):
        self.surface = surface
        self.rect = surface.get_rect().move(x, y)

    @property
    def w(self):
        return self.rect.w

    @property
    def h(self):
        return self.rect.h

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def size(self):
        return (self.w, self.h)

    def move(self, x=None, y=None):
        if x is None and y is None:
            return

        self.rect.update(
            x if x is not None else self.x,
            y if y is not None else self.y,
            self.w,
            self.h,
        )


class AppleSprite(Sprite):
    __slots__ = Sprite.__slots__

    def __init__(self, surface):
        w = surface.get_width()
        h = surface.get_height()
        super().__init__(
            surface,
            round(random.randint(w, snek.WINDOW_WIDTH - (w * 2)) / w) * w,
            round(random.randint(82, snek.WINDOW_HEIGHT - (h * 2)) / h) * h,
        )

    def teleport(self):
        self.move(
            round(random.randint(self.w, snek.WINDOW_WIDTH - (self.w * 2)) / self.w) * self.w,
            round(random.randint(82, snek.WINDOW_HEIGHT - (self.h * 2)) / self.h) * self.h,
        )
