from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from tasks.left import Left
from tasks.ed_fn import Fn
from tasks.add import Add
from son import Files

son = Files()


class Right:
    dodBtn = Button(text="+", background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))

    buttons = BoxLayout(orientation='vertical', size_hint_x=0.35)

    def __init__(self, save):
        self.left = Left()
        self.fn = Fn(self.left, save, self)
        self.self = self
        self.save = save
        self.add = Add()
        self.i = self.save.index
        print("right index ls = ", self.save.index)
        self.delBtn = ToggleButton(text='DEL', background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1), on_press=self.fn.get_state)

    def subm(self, instance):
        for i in self.fn.save.ogls[self.fn.save.index]:
            if i.name == self.add.name.text:
                self.add.name.text = "name taken"
                return
        print("subm index ls = ", self.i)
        self.save.save(self.add.name.text, self.add.desc.text, False)
        self.left.layout.add_widget(Button(text=self.add.name.text, on_release=self.fn.ed_fn, size_hint_y=None, height=65, background_color=(0.85, 0.88, 0.97, 1), color=(0.85, 0.8, 0.9, 1)))

        # TODO
        self.left.layout.remove_widget(self.left.b1)
        self.left.layout.remove_widget(self.left.b2)
        self.left.layout.add_widget(self.left.b1)
        self.left.layout.add_widget(self.left.b2)
        ###

        self.add.popup.dismiss()
        self.add.subm()

    def add_btn(self, btn):
        self.buttons.add_widget(btn, index=2)


    # buttons.add_widget(Redo.layout)
