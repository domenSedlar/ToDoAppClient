from son import Files
from todo import Todo
import todo

son = Files()


def log(mssg):
    pass
    # print(mssg)

def l(mssg):
    print(mssg)

class Save:
    name = ""

    son = son

    def __init__(self, name):
        self.list_of_lists = son.load_ls()
        self.ogls = son.load_tsk()

        self.name = name
        b = 0
        a = ""
        ls_names = son.load_ls()

        while a != name:
            a = ls_names[b].name
            b = b + 1

        self.index = b - 1
        l(self.index)
        self.ls = self.ogls[self.index]

    def save(self, name, desc, comp, i=0):
        log(self.ogls)
        l(self.index)
        self.ogls[self.index].append(Todo(name, desc, comp))
        log(self.ogls)
        son.save_tsk(self.ogls, "ad", self.list_of_lists[self.index].name, name, desc)

    def dele(self, indx):
        nm = self.ogls[self.index][indx].name
        del self.ogls[self.index][indx]
        son.save_tsk(self.ogls, "rm", self.list_of_lists[self.index].name, nm)

    def update(self, name, desc, tsk_index):
        tsk_index = tsk_index
        todo.print_all(self.ogls[self.index][tsk_index])
        # self.ogls[self.index][tsk_index].name = name
        self.ogls[self.index][tsk_index].desc = desc
        todo.print_all(self.ogls[self.index][tsk_index])
        l("update ls index " + str(self.index))
        son.save_tsk(self.ogls, "cd", self.list_of_lists[self.index].name, self.ogls[self.index][tsk_index].name, desc)


