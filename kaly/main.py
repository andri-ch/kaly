#!/usr/bin/python
'''
Game for kaly.at
================
'''

import kivy
kivy.require("1.7.2")

from kivy.app import App
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.core.image import ImageData
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty



class KalyBird(Image):
    '''Represents the image of a bird.'''
    #pass
    def __init__(self, *args, **kwargs):
        super(KalyBird, self).__init__(*args, **kwargs)
        #Logger.debug("WormHole: %s" % dir(self))
        #Logger.debug("WormHole: parent is: %s " % self.parent)
        Logger.debug("KalyBird: pos: %s, %s " % self.to_parent(*self.pos))
        #Logger.debug("WormHole: allow_stretch: %s" % self.allow_stretch)
        #Logger.debug("WormHole: keep_ratio: %s " % self.keep_ratio)
        #Logger.debug("WormHole: id: %s " % self.id)
        #Logger.debug("WormHole: texture: %s " % self.texture)
        #Logger.debug("WormHole: norm_image_size: %s, %s " % self.norm_image_size)

    def get_window(self, win):
        self.size = (win.width / 26, win.height / 23)

    def on_touch_down(self, touch):
        self.x = touch.x
        self.y = touch.y

    def on_touch_move(self, touch):
        self.x = touch.x
        self.y = touch.y


class FirstScreen(FloatLayout):
    #background_image = ObjectProperty(Image(source='media/kaly-background2.png'))
    #bird = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(FirstScreen, self).__init__(*args, **kwargs)
        #texture = CoreImage('media/kaly-background2.png').texture
        #Logger.debug("FirstScreen: dir(texture): %s" % dir(texture))
        #Logger.debug("FirstScreen: size: %s, %s" % texture.size)
        #Logger.debug("FirstScreen: uvsize: %s, %s" % texture.uvsize)
        # ImageData(width, height, fmt, data, source=None, flip_vertical=True)
        #with self.canvas:
        #    Rectangle(texture=texture, pos=self.pos, size=self.size)
        #self.size = texture.width, texture.height
            #texture = Texture.create(size=(2600, 1482), colorfmt='rgba')
            # TextureRegion.create(size=(2600, ...) for non -power of two
            # (NPOT) textures
        #self.win = self.get_parent_window()
        #Logger.debug("Application: widget width, height is: %s, %s " % (self.width, self.height))
        #Logger.debug("Application: x, y is: %s, %s " % (self.x, self.y))
        #Logger.debug("Application: pos: %s" % self.pos)
        #Logger.debug("Application: parent is: %s " % self.parent)
        ### DEBUG ###
        #l = dir(self)
        #for elem in l:
        #    #print('%s is a %s' % (elem, type(elem)))
        #    print('%s is a %s' % (elem, type(eval('self.%s' % elem))))
        #Logger.debug("Application: %s" % dir(self))
        #Logger.debug("Application: allow_stretch: %s" % self.allow_stretch)
        #Logger.debug("Application: keep_ratio: %s " % self.keep_ratio)
        #Logger.debug("Application: id: %s " % self.id)
        #Logger.debug("Application: texture: %s " % self.texture)
        #Logger.debug("Application: norm_image_size: %s " % self.norm_image_size)
        #Logger.debug("Application: keep_ratio: %s " % self.keep_ratio)



class KalyApp(App):
    def build(self):
        first_sc = FirstScreen()
        #hole_1.get_window(first_sc.win)
        #first_sc.add_widget(hole_1)
        #layout = FloatLayout()
        #layout.add_widget(first_sc)
        return first_sc
        #return layout

if __name__ == '__main__':
    KalyApp().run()
