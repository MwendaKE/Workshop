from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem

from modules.datamanager import Music
from modules.definations import Message

DB = "SuperMe.db"


class OneLineArtistView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLineArtistView, self).__init__(**kwargs)
    
    def on_release(self):
        from screens.menu.artist_view import ArtistContentWindow
            
        if not Message.no_artists in self.text:
            ArtistContentWindow(self.text)
         
        
class ArtistsWindow(Screen):
    def __init__(self, **kwargs):
        super(ArtistsWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.artists_container.clear_widgets()
        
        mo = Music(DB)
        artists = mo.load_artists()
        
        self.ids.artists_count.text = str(len(artists))
        
        for artist in artists:
            self.ids.artists_container.add_widget(OneLineArtistView(text=artist))
            
        return