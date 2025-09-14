from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner

from kivy.properties import ObjectProperty, StringProperty

from modules.datamanager import Task
from modules.helpers import show_error
from modules.definations import Error, Text, Title, AppColor
from modules.verifier import verify_date

import re
import datetime
from collections import deque

ENTRY_ALL_ERROR = True
ENTRY_DATE_ERROR = True

DB = "SuperMe.db"


class AddTaskWindow(Screen):
    task_name = ObjectProperty(None)
    date = ObjectProperty(None)
    dur1 = ObjectProperty(None) #textinput
    dur2 = ObjectProperty(None) #spinner
    categ = ObjectProperty(None)
    desc = ObjectProperty(None)
   
    def __init__(self, **kwargs):
        super(AddTaskWindow, self).__init__(**kwargs)
       
    def show_current_date(self):
    	today = datetime.date.today()
    	
    	return f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}"
    	 
    def show_current_time(self):
    	now = datetime.datetime.now()
    	hr = str(now.hour)
    	min = str(now.minute)
    	
    	return f"{hr.zfill(2)}{min.zfill(2)}"
    
    def add_task(self):
        if (self.task_name.text == "" or self.task_name.text.isspace() or
            self.date.text == "" or self.date.text.isspace() or 
            self.dur1.text == "" or self.dur1.text.isspace() or
            self.dur2.text == Text.select_duration or 
            self.categ.text == Text.select_category or
            self.desc.text == "" or self.desc.text.isspace()
            ):
                
            show_error(Title.add_task, Error.required)
               
        else:
            ENTRY_ALL_ERROR = False 
      
            if verify_date(self.date.text) == False:
                ENTRY_DATE_ERROR = True
                
                show_error(Title.add_task, Error.wrong_date_format)
                
            else:
                ENTRY_DATE_ERROR = False
            
                
            if ENTRY_ALL_ERROR == False and ENTRY_DATE_ERROR == False:
                taskobj = Task(DB)
                tasks = taskobj.load_tasks_names()
                task = (self.task_name.text)
            
                if (task in tasks) or (re.search(self.task_name.text, str(tasks), re.I)):
                    show_error(Title.add_task, Error.task_exists)
            
                else:
                    duration = f"{self.dur1.text} {self.dur2.text}"
                    due_date = self.calc_due_date(self.date.text, duration)
                    ctime = self.show_current_time()
                    
                    taskobj.add_task(self.task_name.text.title(), self.date.text, ctime, due_date, duration, self.categ.text, 2, self.desc.text)
            
                self.task_name.text = ""
                self.date.text = ""
                self.dur1.text = ""
                self.dur2.text = Text.select_duration
                self.categ.text = Text.select_category
                self.desc.text = ""
                 
                self.manager.current = "tasks"
        
    def calc_due_date(self, start_date, dur):
        datelst = start_date.split("-")
        dt_date = datetime.date(int(datelst[0]), int(datelst[1]), int(datelst[2])) 
        
        duration = dur.split(" ")
        
        if duration[1] == "Day(s)":
            days = datetime.timedelta(days=int(duration[0])) 
            end_date = dt_date + days
            
        elif duration[1] == "Week(s)":
            days = datetime.timedelta(days=int(duration[0]) * 7) 
            end_date = dt_date + days
            
        elif duration[1] == "Month(s)":
            days = datetime.timedelta(days=int(duration[0]) * 30.46) 
            end_date = dt_date + days
            
        elif duration[1] == "Year(s)":
            days = datetime.timedelta(days=int(duration[0]) * 365.52) 
            end_date = dt_date + days
            
        return end_date
