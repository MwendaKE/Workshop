from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from modules.helpers import show_error
from modules.datamanager import Music
from modules.definations import Error, Text, Title

from kivy.properties import ObjectProperty

DB = "SuperMe.db"

class AddArtistWindow(Screen):
    artist_name = ObjectProperty(None)
    country = ObjectProperty(None)
    description = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddArtistWindow, self).__init__(**kwargs)
        self.artistname = Text.select_artist
        
    def add_artist(self):
        if (self.artist_name.text == "" or self.artist_name.text.isspace() or
            self.country.text == Text.select_country or
            self.description.text == "" or self.description.text.isspace()
            ):
            show_error(Title.add_music_artist, Error.required)
        
        else:
            self.artistname = self.artist_name.text.title()
            
            musicobj = Music(DB)
            
            allartists = musicobj.load_artists_lower()
            
            if self.artistname.lower() in allartists:
                show_error(Title.add_artist, Error.artist_exists)
                
            else:
                musicobj.add_song_artist(self.artistname, self.country.text, self.description.text)
            
                self.artist_name.text = ""
                self.country.text = Text.select_country
                self.description.text = ""
            
            self.refresh_artists_spinner()
            
    def refresh_artists_spinner(self):
        mo = Music(DB)
        
        self.manager.get_screen('addmusic').ids.music_artist_spinner.values = mo.load_artists()
        self.manager.get_screen('editmusic').ids.music_artist_spinner.values = mo.load_artists()
        
        self.manager.current = "artists"
        
        return
    