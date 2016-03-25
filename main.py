# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class FirstScreen(BoxLayout):
    pass


class SecondScreen(BoxLayout):
    pass


class ResultScreen(BoxLayout):
    pass


class HackApp(App):
    def build(self):
        return FirstScreen()
        # return SecondScreen()


if __name__ == '__main__':
    HackApp().run()
