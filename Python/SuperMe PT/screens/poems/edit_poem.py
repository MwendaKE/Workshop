from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Poem
from modules.helpers import show_error
from modules.definations import Text, Title, Error, AppColor

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"


class EditPoemWindow(Screen):
    poem_id_label = ObjectProperty(None)
    title = ObjectProperty(None)
    body = ObjectProperty(None)
    author = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditPoemWindow, self).__init__(**kwargs)
        
    def save_poem(self):
        if (self.title.text == "" or self.title.text.isspace() or 
            self.body.text == "" or self.body.text.isspace() or 
            self.author.text == Text.select_author
            ):
            show_error(Title.edit_poem, Error.required)
               
        else:
            pmobj = Poem(DB)
            
            poemid = self.poem_id_label if isinstance(self.poem_id_label, int) else int(self.poem_id_label.text)
            
            pmobj.update_query(poemid, self.title.text.title(), self.body.text, self.author.title())
            
            self.manager.current = "poems"
        
