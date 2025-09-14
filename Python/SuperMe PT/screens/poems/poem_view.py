from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

from kivy.uix.screenmanager import Screen

from modules.datamanager import Poem
from modules.helpers import ContentLabelView, DeletePoemDialog, show_error, show_message, show_info
from modules.definations import Message, Error, Title

from kivy.clock import Clock

import re


DB = "SuperMe.db"


class PoemViewWindow(Screen):
    pm_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(PoemViewWindow, self).__init__(**kwargs)
        self.poem_patt = "\[b\](.+)\[\/b\] by \[b\](.+)\[\/b\]"
        
        Clock.schedule_once(self.edit_poem, 0.1)
      
    def edit_poem(self, *args):
        pass
     
       
class PoemContentView(Screen):
    def __init__(self, pmtitle, **kwargs):
        super(PoemContentView, self).__init__(**kwargs)
        self.pmtitle = pmtitle
        self.app = App.get_running_app()
        
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('poemview').ids.poem_container.clear_widgets()
        
        pm_patt = "\[b\](.+)\[/b\]"
        
        query = re.search(pm_patt, self.pmtitle)
        
        poet = "Undefined"
        
        if query:
            pm_title = query.group(1)
            
            pmobj = Poem(DB)
            
            pm_poem, poet = pmobj.load_poem_content(pm_title)
                
            if pm_poem:
                from collections import deque
                    
                pm_content = deque()
                    
                for content in pm_poem.split("\n\n"):
                    pm_content.append(content)
                        
            else:
                pm_content = Message.no_poem_content
          
        else:
            self.pmtitle = "Undefined"
            pm_content = "[color=FF0000]This content cannot be displayed![/color]"
        
        self.app.root.ids.manager.get_screen('poemview').ids.poem_titlelabel.text = f"[b]{self.pmtitle}[/b] by [b]{poet}[/b]"
        
        if type(pm_content) == deque:
            for paragraph in pm_content:
                self.app.root.ids.manager.get_screen('poemview').ids.poem_container.add_widget(ContentLabelView(text=paragraph))
            
        else:
            self.app.root.ids.manager.get_screen('poemview').ids.poem_container.add_widget(ContentLabelView(text=pm_content))
        
        self.app.root.ids.manager.current = "poemview"
        
        return
        