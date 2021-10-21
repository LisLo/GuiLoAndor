import os
import sys
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput
picture_path = os.path.join(root_path, f'Pictures{os.sep}')
print(picture_path)


class Games(PageLayout):
    andor1 = os.path.join(picture_path, "Andor-Trilogie-1.jpg")
    andor2 = os.path.join(picture_path, "Andor-Trilogie-2.jpg")
    andor3 = os.path.join(picture_path, "Andor-Trilogie-3.jpg")
    bonus = os.path.join(picture_path, "Schwarze_Kogge.png")


class TestApp(App):
    pass


class StartApp(GetInput, App):
    def __init__(self):
        super().__init__(__file__)

    def build(self):
        pass


if __name__ == "__main__":
    TestApp().run()
