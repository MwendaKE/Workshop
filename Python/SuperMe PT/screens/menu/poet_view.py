from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from modules.datamanager import Poem
from modules.definations import AppColor, Message, Error, Title
from modules.helpers import ContentLabelView

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"

class PoetViewWindow(Screen):
    def __init__(self, **kwargs):
        super(PoetViewWindow, self).__init__(**kwargs)
        
        
class PoetContentWindow(Screen):
    def __init__(self, poetkey, **kwargs):
        super(PoetContentWindow, self).__init__(**kwargs)
        self.poetkey = poetkey
        self.app = App.get_running_app()
         
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('poetview').ids.poet_content_container.clear_widgets()
                
        query =  self.poetkey
        
        if query:
            ptobj = Poem(DB)
            
            cnt, desc = ptobj.get_poet_details(query)
            
            self.app.root.ids.manager.get_screen('poetview').ids.poet_titlelabel.text = f"[b]{query}[/b], [i][color=#83AE74]{cnt}[/color][/i]"
            
            desc_list = [item for item in desc.split("\n\n")]
            
            for paragraph in desc_list:
                self.app.root.ids.manager.get_screen('poetview').ids.poet_content_container.add_widget(ContentLabelView(text=paragraph))
                
            self.app.root.ids.manager.current = "poetview"
        
        else:
            self.app.root.ids.manager.get_screen('poetview').ids.poet_content_container.add_widget(ContentLabelView(text=Message.no_poet_content))
                