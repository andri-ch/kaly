#!/usr/bin/python
'''
Game for kaly.at
================
'''

import kivy
kivy.require("1.7.2")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class FirstScreen(Widget):
    pass


class KalyApp(App):
    def build(self):
        return FirstScreen()

if __name__ == '__main__':
    KalyApp().run()
