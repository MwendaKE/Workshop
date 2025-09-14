from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Diary
from modules.helpers import show_error
from modules.definations import Error, Text, Title, AppColor
from modules.verifier import verify_date, verify_time

import re
from collections import deque
from datetime import datetime


DB = "SuperMe.db"


class EditDiaryWindow(Screen):
    diary_id = ObjectProperty(None)
    title = ObjectProperty(None)
    categ = ObjectProperty(None)
    mood = ObjectProperty(None)
    desc = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditDiaryWindow, self).__init__(**kwargs)
        
    def save_entry(self):
        '''Check if all fields are filled up'''
        
        if (self.categ.text == Text.select_category or 
            self.mood.text == Text.select_mood or
            self.desc.text == "" or self.desc.text.isspace()
            ):
            
            show_error(Title.add_diary_entry, Error.required)
            
        else:
            diaryid = self.diary_id if isinstance(self.diary_id, int) else int(self.diary_id.text)
             
            diaryobj = Diary(DB)
            
            diaryobj.update_query(diaryid, self.title.text, self.categ.text, self.mood.text, self.desc.text)
            
            self.manager.current = "diaries"
         