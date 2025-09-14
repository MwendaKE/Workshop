from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Quote
from modules.helpers import show_error
from modules.definations import Error, Text, Title

DB = "SuperMe.db"


class AddQuoteWindow(Screen):
    author = ObjectProperty()
    category = ObjectProperty()
    quote = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(AddQuoteWindow, self).__init__(**kwargs)
        self.title = Title.add_quote
        
    def add_quote(self):
        if (self.author.text == Text.select_author or 
            self.category.text == Text.select_category or 
            self.quote.text == "" or self.quote.text.isspace()
            ):
            show_error(Title.add_quote, Error.required)
                       
        else:
            import re
            
            qo = Quote(DB)
            
            library = qo.load_quotes()
            quote = (self.author.text, self.quote.text)
            
            if (quote in library) or (re.search(self.quote.text, str([quote[1] for quote in library]), re.I)):
                show_error(Title.add_quote, Error.quote_exists)
                
            else:
                qo.add_quote(self.author.text, self.quote.text, self.category.text)
            
            self.author.text = Text.select_author
            self.category.text = Text.select_category
            self.quote.text = ""
     
            self.manager.current = "quotes"
                

class QuotesAuthorSpinner(Spinner):
    def __init__(self, **kwargs):
        super(QuotesAuthorSpinner, self).__init__(**kwargs)
        self.add_spinner_items()
        
    def add_spinner_items(self):
        authorobj = Quote(DB)
        self.values = authorobj.load_authors()
        
