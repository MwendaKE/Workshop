from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem

from modules.datamanager import Poem
from modules.definations import Message

DB = "SuperMe.db"


class OneLinePoetView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLinePoetView, self).__init__(**kwargs)
       
    def on_release(self):
        from screens.menu.poet_view import PoetContentWindow
            
        if not Message.no_poets in self.text:
            PoetContentWindow(self.text)
       
        
class PoetsWindow(Screen):
    def __init__(self, **kwargs):
        super(PoetsWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.poets_container.clear_widgets()
        
        mo = Poem(DB)
        poets = mo.load_poets()
        
        self.ids.poets_count.text = str(len(poets))
        
        for poet in poets:
            self.ids.poets_container.add_widget(OneLinePoetView(text=poet))
            
        return