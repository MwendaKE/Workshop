from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineIconListItem

from modules.definations import AppColor, Message
from modules.datamanager import Task
from modules.helpers import calc_true_time, calc_true_date, calc_days_active

import humanize, datetime
from collections import deque

DB = "SuperMe.db"


class ThreeLineTaskView(ThreeLineIconListItem):
    def __init__(self, **kwargs):
        super(ThreeLineTaskView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.tasks.task_view import TaskContentView

        if not Message.no_tasks in self.text:
            TaskContentView(self.text)
            
        return
    
    
class TasksWindow(Screen):
    def __init__(self, **kwargs):
        super(TasksWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        tasksobj = Task(DB)
        tasks = tasksobj.load_tasks()
        
        if tasks:
            tasks_count = tasksobj.get_tasks_count()
            tasks_complete = tasksobj.get_completetasks_count()
            tasks_failed = tasksobj.get_failedtasks_count()
            tasks_active = tasksobj.get_activetasks_count()
         
            self.data = deque()
            
            for task, start_date, end_date, category, duration, success in tasks:
                human_time = humanize.naturaltime(calc_true_time(end_date))
                human_sdate = humanize.naturaldate(calc_true_date(start_date))
                human_edate = humanize.naturaldate(calc_true_date(end_date))
               
                if calc_days_active(end_date) < 0 and int(success) == 2:
                    self.update_task_active_status(1, task)
                    
                if calc_days_active(end_date) < 0 and int(success) == 0:
                    self.data.append((f"[color={AppColor.lightred_tc}][b]{task}[/b][/color]", f"{human_sdate} — {human_edate}, {duration}", f"Due: {human_time}"))      
                
                elif (calc_days_active(end_date) >= 0 and int(success) == 1) or (calc_days_active(end_date) < 0 and int(success) == 1):
                    self.data.append((f"[color={AppColor.green_tc}][b]{task}[/b][/color]", f"{human_sdate} — {human_edate}, {duration}", f"Due: {human_time}"))
                    
                elif calc_days_active(end_date) >= 0 and int(success) == 2:
                    self.data.append((f"[color={AppColor.yellow_tc}][b]{task}[/b][/color]", f"{human_sdate} — {human_edate}, {duration}", f"Due: {human_time}"))
                   
                else:
                    self.data.append((f"[color={AppColor.white_tc}][b]{task}[/b][/color]", f"[i]Undefined task[/i][/color]", f"Category: Undefined"))
                    
            self.ids.total_tasks_count.text = tasks_count
            self.ids.tasks_complete.text = tasks_complete
            self.ids.tasks_failed.text = tasks_failed
            self.ids.tasks_active.text = tasks_active
     
            for task, time, categ in self.data:
                self.ids.tasks_container.add_widget(ThreeLineTaskView(text=task, secondary_text=time, tertiary_text=categ))
        
        else:
            self.ids.tasks_container.add_widget(ThreeLineTaskView(text=Message.no_tasks, secondary_text="", tertiary_text=""))
            
        return
        
    def on_pre_leave(self, *args):
        self.ids.tasks_container.clear_widgets()
        
        return
         
    def update_task_active_status(self, status, tname):
        obj = Task(DB)
        obj.update_active_status(status, tname)
        
        return