import pygame as pg


class Window:
    __slots__ = ("w", "h", "surface")

    def __init__(self, width, height, caption="Pygame Tutorial"):
        self.w = width
        self.h = height
        self.surface = pg.display.set_mode((width, height), flags=pg.HWSURFACE | pg.DOUBLEBUF)
        pg.display.set_caption(caption)

    @property
    def size(self):
        return (self.w, self.h)

    def blit(self, sprite):
        self.surface.blit(sprite.surface, sprite.position)

    def blit_ui(self, text):
        for r in text.renders:
            self.surface.blit(*r)

    def clear(self):
        self.surface.fill((0, 0, 0))
