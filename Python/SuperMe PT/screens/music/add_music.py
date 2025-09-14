from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Music
from modules.helpers import show_error
from modules.definations import Error, Text, Title

from collections import deque

DB = "SuperMe.db"


class AddMusicWindow(Screen):
    artist = ObjectProperty(None)
    song_title = ObjectProperty(None)
    genre = ObjectProperty(None)
    lyries = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddMusicWindow, self).__init__(**kwargs)
        
    def add_song(self):
        if (self.artist.text == Text.select_artist or 
            self.song_title.text == "" or self.song_title.text.isspace() or 
            self.genre.text == Text.select_genre or 
            self.lyries.text == "" or self.lyries.text.isspace()
            ):
            show_error(Title.add_music, Error.required)
               
        else:
            import re
            
            musicobj = Music(DB)
            
            musiclibrary = musicobj.load_songs()
            song = (self.artist.text, self.song_title.text)
            
            if (song in musiclibrary) or (re.search(self.song_title.text, str([title[1] for title in musiclibrary]), re.I)):
                show_error(Title.add_music, Error.music_exists)
            
            else:
                musicobj.add_song(self.artist.text, self.song_title.text.title(), self.lyries.text, self.genre.text)
            
            self.artist.text = Text.select_artist
            self.song_title.text = ""
            self.genre.text = Text.select_genre
            self.lyries.text = ""
                
            self.manager.current = "music"
        
        
class MusicArtistSpinner(Spinner):
    def __init__(self, **kwargs):
        super(MusicArtistSpinner, self).__init__(**kwargs)
        self.add_artists()
        
    def add_artists(self):
        musicobj = Music(DB)
        self.values = musicobj.load_artists()
        
        
class MusicGenreSpinner(Spinner):
    def __init__(self, **kwargs):
        super(MusicGenreSpinner, self).__init__(**kwargs)
        self.add_genres()
        
    def add_genres(self):
        musicobj = Music(DB)
        self.values = musicobj.load_genres()