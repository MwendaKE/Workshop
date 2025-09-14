from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty

from modules.datamanager import Event
from modules.helpers import show_error
from modules.definations import Error, Text, Title, AppColor
from modules.verifier import verify_date, verify_time, verify_event_attendance

import re
import datetime
from collections import deque

ENTRY_ALL_ERROR = True
ENTRY_DATE_ERROR = True
ENTRY_TIME_ERROR = True

DB = "SuperMe.db"


class EditEventWindow(Screen):
    event_id = ObjectProperty(None)
    event_name = ObjectProperty(None)
    date = ObjectProperty(None)
    time = ObjectProperty(None)
    venue = ObjectProperty(None)
    address = ObjectProperty(None)
    notes = ObjectProperty(None)
    budget = ObjectProperty(None)
    att = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditEventWindow, self).__init__(**kwargs)
        
    def save_event(self):
        if (self.event_name.text == "" or self.event_name.text.isspace() or
            self.date.text == "" or self.date.text.isspace() or 
            self.time.text == "" or self.time.text.isspace() or
            self.venue.text == "" or self.venue.text.isspace() or 
            self.address.text == "" or self.address.text.isspace() or
            self.notes.text == "" or self.notes.text.isspace() or
            self.budget.text == "" or self.budget.text.isspace() or
            self.att.text == "Select Attendance"
            ):
            	
            show_error(Title.add_event, Error.required)
               
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
                eventobj = Event(DB)
            
                eventid = self.event_id if isinstance(self.event_id, int) else int(self.event_id.text)
                attendance = verify_event_attendance(self.att.text)
                    
                eventobj.update_query(eventid, self.event_name.text.title(), self.date.text, self.time.text, self.venue.text.title(), self.address.text.title(), self.budget.text, self.notes.text, attendance)
            
                self.manager.current = "events"