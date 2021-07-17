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
