import abc


class Scene(metaclass=abc.ABCMeta):
    __slots__ = ("client", "wnd", "frames", "timer")

    def __init__(self, client):
        self.client = client
        self.wnd = wnd
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
