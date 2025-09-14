from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from modules.datamanager import Book, Quote

DB = "SuperMe.db"

class AuthorsWindow(Screen):
    def __init__(self, **kwargs):
        super(AuthorsAccordion, self).__init__(**kwargs)
        self.display_authors()
        
    def display_authors(self):
        authors = set()
        
        bo = Book(DB)
        book_authors = bo.load_book_authors_info()
        
        for det in book_authors:
            authors.add(det)
            
        qo = Quote(DB)
        quote_authors = qo.load_quotes_authors_info()
        
        for det in quote_authors:
            authors.add(det)
     
        acc = Accordion(orientation="vertical")
        
        for item in authors:
            author_name = item[0]
            occupation = item[1]
            country = item[2]
            desc = item[3]
            
            accitem = AccordionItem(title=f"{author_name}, [i]{occupation}, {country}[/i]")
            accitem.add_widget(Label(text=desc))
            acc.add_widget(accitem)
            
        return acc