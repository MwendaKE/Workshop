from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from kivymd.uix.list import TwoLineIconListItem

from modules.datamanager import Book
from modules.definations import AppColor, Message

from collections import deque


DB = "SuperMe.db"


class TwoLineBookView(TwoLineIconListItem):
    def __init__(self, **kwargs):
        super(TwoLineBookView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.books.book_view import BookContentView
        
        if not Message.no_books in self.text:
            BookContentView(self.text)
            
        return
        
    
class BooksWindow(Screen):
    def __init__(self, **kwargs):
        super(BooksWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self, *args):
        booksobj = Book(DB)
        books = booksobj.load_books_with_status()
        
        if books:
            books_count = booksobj.get_books_count()
            count_read = booksobj.get_readbooks_count()
            count_reading = booksobj.get_readingbooks_count()
            count_unread = booksobj.get_unreadbooks_count()
            
            self.data = deque()
        
            for id, author, book, status in books:
                if status == 0:
                    self.data.append((f"[color={AppColor.lightred_tc}][b]{book}[/b][/color][color=#111111][i], {id}[/i][/color]", f"[i]{author}[/i]"))
                
                elif status == 1:
                    self.data.append((f"[color={AppColor.green_tc}][b]{book}[/b][/color][color=#111111][i], {id}[/i][/color]", f"[i]{author}[/i]"))
                    
                else:
                    self.data.append((f"[color={AppColor.yellow_tc}][b]{book}[/b][/color][color=#111111][i], {id}[/i][/color]", f"[i]{author}[/i]"))
            
            self.ids.books_total_count.text = f"{books_count}"
            self.ids.books_count.text = "BOOKS:"
            self.ids.books_read.text = count_read
            self.ids.books_reading.text = count_reading
            self.ids.books_unread.text = count_unread
            
            for book, author in self.data:
                self.ids.books_container.add_widget(TwoLineBookView(text=book, secondary_text=author))
          
        else:
            self.ids.books_container.add_widget(TwoLineBookView(text=Message.no_books, secondary_text=""))
            
        return
        
    def on_pre_leave(self, *args):
       self.ids.books_container.clear_widgets()
       
       return
        
       
