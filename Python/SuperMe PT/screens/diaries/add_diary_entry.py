from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Diary
from modules.helpers import show_error, show_message
from modules.definations import Error, Text, Title, AppColor
from modules.verifier import verify_date, verify_time

import re
from collections import deque
from datetime import datetime
from datetime import date

ENTRY_ALL_ERROR = True
ENTRY_DATE_ERROR = True
ENTRY_TIME_ERROR = True

DB = "SuperMe.db"


class AddDiaryWindow(Screen):
    title = ObjectProperty(None)
    date = ObjectProperty(None)
    time = ObjectProperty(None)
    categ = ObjectProperty(None)
    mood = ObjectProperty(None)
    desc = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddDiaryWindow, self).__init__(**kwargs)
        
    def show_current_date(self):
    	today = date.today()
    	
    	return f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}"
    	
    def show_current_time(self):
    	now = datetime.now()
    	
    	return f"{now.hour}{now.minute}"
    
    def add_entry(self):
        '''Check if all fields are filled up'''
        
        if (self.title.text == "" or self.title.text.isspace() or
            self.date.text == "" or self.date.text.isspace() or 
            self.time.text == "" or self.time.text.isspace() or
            self.categ.text == Text.select_category or 
            self.mood.text == Text.select_mood or
            self.desc.text == "" or self.desc.text.isspace()
            ):
            
            show_message(Title.add_diary_entry, Error.required)
            
        else:
            ENTRY_ALL_ERROR = False 
      
            if verify_date(self.date.text) == False:
                ENTRY_DATE_ERROR = True
                
                show_error(Title.add_diary_entry, Error.wrong_date_format)
                
            else:
                ENTRY_DATE_ERROR = False
                
            if verify_time(self.time.text) == False:
                ENTRY_TIME_ERROR = True
                
                show_error(Title.add_diary_entry, Error.wrong_time_format)
                
            else:
                ENTRY_TIME_ERROR = False
                
                
            if ENTRY_ALL_ERROR == False and ENTRY_DATE_ERROR == False and ENTRY_TIME_ERROR == False:
                diaryobj = Diary(DB)
            
                entries = diaryobj.load_entries_titlecatmood()
                entry = (self.title.text, self.categ.text, self.mood.text)
            
                if (entry in entries) or (re.search(self.title.text, str([title[0] for title in entries]), re.I)):
                    show_error(Title.add_diary_entry, Error.diary_exists)
            
                else:
                    diaryobj.add_entry(self.title.text.title(), self.date.text, self.time.text, self.categ.text, self.mood.text.title(), self.desc.text)
            
                self.title.text = ""
                self.date.text = ""
                self.time.text = ""
                self.categ.text = Text.select_category
                self.mood.text = Text.select_mood
                self.desc.text = ""
                
                self.manager.current = "diaries"