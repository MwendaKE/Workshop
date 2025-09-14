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


DB = "SuperMe.db"


class EditTaskWindow(Screen):
    task_id = ObjectProperty(None)
    task_name = ObjectProperty(None)
    categ = ObjectProperty(None)
    desc = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EditTaskWindow, self).__init__(**kwargs)
        self.active_status = -1
        
    def check_active_status(self, instance, value, status):
        if value == True:
            self.active_status = status
            
        else:
            self.active_status = -1
        
    def save_task(self):
        if (self.categ.text == Text.select_category or
            self.active_status == -1 or
            self.desc.text == "" or self.desc.text.isspace()
            ):
                
            show_error(Title.add_task, Error.required)
               
        else:
            taskid = self.task_id if isinstance(self.task_id, int) else int(self.task_id.text)
             
            taskobj = Task(DB)
            
            taskobj.update_query(taskid, self.task_name.text, self.categ.text, self.desc.text, self.active_status)
            
            self.manager.current = "tasks"
        