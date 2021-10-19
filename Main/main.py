import os
import sys
import kivy 

from kivy.app import App
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput


class TestApp(App):
    pass

'''
class StartApp(GetInput, App):
    def __init__(self):
        super().__init__(__file__)

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        # print(self.A1)
        return GUI
'''

if __name__ == "__main__":
    #StartApp().run()
    TestApp().run()
