import sys

import pygame as pg

import snek


class Client:
    __slots__ = ("clock", "wnd", "scene", "_paused")

    def __init__(self):
        self.clock = pg.time.Clock()
        self.wnd = snek.Window(snek.WINDOW_WIDTH, snek.WINDOW_HEIGHT, snek.WINDOW_CAPTION)
        self.scene = snek.MenuScene(self)

    def run(self):
        while True:
            frame_delta = self.clock.tick() * 1e-3

            events = pg.event.get()
            events = self.scene.handle_events(events)
            if events:
                for event in events:
                    if event.type == pg.QUIT:
                        self.stop()

            self.scene.update(frame_delta)

            if frame_delta < 0.1:
                self.wnd.clear()
                self.scene.draw()
                pg.display.flip()

    def stop(self):
        pg.quit()
        sys.exit()

    def start_game(self):
        self.wnd.clear()
        # Changes the scene
        pg.display.flip()
