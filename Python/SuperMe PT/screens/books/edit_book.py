from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Book
from modules.helpers import show_error
from modules.definations import Text, Title, Error, AppColor

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"


class EditBookWindow(Screen):
    book_id = ObjectProperty(None)
    author = ObjectProperty(None)
    title = ObjectProperty(None)
    category = ObjectProperty(None)
    review = ObjectProperty(None)
    about = ObjectProperty(None)
    isbn = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditBookWindow, self).__init__(**kwargs)
        self.read_status = -1
        
    def check_read_status(self, instance, value, status):
        if value == True:
            self.read_status = status
            
        else:
            self.read_status = -1
        
    def save_book(self):
        if (self.author.text == Text.select_author or 
            self.title.text == "" or self.title.text.isspace() or 
            self.category.text == Text.select_category or 
            self.review.text == "" or self.review.text.isspace() or
            self.about.text == "" or self.about.text.isspace() or 
            self.isbn.text == "" or self.isbn.text.isspace() or
            self.read_status == -1
           ):
            show_error(Title.edit_book, Error.required)
               
        else:
            bookobj = Book(DB)
          
            self.bookid = self.book_id if isinstance(self.book_id, int) else int(self.book_id.text)
                
            bookobj.update_query(self.bookid, self.author.text, self.title.text.title(), self.category.text, self.isbn.text, self.review.text, self.read_status, self.about.text)
            
            self.manager.current = "books"
        
        
class BooksAuthorSpinner(Spinner):
    def __init__(self, **kwargs):
        super(BooksAuthorSpinner, self).__init__(**kwargs)
        self.add_authors()
        
    def add_authors(self):
        authorobj = Book(DB)
        self.values = authorobj.load_book_authors()