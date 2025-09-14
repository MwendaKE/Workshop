from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from modules.helpers import show_error
from modules.datamanager import Article
from modules.definations import Text, Title, Error

from kivy.properties import ObjectProperty

DB = "SuperMe.db"


class AddArticleWriterWindow(Screen):
    writer_name = ObjectProperty(None)
    country = ObjectProperty(None)
    description = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddArticleWriterWindow, self).__init__(**kwargs)
        self.writername = Text.select_writer
    
    def add_article_writer(self):
        if (self.writer_name.text == "" or self.writer_name.text.isspace() or
            self.country.text == Text.select_country or
            self.description.text == "" or self.description.text.isspace()
            ):
            show_error(Title.add_article_writer, Error.required)
        
        else:
            self.writername = self.writer_name.text.title()
            
            artobj = Article(DB)
            
            allwriters = artobj.load_writers_lower()
            
            if self.writername.lower() in allwriters:
                show_error(Title.add_article_writer, Error.writer_exists)
                
            else:
                artobj.add_article_writer(self.writername, self.country.text, self.description.text)
            
                self.writer_name.text = ""
                self.country.text = Text.select_country
                self.description.text = ""
            
            self.refresh_addwriter_window()
            
    def refresh_addwriter_window(self):
        ao = Article(DB)
        
        self.manager.get_screen('addarticle').ids.article_writer_spinner.values = ao.load_writers()
        self.manager.get_screen('addarticle').ids.article_writer_spinner.text = self.writername
        
        self.manager.current = "addarticle"
    
    
class CountrySpinner(Spinner):
    def __init__(self, **kwargs):
        super(CountrySpinner, self).__init__(**kwargs)
        self.add_countries()
        
    def add_countries(self):
        countries_file = "./assets/others/countries.txt"
        
        with open(countries_file) as f:
            self.values = [country.strip() for country in f.readlines()]
            