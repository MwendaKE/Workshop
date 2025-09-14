from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

from modules.datamanager import Book
from modules.helpers import ContentLabelView, WarningPopup, confirm_delete, show_message, show_error, show_warning, show_info
from modules.definations import Message, Error

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"


class BookViewWindow(Screen):
    bk_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(BookViewWindow, self).__init__(**kwargs)
        self.book_patt = "\[b\](.+)\[\/b\] by \[b\](.+)\[\/b\]"
        
        Clock.schedule_once(self.edit_book, 0.1)
      
    def edit_book(self, *args):
        query = re.search(self.book_patt, self.bk_title.text)
        
        if query:    
            bktitle = query.group(1)
            bkauthor = query.group(2)
            
            bookobj = Book(DB)
            
            try:
                bookid, author, book_title, category, isbn, review, book_read, description = bookobj.edit_query(bktitle, bkauthor)
                
                app = App.get_running_app()
                
                app.root.ids.manager.get_screen('editbook').ids.bookid_label.text = f"{bookid}"
                app.root.ids.manager.get_screen('editbook').ids.book_author_spinner.text = author
                app.root.ids.manager.get_screen('editbook').ids.book_title_input.text = book_title
                app.root.ids.manager.get_screen('editbook').ids.book_category_spinner.text = category
                app.root.ids.manager.get_screen('editbook').ids.book_isbn_input.text = isbn
                app.root.ids.manager.get_screen('editbook').ids.book_review_input.text = review
                app.root.ids.manager.get_screen('editbook').ids.book_about_input.text = description
                
                app.root.ids.manager.current = "editbook"
    
                
            except Exception as e:
                show_error("Edit Book", f"Error: Cannot edit this book, {e}.")
                
        else:
            book_content = "[color=FF0000]Content for this book cannot be edited![/color]"
           
    def delete_book(self):
        query = re.search(self.book_patt, self.bk_title.text)
        
        if query:
            bk_title = query.group(1)
            bk_author = query.group(2)
            
            txt = f"Delete [color=EF8887][b]{bk_title}[/b][/color] by [color=EF8887][i]{bk_author}?[/i][/color]"
            
            confirm_delete("Delete Book", txt, "Book", bk_title, bk_author)
            
        else:
            show_error("Delete Book", "This book cannot be deleted.")
        
    def about_book(self):
        query = re.search(self.book_patt, self.bk_title.text)
        
        if query:
            bk_title = query.group(1)
            bk_author = query.group(2)
            
            bookobj = Book(DB)
            bk_about = bookobj.about_query(bk_title, bk_author)
          
            about_list = [{"text": value.strip()} for value in bk_about.split("\n\n")]
            
            show_info("About Book", about_list)
          
        else:
            show_error("About Book", Message.no_book_description)
          
    
class BookContentView(Screen):
    def __init__(self, bktitle, **kwargs):
        super(BookContentView, self).__init__(**kwargs)
        self.bktitle = bktitle
        self.app = App.get_running_app()
         
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('bookview').ids.book_content_container.clear_widgets()
       
        book_patt = "\[b\](.+)\[\/b\](.+)\[i\], (.+)\[\/i\]"
        
        query = re.search(book_patt, self.bktitle)
        
        if query:
            bookid = query.group(3)
            
            bookobj = Book(DB)
            
            try:
                bktitle, bkauthor, bkreview = bookobj.load_book_content(int(bookid))
                
                if bkreview:
                    book_content = deque()
                    
                    for content in bkreview.split("\n\n"):
                        book_content.append(content)
                    
                else:
                    book_content = Message.no_book_review
                
            except Exception as e:
                book_content = f"{Error.book_review_error}, '{e}'."
                
        else:
            book_content = Message.no_book_content
         
        self.app.root.ids.manager.get_screen('bookview').ids.book_titlelabel.text = f"[b]{bktitle}[/b] by [b]{bkauthor}[/b]"
        
        if type(book_content) == deque:
            for paragraph in book_content:
                self.app.root.ids.manager.get_screen('bookview').ids.book_content_container.add_widget(ContentLabelView(text=paragraph))
            
        else:
             self.app.root.ids.manager.get_screen('bookview').ids.book_content_container.add_widget(ContentLabelView(text=book_content))
            
        self.app.root.ids.manager.current = "bookview"
        
        return
        
        
