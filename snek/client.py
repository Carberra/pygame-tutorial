import sys

import pygame as pg
from pygame.locals import *

import snek


class Client:
    __slots__ = ("clock", "wnd", "scene", "_paused")

    def __init__(self):
        self.clock = pg.time.Clock()
        self.wnd = snek.Window(snek.WINDOW_WIDTH, snek.WINDOW_HEIGHT, snek.WINDOW_CAPTION)

    def run(self):
        while True:
            frame_delta = self.clock.tick() * 1e-3

            if frame_delta < 0.1:
                self.wnd.clear()
                pg.display.flip()

    def stop(self):
        pg.quit()
        sys.exit()