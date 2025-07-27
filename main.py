from kivy.config import Config
Config.set("kivy", "default_font", ["MyFont", "./font/simkai.ttf"])

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from libs.input_psd import Input_psd

Window.size = (420, 840)

class Route (ScreenManager) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init()

    def init(self) :
        self.add_widget(Input_psd (name="Input_psd" ))

        self.current = "Input_psd"

# 重定义App的build方法
def app_build() :
    route = Route()
    return route

test = App()
test.build = app_build
test.run()