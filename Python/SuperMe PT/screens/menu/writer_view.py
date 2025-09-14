from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from modules.datamanager import Article
from modules.definations import AppColor, Message, Error, Title
from modules.helpers import ContentLabelView

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"

class WriterViewWindow(Screen):
    def __init__(self, **kwargs):
        super(WriterViewWindow, self).__init__(**kwargs)
        
        
class WriterContentWindow(Screen):
    def __init__(self, writerkey, **kwargs):
        super(WriterContentWindow, self).__init__(**kwargs)
        self.writerkey = writerkey
        self.app = App.get_running_app()
         
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('writerview').ids.writer_content_container.clear_widgets()
                
        query =  self.writerkey
        
        if query:
            artobj = Article(DB)
            
            cnt, desc = artobj.get_writer_details(query)
            
            self.app.root.ids.manager.get_screen('writerview').ids.writer_titlelabel.text = f"[b]{query}[/b], [i][color=#83AE74]{cnt}[/color][/i]"
            
            desc_list = [item for item in desc.split("\n\n")]
            
            for paragraph in desc_list:
                self.app.root.ids.manager.get_screen('writerview').ids.writer_content_container.add_widget(ContentLabelView(text=paragraph))
                
            self.app.root.ids.manager.current = "writerview"
        
        else:
            self.app.root.ids.manager.get_screen('writerview').ids.writer_content_container.add_widget(ContentLabelView(text=Message.no_writer_content))
                