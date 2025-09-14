from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem
from modules.datamanager import Book, Quote
from modules.definations import Message


DB = "SuperMe.db"


class OneLineAuthorView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLineAuthorView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.menu.author_view import AuthorContentWindow
            
        if not Message.no_authors in self.text:
            AuthorContentWindow(self.text)
        
        
class AuthorsWindow(Screen):
    def __init__(self, **kwargs):
        super(AuthorsWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.authors_container.clear_widgets()
        
        authors = set()
        
        bo = Book(DB)
        book_authors = bo.load_book_authors()
        
        for author in book_authors:
            authors.add(author)
            
        qo = Quote(DB)
        quote_authors = qo.load_authors()
        
        for author in quote_authors:
            authors.add(author)
            
        self.ids.authors_count.text = str(len(authors))
         
        for author in authors:
            self.ids.authors_container.add_widget(OneLineAuthorView(text=author))
            
