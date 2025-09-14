from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem

from modules.datamanager import Article
from modules.definations import Message

DB = "SuperMe.db"


class OneLineWriterView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLineWriterView, self).__init__(**kwargs)
    
    def on_release(self):
        from screens.menu.writer_view import WriterContentWindow
            
        if not Message.no_writers in self.text:
            WriterContentWindow(self.text)
         
        
class WritersWindow(Screen):
    def __init__(self, **kwargs):
        super(WritersWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.writers_container.clear_widgets()
        
        ao = Article(DB)
        writers = ao.load_writers()
        
        self.ids.writers_count.text = str(len(writers))
        
        for writer in writers:
            self.ids.writers_container.add_widget(OneLineWriterView(text=writer))
            
        return