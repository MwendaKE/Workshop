from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Article
from modules.helpers import show_error
from modules.definations import Error, Text, Title, AppColor
from modules.verifier import verify_date, verify_time, verify_event_attendance

import re
import datetime
from collections import deque

ENTRY_ALL_ERROR = True
ENTRY_DATE_ERROR = True

DB = "SuperMe.db"


class EditArticleWindow(Screen):
    art_id = ObjectProperty(None)
    title = ObjectProperty(None)
    categ = ObjectProperty(None)
    body = ObjectProperty(None)
    writer = ObjectProperty(None)
    date = ObjectProperty(None)
    ref = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditArticleWindow, self).__init__(**kwargs)
        
    def save_article(self):
        if (self.title.text == "" or self.title.text.isspace() or
            self.categ.text == Text.select_category or 
            self.body.text == "" or self.body.text.isspace() or
            self.writer.text == Text.select_writer or 
            self.date.text == "" or self.date.text.isspace() or
            self.ref.text == "" or self.ref.text.isspace()
            ):
            	
            show_error(Title.edit_article, Error.required)
               
        else:
            ENTRY_ALL_ERROR = False 
      
            if verify_date(self.date.text) == False:
                ENTRY_DATE_ERROR = True
                
                show_error(Title.edit_article, Error.wrong_date_format)
                
            else:
                ENTRY_DATE_ERROR = False
           
            if ENTRY_ALL_ERROR == False and ENTRY_DATE_ERROR == False:
                artobj = Article(DB)
            
                artid = self.art_id if isinstance(self.art_id, int) else int(self.art_id.text)
                
                artobj.update_query(artid, self.title.text.title(), self.categ.text, self.body.text, self.writer.text, self.date.text, self.ref.text)
            
                self.manager.current = "articles"