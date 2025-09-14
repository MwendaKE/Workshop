from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem
from modules.datamanager import Music

DB = "SuperMe.db"


class OneLineGenresView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLineGenresView, self).__init__(**kwargs)
        
        
class GenreWindow(Screen):
    def __init__(self, **kwargs):
        super(GenreWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.genres_container.clear_widgets()
        
        mo = Music(DB)
        genres = mo.load_genres()
        
        self.ids.genres_count.text = str(len(genres))
        
        for genre in genres:
            self.ids.genres_container.add_widget(OneLineGenresView(text=genre))
            
        return