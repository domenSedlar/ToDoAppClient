from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

from lists.list_add import List_Add

add = List_Add()
add.subm_btn()


class Lists:

    btn_rm = ToggleButton(text="Remove", size_hint_y=None, height=100, on_release=add.give_state, color=(0.85, 0.8, 0.9, 1), background_color=(0.60, 0.68, 0.92, 1))
    btn_add = Button(text="New", size_hint_y=None, height=100, on_release=add.open, color=(0.85, 0.8, 0.9, 1), background_color=(0.60, 0.68, 0.92, 1))
    btn_time = ToggleButton(text="Alarm", size_hint_y=None, height=100, on_release=add.give_alarm_state, color=(0.85, 0.8, 0.9, 1), background_color=(0.60, 0.68, 0.92, 1))
    btn_x = Button(text="X", size_hint_y=None, height=100, on_release=add.give_state, color=(0.85, 0.8, 0.9, 1), background_color=(0.9, 0.25, 0.41, 1))

    add.get_btns(btn_rm, btn_time)

    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    btns = GridLayout(cols=5, size_hint_y=None)
    btns.bind(minimum_height=btns.setter('height'))

    btns.add_widget(btn_add)
    btns.add_widget(btn_rm)
    btns.add_widget(add.mid.redo_btn)
    btns.add_widget(btn_time)
    btns.add_widget(btn_x)

    root.add_widget(add.layout)

    all = GridLayout(cols=1)
    all.add_widget(btns)
    all.add_widget(root)