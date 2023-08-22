from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class Add:

    def subm(self):
        self.name.text = ""
        self.desc.text = ""

    # popup for adding tasks
    add = BoxLayout(orientation='vertical')
    name = TextInput(multiline=False, hint_text="NAME")
    desc = TextInput(size_hint_y=2, hint_text="DESCRIPTION")

    popup = Popup(title='Add', content=add, size_hint=(0.7, 0.9))

    def o(self, instance):
        self.popup.open()


