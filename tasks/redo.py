from todo import Todo
from tasks.edit import Edit
from get_index import get_index_of_task

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

todo = Todo


def ed_fn(instance, state, edit, left, save):
    if state == "normal":
        edit.ed_fn(instance)
    else:
        left.layout.remove_widget(instance)
        index = get_index_of_task(instance.text, save.ls)

        objc = save.ls[index]

        save.save(objc.name, objc.desc, objc.completed)
        save.dele(index)


class Redo:

    # deleted is storing the last deleted item
    deleted = Todo

    def __init__(self, left, save, state, right):
        def call_undo(instance):
            self.undo()

        self.layout = BoxLayout(orientation='vertical')
        self.btn_redo = Button(text='No item has been deleted', background_color=(0.60, 0.68, 0.92, 1), color=(0.85, 0.8, 0.9, 1), on_release=call_undo)
        self.layout.remove_widget(self.btn_redo)
        self.layout.add_widget(self.btn_redo)
        self.label_name = Label(color=(0.85, 0.8, 0.9, 1))
        self.label_desc = Label(color=(0.85, 0.8, 0.9, 1))

        self.layout.add_widget(self.label_name)
        self.layout.add_widget(self.label_desc)

        self.left = left
        self.save = save
        self.state = state
        self.right = right
        self.edit = Edit(save)
        self.first = True

    def get_state(self, state):
        self.state = state

    def undo(self):
        def a(instance):
            ed_fn(instance, self.state, self.edit, self.left, self.save)

        self.left.layout.add_widget(Button(text=self.deleted.name, on_release=a, height=65, size_hint_y=None, color=(0.85, 0.8, 0.9, 1), background_color=(0.85, 0.88, 0.97, 1)))
        self.save.save(self.deleted.name, self.deleted.desc, self.deleted.completed)
        # TODO
        self.left.layout.remove_widget(self.left.b1)
        self.left.layout.remove_widget(self.left.b2)
        self.left.layout.add_widget(self.left.b1)
        self.left.layout.add_widget(self.left.b2)


    def sv(self, objc):

        self.deleted.name = objc.name
        self.deleted.desc = objc.desc
        self.deleted.completed = objc.completed

        self.label_name.text = objc.name
        self.label_desc.text = objc.desc

        self.btn_redo.text = "Restore last deleted task"

        if self.first:
            self.right.buttons.add_widget(self.layout)
            self.first = False



