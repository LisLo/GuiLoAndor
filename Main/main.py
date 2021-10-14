import os
import sys

from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput

Builder.load_file("start.kv")


class Games(Screen):
    btn1 = ObjectProperty()
    btn2 = ObjectProperty()
    btn3 = ObjectProperty()


ms = ScreenManager()
ms.add_widget(Games(name="games"))

class StartApp(GetInput, App):
    def __init__(self):
        super().__init__(__file__)

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        print(self.A1)
        return ms


if __name__ == "__main__":
    StartApp().run()
