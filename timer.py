from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        my_text = str(self.total - self.current) + " s"
        super().__init__(text=my_text, **kwargs)

    def start(self):
        Clock.schedule_interval(self.change, 0.02)

    def change(self, dt):
        self.current += 0.024
        self.text = str(round(self.total - self.current, 2)).ljust(4, "0") + " s"
        if self.current >= self.total:
            self.done = True
            return False
        if self.done:
            return False
