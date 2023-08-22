from kivy.uix.screenmanager import ScreenManager, Screen
from tasks.tsks import A


class Scrn_manger:
    sm = ScreenManager()
    name = ""
    sc = Screen(name="tasks")

    # main.right.dodBtn.bind(on_press=main.dod)

    def to_lists(self, sc, a):
        self.sm.current = "lists"
        self.sm.remove_widget(sc)
        a.layout.clear_widgets()
        sc.clear_widgets()
        a.left.layout.clear_widgets()
        a.right.buttons.clear_widgets()
        a.right.add.add.clear_widgets()

    a = True

    def to_tasks(self, name):
        a = A(name)

        if self.a:
            self.a = False
            # a.right.delBtn.bind(on_release=a.right.fn.get_state)

        ly = a.a()

        a.bcbtn.bind(on_release=lambda i: self.to_lists(self.sc, a))
        self.sc.add_widget(ly)
        self.sm.add_widget(self.sc)
        self.sm.current = "tasks"





