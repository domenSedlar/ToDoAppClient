from kivy.app import App
from kivy.uix.screenmanager import Screen

import json
from scrn_mangr import Scrn_manger
from lists.lists import Lists


def stop(instance):
    a = open("abc.txt", "w")
    json.dump([[]], a)
    App.get_running_app().stop()
    a.close()


class Panther(App):
    ls = Lists()
    ls.btn_x.bind(on_release=stop)
    sm = Scrn_manger()
    lists = Screen(name="lists")
    lists.add_widget(ls.all)
    sm.sm.add_widget(lists)

    def build(self):
        return Scrn_manger.sm


if __name__ == '__main__':
    Panther().run()

