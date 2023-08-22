from tasks.edit import Edit
from tasks.redo import Redo
from get_index import get_index_of_task


class Fn:

    state = "normal"

    def __init__(self, left, save, right):
        self.left = left
        self.save = save
        self.right = right
        self.edit = Edit(save)
        self.r = Redo(self.left, self.save, self.state, self.right)

    def get_state(self, state):
        self.state = state.state
        self.r.get_state(self.state)

    def ed_fn(self, instance):
        if self.state == "normal":
            self.edit.get_btn(instance)
            self.edit.ed_fn(instance)

        else:
            self.left.layout.remove_widget(instance)
            index = get_index_of_task(instance.text, self.save.ls)

            objc = self.save.ls[index]
            self.r.sv(objc)
            self.save.dele(index)
