from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

schemes = [
    [
        (0, 1),
        "FEF4C0",
        "FDB10B",
        "FE8535",
        "FD292F",
        "B20000"
    ],
    [
        (1, 0),
        "#583E26",
        "#A78B71",
        "#F7C815",
        "#EC9704",
        "#9C4A1A"
    ],
    [
        (1, 0),
        "#1A2902",
        "#344C11",
        "#778D45",
        "#AEC09A",
        "#AEC670"
    ],
    [
        (1, 0),
        "#012E4A",
        "#036280",
        "#378BA4",
        "#81BECE",
        "#E8EDE7"
    ],
    [
        (1, 0),
        "#4F6C77",
        "#9EABB3",
        "#EAEEEF",
        "#F6E8DA",
        "#A7C4D4"
    ],
    [
        (1, 1),
        "#871522",
        "#E0484A",
        "#82204B",
        "#33122A",
        "#0E0613"
    ],
    [
        (1, 1),
        "#640007",
        "#C91959",
        "#E14591",
        "#EBD1EA",
        "#52A051"
    ],
    [
        (0, 1),
        "#D3B19E",
        "#D39CBD",
        "#995E7C",
        "#683142",
        "#312528"
    ]

]


class Scheme(BoxLayout):
    def __init__(self, scheme_id, labels, btns1, btns2, btns3, btns4, win, **kwargs):
        super().__init__(**kwargs)

        self.labels = labels

        self.btns1 = btns1
        self.btns2 = btns2
        self.btns3 = btns3
        self.btns4 = btns4

        self.win = win

        self.scheme = schemes[scheme_id]

        self.btn1 = Button(size_hint_x=1.2, background_normal=self.scheme[1], background_color=self.scheme[1])
        self.btn2 = Button(background_normal=self.scheme[2], background_color=self.scheme[2])
        self.btn3 = Button(background_normal=self.scheme[3], background_color=self.scheme[3])
        self.btn4 = Button(background_normal=self.scheme[4], background_color=self.scheme[4])
        self.btn5 = Button(background_normal=self.scheme[5], background_color=self.scheme[5])

        for btn in [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5]:
            self.add_widget(btn)
            btn.on_press = self.repainting


    def repainting(self):
        self.win.clearcolor = self.scheme[1]
        for btn1 in self.btns1:
            btn1.background_color = self.scheme[2]
        for btn2 in self.btns2:
            btn2.background_color = self.scheme[3]
        for btn3 in self.btns3:
            btn3.background_color = self.scheme[4]
        for btn4 in self.btns4:
            btn4.background_color = self.scheme[5]
        for btn in self.btns1 + self.btns2 + self.btns3 + self.btns4:
            btn.color = "#FFFFFF" if self.scheme[0][1] else "#000000"
        for label in self.labels:
            label.color = "#FFFFFF" if self.scheme[0][0] else "#000000"
