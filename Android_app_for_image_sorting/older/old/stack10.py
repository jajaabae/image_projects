#qpy:kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import os

import remove_pyc
from Imglayout import Imglayout
from get_imageExtentions import get_imageExtentions
from fileNameContainer import fileNameContainer


class MainTApp(App):
    fnc = fileNameContainer()
    im=Image(source=fnc.getFileName())
    
    def build(self):
        root = BoxLayout(orientation='vertical')
        c = Imglayout()
        root.add_widget(c)
        #self.im.keep_ratio= False
        self.im.keep_ratio= True
        #self.im.allow_stretch = False
        self.im.allow_stretch = True
        c.add_widget(self.im)
        
        cat=Button(text="A",size_hint=(0,.07))
        cat.bind(on_press=self.tagButtonClick)
        root.add_widget(cat);

        btnList = ['B', 'C', 'D']
        for b in btnList:
            cat=Button(text=b,size_hint=(0,.07))
            cat.bind(on_press=self.tagButtonClick)
            root.add_widget(cat);
        
        cat=Button(text="Next",size_hint=(1,.07))
        cat.bind(on_press=self.callback)
        ###c.add_widget(self.im)
        root.add_widget(cat);
        return root

    def callback(self, value):
        fnc2 = fileNameContainer()
        self.im.source = fnc2.getFileName()
        
    def tagButtonClick(instance, value):
        print value.text

        
        
if __name__ == '__main__':
    MainTApp().run()



    
    
    
    
    
