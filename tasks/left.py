from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.label import Label


class Left:

    def a(self, name):
        self.b.text = name

    b1 = Button(size_hint_y=None, height=100, background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))
    b2 = Button(size_hint_y=None, height=100, background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))
    b3 = Button(size_hint_y=None, height=100, background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))

    test = GridLayout(cols=1)

    b = Button(text="a", size_hint_y=None, height=100, background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1))

    test.add_widget(b)

    layout = GridLayout(cols=1, size_hint_y=None)
    layout.bind(minimum_height=layout.setter('height'))

    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    test.add_widget(root)
    test.add_widget(Label(text="PANTHER TODO LIST", height=100, color=(0.85, 0.8, 0.9, 1)))






