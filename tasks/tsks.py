from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from save import Save
from tasks.right_side import Right


def log(mssg):
    pass


class A:
    bcbtn = Button(text="BACK", background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))
    layout = BoxLayout(orientation='horizontal')

    def __init__(self, name):
        self.save = Save(name)

        self.right = Right(self.save)
        self.left = self.right.left
        self.name = name

        self.save.son.get_index(name)

        self.right.buttons.add_widget(self.right.dodBtn)
        self.right.buttons.add_widget(self.right.delBtn)
        self.right.dodBtn.bind(on_release=self.right.add.o)

        self.right.add.add.add_widget(self.right.add.name)
        self.right.add.add.add_widget(self.right.add.desc)
        sbm = Button(text='submit', background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))
        sbm.bind(on_release=self.right.subm)
        self.right.add.add.add_widget(sbm)

    def a(self):
        self.left.a(self.name)
        fn = self.right.fn

        for i in self.save.ls:
            left = self.right.left
            if i.completed:
                left.layout.add_widget((Button(text=i.name, size_hint_y=None, height=65, on_release=fn.ed_fn, background_color=(0.37, 0.76, 0.24, 1), color=(0.85, 0.8, 0.9, 1))))
            else:
                left.layout.add_widget((Button(text=i.name, size_hint_y=None, height=65, on_release=fn.ed_fn, background_color=(0.85, 0.88, 0.97, 1), color=(0.85, 0.8, 0.9, 1))))

        if len(self.save.ls) > 8:
            left.layout.add_widget(left.b1)
            left.layout.add_widget(left.b2)

        self.layout.add_widget(self.left.test)
        self.layout.add_widget(self.right.buttons)
        # right.dodBtn.bind(on_press=dod)
        self.right.add_btn(self.bcbtn)

        return self.layout
