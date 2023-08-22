from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from lists.lists_mid import Mid
from son import Files

son = Files()
mid = Mid()


class List_Add:

    mid = mid

    def get_btns(self, rm, al):
        self.rm = rm
        self.al = al

    def give_state(self, state):
        mid.get_state(state.state)
        if not state.state == "normal":
            self.al.state = "normal"
            mid.get_alarm_state(self.al.state)

    def give_alarm_state(self, state):
        mid.get_alarm_state(state.state)
        if not state.state == "normal":
            self.rm.state = "normal"
            mid.get_state(self.rm.state)

    mid.idk()

    layout = mid.layout

    add = BoxLayout(orientation='vertical')
    inpoot = BoxLayout(orientation='vertical')
    # right = BoxLayout(orientation='vertical')
    mk_reminder = BoxLayout(orientation='vertical')
    mk_checkboxes = GridLayout(cols=7)

    label = Label(text="List name", height=70, size_hint_y=None, color=(0.85, 0.8, 0.9, 1))
    list_name = TextInput()
    inpoot.add_widget(label)
    inpoot.add_widget(list_name)

    mk_label1 = Label(text="day", color=(0.85, 0.8, 0.9, 1))
    mk_label2 = Label(text="hour", color=(0.85, 0.8, 0.9, 1))

    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    checkbox_list = []
    for i in days:
        a = CheckBox()
        mk_checkboxes.add_widget(a)
        checkbox_list.append(a)

    mk_checkboxes.add_widget(Label(text="mon"))
    mk_checkboxes.add_widget(Label(text="tue"))
    mk_checkboxes.add_widget(Label(text="wed"))
    mk_checkboxes.add_widget(Label(text="thu"))
    mk_checkboxes.add_widget(Label(text="fri"))
    mk_checkboxes.add_widget(Label(text="sat"))
    mk_checkboxes.add_widget(Label(text="sun"))

    mk_hour = TextInput(text="00:00")

    mk_reminder.add_widget(mk_label1)
    mk_reminder.add_widget(mk_checkboxes)
    mk_reminder.add_widget(mk_label2)
    mk_reminder.add_widget(mk_hour)

    add.add_widget(inpoot)
    add.add_widget(mk_reminder)

    pop = Popup(title='Test popup', content=add, size_hint=(0.5, 0.9))

    def subm_btn(self):
        def subm(instance):

            for i in son.load_ls():
                if self.list_name.text == i.name:
                    self.list_name.text = "Pick a different name"
                    return

            num_of_chars = 0
            for i in self.mk_hour.text:
                num_of_chars = num_of_chars + 1
                if num_of_chars == 3:
                    if i != ":":
                        self.mk_hour.text = "please enter a time in this format '??:??'"
                        return
                elif i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0":
                    self.mk_hour.text = "please enter a time in this format '??:??'"
                    return
                elif num_of_chars == 6:
                    self.mk_hour.text = "please enter a time in this format '??:??'"
                    return

            reimnder = ""
            a = -1

            for i in self.checkbox_list:
                a += 1
                if i.state != "normal":
                    reimnder = reimnder + self.days[a] + "+"

            reimnder = reimnder + "-" + self.mk_hour.text

            mid.add(self.layout, self.list_name.text, reimnder)

            self.list_name.text = ""
            for i in self.checkbox_list:
                i.state = "normal"
            self.mk_hour.text = ""

            self.pop.dismiss()

        sbm_btn = Button(text="Add list", height=100, size_hint_y=None, on_release=subm, color=(0.85, 0.8, 0.9, 1))
        self.add.add_widget(sbm_btn)

    def open(self, instance):
        self.pop.open()


