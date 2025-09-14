from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineIconListItem

from modules.datamanager import Music
from modules.definations import Message

from collections import deque

DB = "SuperMe.db"
 
 
class TwoLineMusicView(TwoLineIconListItem):
    def __init__(self, **kwargs):
        super(TwoLineMusicView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.music.music_view import MusicContentView
        
        if not Message.no_music in self.text:
            MusicContentView(self.text)
        
        return
        
                              
class MusicWindow(Screen):
    def __init__(self, **kwargs):
        super(MusicWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        musicobj = Music(DB)
        music = musicobj.load_songs()
        
        if music:
            music_count = musicobj.get_music_count()
        
            self.data = deque()
            
            for artist, song in music:
                self.data.append((f"[b]{song}[/b]", f"[i]{artist}[/i]"))
                
            self.ids.music_count.text = music_count
            
            for song, artist in self.data:
                self.ids.music_container.add_widget(TwoLineMusicView(text=song, secondary_text=artist))
         
        else:
            self.ids.music_container.add_widget(TwoLineMusicView(text=Message.no_music, secondary_text=""))
        
        return
        
    def on_pre_leave(self, *args):
        self.ids.music_container.clear_widgets()
       
        return    