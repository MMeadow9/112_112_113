from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from scheme import Scheme
from timer import Timer

colors = {
    "red": ["#DD1212", "#770606", "#FFFFFF"],
    "orange": ["#DD6212", "#773106", "#FFFFFF"],
    "yellow": ["#DDD212", "#777106", "#000000"],
    "green": ["#12FF12", "#068806", "#FFFFFF"],
    "cyan": ["#12BBDD", "#066677", "#FFFFFF"],
    "purple": ["#9912DD", "#500677", "#FFFFFF"],
    "gray": ["#AAAAAA", "#565656", "#FFFFFF"]
}

Window.clearcolor = colors["gray"][0]
btn_color = colors["gray"][1]
text_color = colors["gray"][2]

alpha = 0
beta = 0.98
gamma = 0.5

numbers = "112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 118 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 118 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 117 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 116 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 115 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 114 112 112 113 112 112 113 112 112 119 "

def set_scheme(color_name):
    global btn_color

    color = colors[color_name]
    Window.clearcolor = color[0]
    btn_color = color[1]


buttons_CC = []  # Buttons Change Color
labels_CC = []  # Labels Change Color

lbls = []

btns_1, btns_2, btns_3, btns_4 = [], [], [], []

count = 0

def zeroing():
    global count
    count = 0


def increase():
    global count
    count += 1


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = Label(text="112-112-113", font_size=50, size_hint_y=3, bold=True, italic=True)

        self.play_btn = Button(text="Играть", background_normal=btn_color, background_color=btn_color, font_size=35, size_hint_y=5)
        self.scheme_btn = Button(text="Изменить цветовую схему", font_size=20, background_normal=btn_color, background_color=btn_color, size_hint_y=5)

        buttons_CC.extend([self.play_btn, self.scheme_btn])
        labels_CC.append(self.title)

        self.play_btn.on_press = self.to_play

        self.scheme_btn.on_press = self.to_colors

        self.line = BoxLayout(orientation='vertical', padding=16, spacing=24)
        [self.line.add_widget(widget) for widget in [self.title, self.play_btn, self.scheme_btn]]

        btns_2.append(self.play_btn)
        btns_4.append(self.scheme_btn)

        self.add_widget(self.line)

    def to_play(self):
        zeroing()
        self.manager.transition.direction = "down"
        self.manager.current = 'play'


    def to_colors(self):
        self.manager.transition.direction = "up"
        self.manager.current = 'colors'


class ColorsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.r_btn = Button(background_normal=colors["red"][0], background_color=colors["red"][0])
        self.o_btn = Button(background_normal=colors["orange"][0], background_color=colors["orange"][0])
        self.y_btn = Button(background_normal=colors["yellow"][0], background_color=colors["yellow"][0])
        self.g_btn = Button(background_normal=colors["green"][0], background_color=colors["green"][0])
        self.c_btn = Button(background_normal=colors["cyan"][0], background_color=colors["cyan"][0])
        self.p_btn = Button(background_normal=colors["purple"][0], background_color=colors["purple"][0])

        self.gray_btn = Button(background_normal=colors["gray"][0], background_color=colors["gray"][0])

        self.back_btn = Button(text="Назад", font_size=28, background_normal=btn_color, background_color=btn_color)

        self.color_text = Label(text="Выбор цвета", font_size=25)

        self.schemes_btn = Button(text="К схемам", font_size=26, background_normal=btn_color, background_color=btn_color)

        self.r_btn.on_press = self.red
        self.o_btn.on_press = self.orange
        self.y_btn.on_press = self.yellow
        self.g_btn.on_press = self.green
        self.c_btn.on_press = self.cyan
        self.p_btn.on_press = self.purple

        self.gray_btn.on_press = self.gray

        self.back_btn.on_press = self.to_main

        self.schemes_btn.on_press = self.to_schemes

        buttons_CC.extend([self.back_btn, self.schemes_btn])
        labels_CC.extend([self.color_text])
        btns_1.append(self.back_btn)
        btns_4.append(self.schemes_btn)

        self.layout1 = BoxLayout(padding=6, spacing=15)
        self.layout2 = BoxLayout(padding=6, spacing=15)
        self.layout3 = BoxLayout(padding=6, spacing=15)
        self.layout4 = BoxLayout(padding=6, spacing=15, size_hint_y=1.25)
        self.layout5 = BoxLayout(padding=6, spacing=15, size_hint_y=1.25)

        [self.layout1.add_widget(widget) for widget in [self.r_btn, self.o_btn]]
        [self.layout2.add_widget(widget) for widget in [self.y_btn, self.g_btn]]
        [self.layout3.add_widget(widget) for widget in [self.c_btn, self.p_btn]]
        [self.layout4.add_widget(widget) for widget in [self.back_btn, self.gray_btn]]
        [self.layout5.add_widget(widget) for widget in [self.color_text, self.schemes_btn]]

        self.layout_main = BoxLayout(orientation='vertical', padding=14, spacing=3)

        [self.layout_main.add_widget(widget) for widget in
         [self.layout4, self.layout1, self.layout2, self.layout3, self.layout5]]

        self.add_widget(self.layout_main)

    def red(self):
        set_scheme("red")
        for button in buttons_CC:
            button.background_color = colors["red"][1]
            button.color = colors["red"][2]
        for label in labels_CC:
            label.color = colors["red"][2]

    def orange(self):
        set_scheme("orange")
        for button in buttons_CC:
            button.background_color = colors["orange"][1]
            button.color = colors["orange"][2]
        for label in labels_CC:
            label.color = colors["orange"][2]

    def yellow(self):
        set_scheme("yellow")
        for button in buttons_CC:
            button.background_color = colors["yellow"][1]
            button.color = colors["yellow"][2]
        for label in labels_CC:
            label.color = colors["yellow"][2]

    def green(self):
        set_scheme("green")
        for button in buttons_CC:
            button.background_color = colors["green"][1]
            button.color = colors["green"][2]
        for label in labels_CC:
            label.color = colors["green"][2]

    def cyan(self):
        set_scheme("cyan")
        for button in buttons_CC:
            button.background_color = colors["cyan"][1]
            button.color = colors["cyan"][2]
        for label in labels_CC:
            label.color = colors["cyan"][2]

    def purple(self):
        set_scheme("purple")
        for button in buttons_CC:
            button.background_color = colors["purple"][1]
            button.color = colors["purple"][2]
        for label in labels_CC:
            label.color = colors["purple"][2]

    def gray(self):
        set_scheme("gray")
        for button in buttons_CC:
            button.background_color = colors["gray"][1]
            button.color = colors["gray"][0]
        for label in labels_CC:
            label.color = colors["gray"][2]

    def to_main(self):
        self.manager.transition.direction = "down"
        self.manager.current = 'main'

    def to_schemes(self):
        self.manager.transition.direction = "up"
        self.manager.current = 'schemes'


class PlayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.is_started = False

        self.nums = Label(text=numbers[count:count + 20], font_size=25)

        self.one_btn = Button(text="1", font_size=45, background_normal=btn_color, background_color=btn_color, size_hint_x=.8)
        self.two_btn = Button(text="2", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.three_btn = Button(text="3", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.four_btn = Button(text="4", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.five_btn = Button(text="5", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.six_btn = Button(text="6", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.seven_btn = Button(text="7", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.eight_btn = Button(text="8", font_size=45, background_normal=btn_color, background_color=btn_color)
        self.nine_btn = Button(text="9", font_size=45, background_normal=btn_color, background_color=btn_color)

        self.one_btn.on_press = self.check1
        self.two_btn.on_press = self.check2
        self.three_btn.on_press = self.check3
        self.four_btn.on_press = self.check4
        self.five_btn.on_press = self.check5
        self.six_btn.on_press = self.check6
        self.seven_btn.on_press = self.check7
        self.eight_btn.on_press = self.check8
        self.nine_btn.on_press = self.check9

        [button.set_disabled(True) for button in
         [self.one_btn, self.two_btn, self.three_btn, self.four_btn, self.five_btn, self.six_btn, self.seven_btn,
          self.eight_btn, self.nine_btn]]

        self.start_btn = Button(text="Начать", font_size=23, background_normal=btn_color, background_color=btn_color)

        self.timer = Timer(3, font_size=50)
        self.timer.bind(done=self.to_main)
        labels_CC.append(self.timer)

        self.back_btn = Button(text="Назад", font_size=26, background_normal=btn_color, background_color=btn_color)

        self.back_btn.on_press = self.to_main
        self.start_btn.on_press = self.start

        self.layout1 = BoxLayout(padding=7)
        self.layout2 = BoxLayout(size_hint_y=2.25, spacing=10, padding=7)
        self.layout3 = BoxLayout(size_hint_y=1.5, spacing=10, padding=7)
        self.layout4 = BoxLayout(size_hint_y=1.5, spacing=10, padding=7)
        self.layout5 = BoxLayout(size_hint_y=1.5, spacing=10, padding=7)

        self.layout1.add_widget(self.nums)

        [self.layout2.add_widget(widget) for widget in [self.one_btn, self.start_btn]]
        [self.layout3.add_widget(widget) for widget in [self.two_btn, self.three_btn, self.four_btn]]
        [self.layout4.add_widget(widget) for widget in [self.five_btn, self.six_btn, self.seven_btn]]
        [self.layout5.add_widget(widget) for widget in [self.eight_btn, self.nine_btn, self.back_btn]]

        self.layout_main = BoxLayout(orientation='vertical', padding=14, spacing=6)

        [self.layout_main.add_widget(widget) for widget in
         [self.layout1, self.layout2, self.layout3, self.layout4, self.layout5]]

        buttons_CC.extend([self.one_btn, self.two_btn, self.three_btn, self.four_btn, self.five_btn, self.six_btn, self.seven_btn, self.eight_btn, self.nine_btn, self.start_btn, self.back_btn])
        labels_CC.append(self.nums)

        btns_1.extend([self.one_btn, self.start_btn])
        btns_2.extend([self.two_btn, self.three_btn, self.four_btn])
        btns_3.extend([self.five_btn, self.six_btn, self.seven_btn])
        btns_4.extend([self.eight_btn, self.nine_btn, self.back_btn])

        self.add_widget(self.layout_main)

    def to_main(self, *args):
        self.timer.done = True
        [button.set_disabled(True) for button in [self.one_btn, self.two_btn, self.three_btn, self.four_btn, self.five_btn, self.six_btn, self.seven_btn,
            self.eight_btn, self.nine_btn]]
        self.restart()
        zeroing()
        self.nums.text = numbers[count:count + 20]
        self.manager.transition.direction = "up"
        self.manager.current = 'main'

    def start(self):
        self.is_started = True
        [button.set_disabled(False) for button in
         [self.one_btn, self.two_btn, self.three_btn, self.four_btn, self.five_btn, self.six_btn, self.seven_btn,
          self.eight_btn, self.nine_btn]]
        self.layout2.remove_widget(self.start_btn)
        self.layout2.add_widget(self.timer)
        self.timer.start()

    def restart(self):
        if self.start_btn not in self.layout2.children:
            self.layout2.remove_widget(self.timer)
            self.layout2.add_widget(self.start_btn)
        self.timer = Timer(3, font_size=50)
        self.timer.bind(done=self.to_main)
        labels_CC.append(self.timer)

    def next(self):
        self.timer.current = 0
        self.timer.total = max(round(self.timer.total * beta + alpha, 4), gamma)
        increase()
        if self.nums.text[0] == " ":
            increase()
        self.nums.text = numbers[count:count + 20]

    def check1(self):
        if self.nums.text.replace(" ", "")[0] == "1":
            self.next()
        else:
            self.to_main()

    def check2(self):
        if self.nums.text.replace(" ", "")[0] == "2":
            self.next()
        else:
            self.to_main()

    def check3(self):
        if self.nums.text.replace(" ", "")[0] == "3":
            self.next()
        else:
            self.to_main()

    def check4(self):
        if self.nums.text.replace(" ", "")[0] == "4":
            self.next()
        else:
            self.to_main()

    def check5(self):
        if self.nums.text.replace(" ", "")[0] == "5":
            self.next()
        else:
            self.to_main()

    def check6(self):
        if self.nums.text.replace(" ", "")[0] == "6":
            self.next()
        else:
            self.to_main()

    def check7(self):
        if self.nums.text.replace(" ", "")[0] == "7":
            self.next()
        else:
            self.to_main()

    def check8(self):
        if self.nums.text.replace(" ", "")[0] == "8":
            self.next()
        else:
            self.to_main()

    def check9(self):
        if self.nums.text.replace(" ", "")[0] == "9":
            self.next()
        else:
            self.to_main()


class SchemesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.back_btn = Button(text="К цветам", size_hint_y=0.8, font_size=25, background_normal=btn_color, background_color=btn_color)

        btns_1.append(self.back_btn)

        self.scheme1 = Scheme(0, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme2 = Scheme(1, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme3 = Scheme(2, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme4 = Scheme(3, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme5 = Scheme(4, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme6 = Scheme(5, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme7 = Scheme(6, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)
        self.scheme8 = Scheme(7, labels_CC, btns_1, btns_2, btns_3, btns_4, Window)

        self.layout1 = BoxLayout(spacing=16)
        self.layout2 = BoxLayout(spacing=16)
        self.layout3 = BoxLayout(spacing=16)
        self.layout4 = BoxLayout(spacing=16)

        [self.layout1.add_widget(scheme) for scheme in [self.scheme1, self.scheme2]]
        [self.layout2.add_widget(scheme) for scheme in [self.scheme3, self.scheme4]]
        [self.layout3.add_widget(scheme) for scheme in [self.scheme5, self.scheme6]]
        [self.layout4.add_widget(scheme) for scheme in [self.scheme7, self.scheme8]]

        buttons_CC.append(self.back_btn)

        self.layout_main = BoxLayout(orientation="vertical", padding=17, spacing=18)

        self.layout_main.add_widget(self.back_btn)

        [self.layout_main.add_widget(layout) for layout in [self.layout1, self.layout2, self.layout3, self.layout4]]

        self.back_btn.on_press = self.to_colors

        self.add_widget(self.layout_main)

    def to_colors(self):
        self.manager.transition.direction = "down"
        self.manager.current = 'colors'


class Game(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ColorsScreen(name='colors'))
        sm.add_widget(PlayScreen(name='play'))
        sm.add_widget(SchemesScreen(name='schemes'))
        return sm

app = Game()
app.run()
