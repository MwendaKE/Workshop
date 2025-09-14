from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty

from modules.datamanager import Clip
from modules.helpers import show_error
from modules.definations import Error, Text, Title

from collections import deque

DB = "SuperMe.db"


class AddClipWindow(Screen):
    clip = ObjectProperty(None)
    writer = ObjectProperty(None)
    stitle = ObjectProperty(None)
    stype = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddClipWindow, self).__init__(**kwargs)
        
    def add_clip(self):
        if (self.clip.text == "" or self.clip.text.isspace() or
            self.writer.text == "" or self.writer.text.isspace() or 
            self.stitle.text == "" or self.stitle.text.isspace() or
            self.stype.text == Text.select_type
            ):
            show_error(Title.add_clip, Error.required)
               
        else:
            import re
            
            clipobj = Clip(DB)
            
            cliplibrary = clipobj.load_clips()
            clip = (self.clip.text.capitalize(), self.writer.text, self.stitle.text.title(), self.stype.text)
            
            if (clip in cliplibrary) or (re.search(self.clip.text, str([title[0] for title in cliplibrary]), re.I)):
                show_error(Title.add_clip, Error.clip_exists)
            
            else:
                clipobj.add_clip(self.clip.text, self.writer.text, self.stitle.text.title(), self.stype.text)
            
            self.clip.text = ""
            self.writer.text = ""
            self.stitle.text = ""
            self.stype.text = Text.select_type
                
            self.manager.current = "clips"
        
        