from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from modules.datamanager import Music
from modules.definations import AppColor, Message, Error, Title
from modules.helpers import ContentLabelView

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"

class ArtistViewWindow(Screen):
    def __init__(self, **kwargs):
        super(ArtistViewWindow, self).__init__(**kwargs)
        
        
class ArtistContentWindow(Screen):
    def __init__(self, artistkey, **kwargs):
        super(ArtistContentWindow, self).__init__(**kwargs)
        self.artistkey = artistkey
        self.app = App.get_running_app()
         
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('artistview').ids.artist_content_container.clear_widgets()
                
        query =  self.artistkey
        
        if query:
            msobj = Music(DB)
            
            cnt, desc = msobj.get_artist_details(query)
            
            self.app.root.ids.manager.get_screen('artistview').ids.artist_titlelabel.text = f"[b]{query}[/b], [i][color=#83AE74]{cnt}[/color][/i]"
            
            desc_list = [item for item in desc.split("\n\n")]
            
            for paragraph in desc_list:
                self.app.root.ids.manager.get_screen('artistview').ids.artist_content_container.add_widget(ContentLabelView(text=paragraph))
                
            self.app.root.ids.manager.current = "artistview"
        
        else:
            self.app.root.ids.manager.get_screen('artistview').ids.artist_content_container.add_widget(ContentLabelView(text=Message.no_artist_content))
                