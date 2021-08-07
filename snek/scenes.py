__all__ = ("MenuScene", "MainScene")


import abc

import pygame as pg

import snek


class Scene(metaclass=abc.ABCMeta):
    __slots__ = ("client", "wnd", "frames", "timer")

    def __init__(self, client):
        self.client = client
        self.wnd = client.wnd
        self.frames = 0
        self.timer = 0

    @property
    def fps(self):
        if not self.timer:
            return 0

        return self.frames / self.timer

    def handle_events(self, events):
        return events

    def update(self, delta):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError


class MenuScene(Scene):
    __slots__ = Scene.__slots__ + ("background", "title", "play_button", "quit_button", "buttons")

    def __init__(self, client):
        super().__init__(client)
        self.background = snek.Sprite(pg.image.load("./assets/backgrounds/menu.jpg").convert(), 0, 0)
        self.title = snek.Text("+ SNEK +", snek.WINDOW_WIDTH / 2, snek.WINDOW_HEIGHT * 0.4, 100, align="center")
        self.play_button = snek.TextButton(
            self.client.start_game, "Play game", snek.WINDOW_WIDTH / 2,
            snek.WINDOW_HEIGHT * 0.55, 50, align="center",
        )
        self.quit_button = snek.TextButton(
            self.client.stop, "Quit", snek.WINDOW_WIDTH / 2,
            snek.WINDOW_HEIGHT * 0.65, 50, align="center",
        )
        self.buttons = (self.play_button, self.quit_button)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.MOUSEMOTION:
                for button in self.buttons:
                    if button.is_under_mouse(event.pos):
                        button.on_hover()
                        events.remove(event)
                    elif button.hovering:
                        button.on_unhover()
                        events.remove(event)

            elif event.type == pg.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.is_under_mouse(event.pos):
                        button.on_click()
                        events.remove(event)

    def update(self, delta):
        pass

    def draw(self):
        self.wnd.blit(self.background)
        for i in (self.title, *self.buttons):
            self.wnd.blit_ui(i)


class MainScene(Scene):
    __slots__ = Scene.__slots__ + ("background", "apple", "snek")

    def __init__(self, client):
        super().__init__(client)
        self.background = snek.Sprite(pg.image.load("./assets/backgrounds/board.png").convert(), 0, 0)
        self.apple = snek.AppleSprite(pg.image.load("./assets/sprites/apple.png").convert_alpha())
        self.snek = snek.Snek(pg.image.load("./assets/sprites/snekpart.png").convert_alpha())

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                self.snek.change_direction(event.key)
        return events

    def update(self, delta):
        self.timer += delta
        self.snek.move(delta)

    def draw(self):
        # self.wnd.blit(self.background)
        self.wnd.blit(self.apple)
        for part in self.snek.body:
            self.wnd.blit(part)
