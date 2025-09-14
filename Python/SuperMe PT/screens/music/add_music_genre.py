from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Music
from modules.helpers import show_error
from modules.definations import Error, Text, Title


DB = "SuperMe.db"


class AddMusicGenreWindow(Screen):
    genre = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddMusicGenreWindow, self).__init__(**kwargs)
        self.genredata = Text.select_genre
        
    def add_genre(self):
        if self.genre.text == "" or self.genre.text.isspace():
            show_error(Title.add_genre, Error.required)
            
        else:
            self.genredata = self.genre.text.title()
            
            musicobj = Music(DB)
            allgenres = musicobj.load_genres_lower()
            
            if self.genredata.lower() in allgenres:
                show_error(Title.add_genre, Error.genre_exists)
                
            else:
                musicobj.add_song_genre(self.genredata)
                
                self.genre.text = ""
                
            self.refresh_genres()
                
    def refresh_genres(self):
        mo = Music(DB)
        
        self.manager.get_screen('addmusic').ids.music_genre_spinner.values = mo.load_genres()
        self.manager.get_screen('addmusic').ids.music_genre_spinner.text = self.genredata
        
        self.manager.current = "addmusic"
    