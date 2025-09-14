from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineIconListItem

from modules.datamanager import Poem
from modules.definations import Message

from collections import deque

DB = "SuperMe.db"
 
 
class TwoLinePoemView(TwoLineIconListItem):
    def __init__(self, **kwargs):
        super(TwoLinePoemView, self).__init__(**kwargs)
        
    def on_release(self):
    	from screens.poems.poem_view import PoemContentView
    	
    	if not "Click the '+ Add' below to add." in self.text:
    		PoemContentView(self.text)
	
                              
class PoemWindow(Screen):
    def __init__(self, **kwargs):
        super(PoemWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self):
        poemobj = Poem(DB)
        poems = poemobj.load_poems()
        
        if poems:
            poem_count = poemobj.get_poems_count()
            
            self.data = deque()
            
            for title, author in poems:
                self.data.append((f"[b]{title}[/b]", f"[i]{author}[/i]"))
                
            self.ids.poem_count.text = str(poem_count)
            
            for title, author in self.data:
            	self.ids.poems_container.add_widget(TwoLinePoemView(text=title, secondary_text=author))
         
        else:
            self.ids.poems_container.add_widget(TwoLinePoemView(text=f"{Message.no_poems}", secondary_text=""))
        
        return
            
    def on_pre_leave(self, *args):
        self.ids.poems_container.clear_widgets()
        
        return       