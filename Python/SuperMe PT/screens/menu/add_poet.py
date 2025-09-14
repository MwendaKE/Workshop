from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from modules.helpers import show_error
from modules.datamanager import Poem
from modules.definations import Error, Text, Title

from kivy.properties import ObjectProperty

DB = "SuperMe.db"

class AddPoetWindow(Screen):
    author_name = ObjectProperty(None)
    country = ObjectProperty(None)
    description = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddPoetWindow, self).__init__(**kwargs)
        self.authorname = Text.select_author
        
    def add_poet(self):
        if (self.author_name.text == "" or self.author_name.text.isspace() or
            self.country.text == Text.select_country or
            self.description.text == "" or self.description.text.isspace()
            ):
            show_error(Title.add_poem_author, Error.required)
        
        else:
            self.authorname = self.author_name.text.title()
            
            pobj = Poem(DB)
            
            allpoets = pobj.load_poets_lower()
            
            if self.authorname.lower() in allpoets:
                show_error(Title.add_poem_author, Error.author_exists)
                
            else:
                pobj.add_poet(self.authorname, self.country.text, self.description.text)
            
            self.author_name.text = ""
            self.country.text = Text.select_country
            self.description.text = ""
            
            self.refresh_poets_spinner()
            
    def refresh_poets_spinner(self):
        qo = Poem(DB)
        
        self.manager.get_screen('addpoem').ids.poem_author_spinner.values = qo.load_poets()
        
        self.manager.current = "poets"
        
        return
    