from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from get_index import get_index_of_task

import todo
from son import Files

son = Files()


def log(mssg):
    pass


class Edit:

    def __init__(self, save):
        self.save = save

    counter_of_tasks = 0
   # todos = save.ls

    def get_btn(self, instance):
        self.instance = instance

    def ed_chc(self, instance):
        task_index = int(instance.id)
        son.comp(int(instance.id), self.save.index)

        if not self.save.ls[task_index].completed:
            instance.background_color = (0.37, 0.76, 0.24, 1)
            self.instance.background_color = (0.37, 0.76, 0.24, 1)
            self.save.ls[task_index].completed = True

        else:
            instance.background_color = 0.60, 0.68, 0.92, 1
            self.instance.background_color = 0.85, 0.88, 0.97, 1
            self.save.ls[task_index].completed = False

    def ed_save(self, instance, name, desc, task_index):
        todo.print_all(self.save.ls[task_index])
        self.save.update(name, desc, task_index)
        # self.save.ls[task_index].name = name
        # self.save.ls[task_index].desc = desc
        # instance.text = name
        todo.print_all(self.save.ls[task_index])

    def ed_fn(self, instance):

        task_index = get_index_of_task(instance.text, self.save.ls)
        log(task_index)
        log(len(self.save.ls))

        def btnsave(btn):
            self.ed_save(instance, ed_name.text, ed_desc.text, task_index)

        ed_main = BoxLayout(orientation='horizontal')
        ed_left = BoxLayout(orientation='vertical', size_hint_x=3)
        ed_right = BoxLayout(orientation='vertical')

        ed_name = Label(text=instance.text)
        ed_desc = TextInput(text=self.save.ls[task_index].desc, size_hint_y=3)
#        ed_check = Button(text='FINISHED', id=str(task_index), on_release=self.ed_chc, background_color=(0.60, 0.68, 0.92, 1))
        s = str(task_index)
        ed_check = Button(text='DONE', on_release=self.ed_chc, background_color=(0.60, 0.68, 0.92, 1))
        ed_check.id = s
        ed_save = Button(text='SAVE', on_release=btnsave, background_color=(0.60, 0.68, 0.92, 1))

        if self.save.ls[task_index].completed:
            ed_check.background_color = (0, 1, 0, 1)

        ed_left.add_widget(ed_name)
        ed_left.add_widget(ed_desc)
        ed_right.add_widget(ed_check)
        ed_right.add_widget(ed_save)

        ed_main.add_widget(ed_left)
        ed_main.add_widget(ed_right)

        ed_pop = Popup(title='Edit', content=ed_main, size_hint=(0.7, 0.9))

        ed_pop.open()

    # left side of the app
    ls = BoxLayout(orientation='vertical')

