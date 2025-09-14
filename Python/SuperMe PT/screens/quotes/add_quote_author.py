from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from modules.helpers import show_error
from modules.datamanager import Quote
from modules.definations import Error, Text, Title

from kivy.properties import ObjectProperty

DB = "SuperMe.db"

class AddQuoteAuthorWindow(Screen):
    author_name = ObjectProperty(None)
    occupation = ObjectProperty(None)
    country = ObjectProperty(None)
    description = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddQuoteAuthorWindow, self).__init__(**kwargs)
        self.authorname = Text.select_author
        
    def add_author(self):
        if (self.author_name.text == "" or self.author_name.text.isspace() or
            self.occupation.text == "" or self.occupation.text.isspace() or
            self.country.text == Text.select_country or
            self.description.text == "" or self.description.text.isspace()
            ):
            show_error(Title.add_quote_author, Error.required)
        
        else:
            self.authorname = self.author_name.text.title()
            
            quoteobj = Quote(DB)
            
            allauthors = quoteobj.load_authors_lower()
            
            if self.authorname.lower() in allauthors:
                show_error(Title.add_quote_author, Error.author_exists)
                
            else:
                quoteobj.add_quote_author(self.authorname, self.occupation.text, self.country.text, self.description.text)
            
            self.author_name.text = ""
            self.occupation.text = ""
            self.country.text = Text.select_country
            self.description.text = ""
            
            self.refresh_addquote_window()
            
    def refresh_addquote_window(self):
        qo = Quote(DB)
        
        self.manager.get_screen('addquote').ids.quote_author_spinner.values = qo.load_authors()
        self.manager.get_screen('addquote').ids.quote_author_spinner.text = self.authorname
        
        self.manager.current = "addquote"
    