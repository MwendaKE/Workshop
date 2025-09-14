from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from modules.datamanager import Quote
from modules.definations import Message
from modules.helpers import show_info

from collections import deque

DB = "SuperMe.db"
        

class QuoteLabelView(MDLabel):
    def __init__(self, **kwargs):
        super(QuoteLabelView, self).__init__(**kwargs)


class QuotesWindow(Screen):
    def __init__(self, **kwargs):
        super(QuotesWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        quotesobj = Quote(DB)
        quotes = quotesobj.load_quotes()
        
        if quotes:
            quotes_count = quotesobj.get_quotes_count()
        
            data = deque()
            
            for author, quote in quotes:
                data.append(f"[color=#26DDC7]{quote}[/color], [color=#EAC155][i]{author}[/i][/color]")
                
            self.ids.quotes_count.text = quotes_count
        
            for quote in data:
            	self.ids.quotes_container.add_widget(QuoteLabelView(text=quote))
         
        else:
            self.ids.quotes_container.add_widget(QuoteLabelView(text=Message.no_quotes))
            
    def on_pre_leave(self, *args):
        self.ids.quotes_container.clear_widgets()
        
        return        