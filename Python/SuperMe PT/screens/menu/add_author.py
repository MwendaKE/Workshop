from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from modules.helpers import show_error
from modules.datamanager import Book
from modules.definations import Text, Title, Error

from kivy.properties import ObjectProperty

DB = "SuperMe.db"


class AddAuthorWindow(Screen):
    author_name = ObjectProperty(None)
    occupation = ObjectProperty(None)
    country = ObjectProperty(None)
    description = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddAuthorWindow, self).__init__(**kwargs)
        self.authorname = Text.select_author
    
    def add_author(self):
        if (self.author_name.text == "" or self.author_name.text.isspace() or
            self.occupation.text == "" or self.occupation.text.isspace() or 
            self.country.text == Text.select_country or
            self.description.text == "" or self.description.text.isspace()
            ):
            show_error(Title.add_author, Error.required)
        
        else:
            self.authorname = self.author_name.text.title()
            
            bookobj = Book(DB)
            
            allauthors = bookobj.load_book_authors_lower()
            
            if self.authorname.lower() in allauthors:
                show_error(Title.add_author, Error.author_exists)
                
            else:
                bookobj.add_book_author(self.authorname, self.occupation.text, self.country.text, self.description.text)
            
                self.author_name.text = ""
                self.occupation.text = ""
                self.country.text = Text.select_country
                self.description.text = ""
        
            self.refresh_authors_spinner()
            
    def refresh_authors_spinner(self):
        ao = Book(DB)
        
        self.manager.get_screen('addbook').ids.book_author_spinner.values = ao.load_book_authors()
        self.manager.get_screen('editbook').ids.book_author_spinner.values = ao.load_book_authors()
        
        self.manager.current = "authors"
          
        return
    
    
class CountrySpinner(Spinner):
    def __init__(self, **kwargs):
        super(CountrySpinner, self).__init__(**kwargs)
        self.add_countries()
        
    def add_countries(self):
        countries_file = "./assets/others/countries.txt"
        
        with open(countries_file) as f:
            self.values = [country.strip() for country in f.readlines()]
            