from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Article, Quote
from modules.helpers import show_error
from modules.definations import Error, Text, Title
from modules.verifier import verify_date

from collections import deque

ENTRY_ALL_ERROR = True
ENTRY_DATE_ERROR = True


DB = "SuperMe.db"


class AddArticleWindow(Screen):
    title = ObjectProperty(None)
    categ = ObjectProperty(None)
    writer = ObjectProperty(None)
    body = ObjectProperty(None)
    date_written = ObjectProperty(None)
    ref = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddArticleWindow, self).__init__(**kwargs)
        
    def add_article(self):
        if (self.title.text == "" or self.title.text.isspace() or 
            self.categ.text == Text.select_category or 
            self.writer.text == Text.select_writer or 
            self.body.text == "" or self.body.text.isspace() or
            self.date_written.text == "" or 
            self.ref.text == "" 
            ):
            show_error(Title.add_article, Error.required)
               
        else:
            if verify_date(self.date_written.text) == False:
                ENTRY_DATE_ERROR = True
                
                show_error(Title.add_article, Error.wrong_date_format)
                
            else:
                ENTRY_DATE_ERROR = False
                
            if ENTRY_DATE_ERROR == False:
                import re
            
                artobj = Article(DB)
            
                artlibrary = artobj.load_articles()
                article = (self.title.text, self.categ.text, self.date_written.text)
            
                if (article in artlibrary) or (re.search(self.title.text, str([title[0] for title in artlibrary]), re.I)):
                    show_error(Title.add_article, Error.article_exists)
            
                else:
                    artobj.add_article(self.title.text.title(), self.categ.text, self.body.text, self.writer.text, self.date_written.text,  self.ref.text)
            
                self.title.text = ""
                self.categ = Text.select_category
                self.writer.text = Text.select_writer
                self.body.text = ""
                self.date_written.text = ""
                self.ref.text = ""
                
                self.manager.current = "articles"
        
        
class ArticleWriterSpinner(Spinner):
    def __init__(self, **kwargs):
        super(ArticleWriterSpinner, self).__init__(**kwargs)
        self.add_writers()
        
    def add_writers(self):
        obj = Article(DB)
        self.values = obj.load_writers()
        