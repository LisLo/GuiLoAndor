import os
import sys
from kivy.app import App
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput


class TestApp(App):
    pass


class StartApp(GetInput, App):
    def __init__(self):
        super().__init__(__file__)


    def build(self):
        pass


if __name__ == "__main__":
    TestApp().run()
