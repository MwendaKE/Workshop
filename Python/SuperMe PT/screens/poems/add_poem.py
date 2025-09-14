from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Poem, Quote
from modules.helpers import show_error
from modules.definations import Error, Text, Title

from collections import deque

DB = "SuperMe.db"


class AddPoemWindow(Screen):
    title = ObjectProperty(None)
    author = ObjectProperty(None)
    body = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddPoemWindow, self).__init__(**kwargs)
        
    def add_poem(self):
        if (self.author.text == Text.select_author or 
            self.title.text == "" or self.title.text.isspace() or 
            self.body.text == "" or self.body.text.isspace()
            ):
            show_error(Title.add_poem, Error.required)
               
        else:
            import re
            
            poemobj = Poem(DB)
            
            poemlibrary = poemobj.load_poems()
            poem = (self.title.text, self.author.text)
            
            if (poem in poemlibrary) or (re.search(self.title.text, str([title[0] for title in poemlibrary]), re.I)):
                show_error(Title.add_poem, Error.poem_exists)
            
            else:
                poemobj.add_poem(self.title.text.title(), self.body.text, self.author.text)
            
            self.author.text = Text.select_author
            self.title.text = ""
            self.body.text = ""
                
            self.manager.current = "poems"
        
        
class PoemAuthorSpinner(Spinner):
    def __init__(self, **kwargs):
        super(PoemAuthorSpinner, self).__init__(**kwargs)
        self.add_poets()
        
    def add_poets(self):
        pobj = Poem(DB)
        self.values = pobj.load_poets()
        