from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Book
from modules.helpers import show_error
from modules.definations import Text, Title, Error, AppColor

from collections import deque


DB = "SuperMe.db"


class AddBookWindow(Screen):
    author = ObjectProperty(None)
    title = ObjectProperty(None)
    category = ObjectProperty(None)
    review = ObjectProperty(None)
    about = ObjectProperty(None)
    isbn = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddBookWindow, self).__init__(**kwargs)
        self.read_status = -1
        
    def check_read_status(self, instance, value, status):
        if value == True:
            self.read_status = status
            
        else:
            self.read_status = -1
        
    def add_book(self):
        if (self.author.text == Text.select_author or 
            self.title.text == "" or self.title.text.isspace() or 
            self.category.text == Text.select_category or 
            self.review.text == "" or self.review.text.isspace() or
            self.about.text == "" or self.about.text.isspace() or 
            self.isbn.text == "" or self.isbn.text.isspace() or
            self.read_status == -1
           ):
            show_error(Title.add_book, Error.required)
               
        else:
            import re
            
            bookobj = Book(DB)
      
            library = bookobj.load_books()
            book = (self.author.text, self.title.text)
            
            if (book in library) or (re.search(self.title.text, str([title[1] for title in library]), re.I)):
                show_error(Title.add_book, Error.book_exists)
            
            else:
                bookobj.add_book(self.author.text, self.title.text.title(), self.category.text, self.isbn.text, self.review.text, self.about.text, self.read_status)
            
                self.author.text = Text.select_author
                self.title.text = ""
                self.category.text = Text.select_category
                self.isbn.text = ""
                self.review.text = ""
                self.about.text = ""
                self.read_status = -1
                
            self.manager.current = "books"
            
      
class BooksAuthorSpinner(Spinner):
    def __init__(self, **kwargs):
        super(BooksAuthorSpinner, self).__init__(**kwargs)
        self.add_authors()
        
    def add_authors(self):
        authorobj = Book(DB)
        self.values = authorobj.load_book_authors()
        