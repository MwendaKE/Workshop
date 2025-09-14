from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

from kivy.uix.screenmanager import Screen

from modules.datamanager import Music
from modules.helpers import ContentLabelView, confirm_delete, show_error, show_message, show_info
from modules.definations import Message, Error, Title

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"


class MusicViewWindow(Screen):
    ms_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(MusicViewWindow, self).__init__(**kwargs)
        self.music_auth_patt = "\[b\](.+)\[\/b\] by \[b\](.+)\[\/b\]"
        Clock.schedule_once(self.edit_song, 0.1)
      
    def edit_song(self, msong, *args):
        pass
        
    def delete_song(self):
        query = re.search(self.music_auth_patt, self.ms_title.text)
           
        if query:
            ms_title = query.group(1)
            ms_artist = query.group(2)
            
            txt = f"Delete [color=EF8887][b]{ms_title}[/b][/color] by [color=EF8887][i]{ms_artist}?[/i][/color]"
            
            confirm_delete("Delete Song", txt, "Music", ms_title, ms_artist)
   
        else:
            show_error("Delete Song", "Error: This song cannot be deleted.")
        
    def about_song(self):
        query = re.search(self.music_auth_patt, self.ms_title.text)
           
        if query:
            ms_title = query.group(1)
            ms_artist = query.group(2)
            
            musicobj = Music(DB)
            art, song, genre = musicobj.about_query(ms_title, ms_artist)
            
            text_str = f"[b]Song: [/b]\n[color=83AE74]{song}\n[/color][b]Artist: [/b]\n[color=83AE74]{art}[/color]\n[b]Genre: [/b]\n[color=83AE74]{genre}[/color]"
            text_list = text_str.split("\n")
            
            show_info("About Song", [{'text': t} for t in text_list])
            
        else:
            show_error("About Book", Message.no_book_description)
       
       
class MusicContentView(Screen):
    def __init__(self, musictitle, **kwargs):
        super(MusicContentView, self).__init__(**kwargs)
        self.music_title = musictitle
        self.app = App.get_running_app()
        
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('songview').ids.lyries_container.clear_widgets()
            
        music_art_patt = "\[b\](.+)\[/b\]"
        artist = "Undefined"
        query = re.search(music_art_patt, self.music_title)
        
        if query:
            ms_title = query.group(1)
            
            musicobj = Music(DB)
            
            try:
                artist, music_content = musicobj.load_song(ms_title)
                
                if music_content:
                    music_lyries = deque()
                    
                    for content in music_content.split("\n\n"):
                        music_lyries.append(content)
                        
                else:
                    music_lyries = Message.no_music_lyries
                    
                
            except Exception as error:
                music_lyries = f"[color=FF0000]This content cannot be displayed!; {error}.[/color]"
            
        else:
            music_lyries = "[color=FF0000]Undefined music lyries![/color]"
        
        self.app.root.ids.manager.get_screen('songview').ids.music_titlelabel.text = f"[b]{ms_title}[/b] by [b]{artist}[/b]"
        
        if type(music_lyries) == deque:
            for paragraph in music_lyries:
                self.app.root.ids.manager.get_screen('songview').ids.lyries_container.add_widget(ContentLabelView(text=paragraph))
            
        else:
             self.app.root.ids.manager.get_screen('songview').ids.lyries_container.add_widget(ContentLabelView(text=music_lyries))
            
        self.app.root.ids.manager.current = "songview"
        
        