import pygame as pg


class Text:
    __slots__ = ("_body", "_colour", "x", "y", "w", "h", "size", "align", "font", "renders")

    def __init__(self, body, x, y, size, align="topleft", colour=(255, 255, 255)):
        self._body = body.split("\n")
        self._colour = pg.color.Color(colour)
        self.x = x
        self.y = y
        self.w = 0
        self.h = 0
        self.size = size
        self.align = align

        self.font = pg.font.Font(f"./assets/fonts/DK Lemon Yellow Sun.otf", size)
        self.renders = []
        self.render()

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def body(self):
        return "\n".join(self._body)

    @body.setter
    def body(self, value):
        self._body = value.split("\n")
        self.render()

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if isinstance(value, pg.color.Color):
            self._colour = value
        else:
            self._colour = pg.color.Color(value)

    def render(self):
        self.renders.clear()
        self.w = 0
        self.h = 0

        for i, line in enumerate(self._body):
            surface = self.font.render(line, True, self.colour).convert_alpha()
            self.w = max(self.w, surface.get_width())
            self.h += surface.get_height()

            rect = surface.get_rect()
            setattr(rect, self.align, (self.x, self.y + (surface.get_height() * i)))
            self.renders.append((surface, rect))


class TextButton(Text):
    __slots__ = Text.__slots__ + ("action", "hovering")

    def __init__(self, action, body, x, y, size, align="topleft", colour=(255, 255, 255)):
        super().__init__(body, x, y, size, align, colour)
        self.action = action
        self.hovering = False

    def is_under_mouse(self, pos):
        return self.renders[0][1].collidepoint(pos)

    def on_hover(self, *args, **kwargs):
        if not self.body.startswith("+"):
            self.body = f"+ {self.body} +"
        self.hovering = True
        self.render()

    def on_unhover(self, *args, **kwargs):
        self.body = self.body[2:-2]
        self.hovering = False
        self.render()

    def on_click(self, *args, **kwargs):
        self.action(*args, **kwargs)
