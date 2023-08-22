from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from lists.chgn_alarm import Chgn_alarm
from save_lists import Save_Lists
from scrn_mangr import Scrn_manger
from son import Files

son = Files()
sm = Scrn_manger()
sv_ls = Save_Lists()
c_a = Chgn_alarm()


def pressed(instance, state_del, layout, state_al):
    if not state_del == "normal":
        layout.remove_widget(instance)
        son.del_ls(instance.text)
    elif not state_al == "normal":
        c_a.open(instance.text)
    else:
        sm.to_tasks(instance.text)
        sm.name = instance.text

class Mid:
    state_del = "normal"
    state_alarm = "normal"
    redo_btn = Button(text="Restore", color=(0.85, 0.8, 0.9, 1), background_color=(0.60, 0.68, 0.92, 1))

    def get_state(self, state):
        self.state_del = state

    def get_alarm_state(self, state):
        self.state_alarm = state

    lists = son.load_ls()

    layout = GridLayout(cols=1, size_hint_y=None)

    layout.bind(minimum_height=layout.setter('height'))

    def idk(self):
        def prssd(instance):
            pressed(instance, self.state_del, self.layout, self.state_alarm)

        for i in self.lists:
            btn = Button(text=i.name, size_hint_y=None, height=80, on_release=prssd, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1))
            self.layout.add_widget(btn)
        self.layout.add_widget(self.b1)

    def add(self, layout, name, reminder):
        def prssd(instance):
            pressed(instance, self.state_del, self.layout, self.state_alarm)
        sv_ls.save(name, reminder)
        btn = Button(text=name, size_hint_y=None, height=80, on_release=prssd, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1))
        layout.add_widget(btn)

        self.layout.remove_widget(self.b1)
        self.layout.add_widget(self.b1)

    def restore(self):
        def prssd(instance):
            pressed(instance, self.state_del, self.layout, self.state_alarm)
        a = son.chec()
        if a != "":
            sv_ls.restore(a)
            self.layout.add_widget(Button(text=a.name, size_hint_y=None, height=80, on_release=prssd, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1)))

            self.layout.remove_widget(self.b1)
            self.layout.add_widget(self.b1)

    def __init__(self):
        self.redo_btn.bind(on_release=lambda i: self.restore())

        self.b1 = Button(size_hint_y=None, height=80, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1))
        self.b2 = Button(size_hint_y=None, height=80, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1))
        self.b3 = Button(size_hint_y=None, height=80, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1))
