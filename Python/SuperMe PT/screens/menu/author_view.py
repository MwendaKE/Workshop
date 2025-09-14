from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from modules.datamanager import Book, Quote
from modules.definations import AppColor, Message, Error, Title
from modules.helpers import ContentLabelView

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"

class AuthorViewWindow(Screen):
    #bk_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AuthorViewWindow, self).__init__(**kwargs)
        
        
class AuthorContentWindow(Screen):
    def __init__(self, authorkey, **kwargs):
        super(AuthorContentWindow, self).__init__(**kwargs)
        self.authorkey = authorkey
        self.app = App.get_running_app()
         
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('authorview').ids.author_content_container.clear_widgets()
        
        query = self.authorkey
        
        if query:
            bkobj = Book(DB)
            bkauthors = bkobj.load_book_authors()
            
            if query in bkauthors:
                occ, cnt, desc = bkobj.get_author_details(query)
            
            else:
                qtobj = Quote(DB)
                occ, cnt, desc = qtobj.get_author_details(query)
             
            self.app.root.ids.manager.get_screen('authorview').ids.author_titlelabel.text = f"[b]{query}[/b], [i][color=#26DDC7]{occ}[/color], [color=#83AE74]{cnt}[/color][/i]"
            
            desc_list = [item for item in desc.split("\n\n")]
            
            for paragraph in desc_list:
                self.app.root.ids.manager.get_screen('authorview').ids.author_content_container.add_widget(ContentLabelView(text=paragraph))
                
            self.app.root.ids.manager.current = "authorview"
        
        else:
            self.app.root.ids.manager.get_screen('authorview').ids.author_content_container.add_widget(ContentLabelView(text=Message.no_author_content))
                