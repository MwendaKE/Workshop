from kivy.app import App

from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty, StringProperty

from modules.datamanager import Task
from modules.helpers import ContentLabelView, show_error, show_info, show_message, confirm_delete

from kivy.clock import Clock

import re


DB = "SuperMe.db"


class TaskViewWindow(Screen):
    tv_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(TaskViewWindow, self).__init__(**kwargs)
        self.task_patt = "\[b\](.+)\[/b\]"
        Clock.schedule_once(self.edit_task, 0.1)
      
    def edit_task(self, *args):
        try:
            query = re.search(self.task_patt, self.tv_title.text)
        
        except:
            query = ""
            
        if query:    
            ttitle = query.group(1)
            
            taskobj = Task(DB)
            
            try:
                tid, dur, categ, desc = taskobj.edit_query(ttitle)
                
                app = App.get_running_app()
      
                app.root.ids.manager.get_screen('editask').ids.task_id_label.text = str(tid)
                app.root.ids.manager.get_screen('editask').ids.task_name_input.text = ttitle
                app.root.ids.manager.get_screen('editask').ids.task_categ_spinner.text = categ
                app.root.ids.manager.get_screen('editask').ids.task_duration_input.text = dur
                app.root.ids.manager.get_screen('editask').ids.task_desc_input.text = desc
               
                app.root.ids.manager.current = "editask"
    
            except Exception as e:
                show_error("Edit Task", f"Error: Cannot edit this entry.")
            
        else:
            pass
            
    def delete_task(self):
        query = re.search(self.task_patt, self.tv_title.text)
        
        if query:
            ttitle = query.group(1)
            
            txt = f"Delete [color=EF8887][b]{ttitle}[/b][/color] from tasks?"
            
            confirm_delete("Delete Task", txt, "Task", ttitle, "")
            
        else:
            show_error("Delete Task", "This task cannot be deleted.")
        
    def about_task(self):
        import humanize
        from modules.helpers import calc_true_time, calc_true_datetime
        
        query = re.search(self.task_patt, self.tv_title.text)
    
        if query:
            tv_title = query.group(1)
            
            taskobj = Task(DB)
            sdate, stime, edate, dur, categ, success = taskobj.about_query(tv_title)
            
            if stime:
                human_time = humanize.naturaltime(calc_true_datetime(sdate, stime))
                
            else:
            	human_time = humanize.naturaltime(calc_true_time(sdate))
           
            if success == 0:
            	success = "Failed"
            	
            elif success == 1:
            	success = "Completed"
            	
            else:
            	success = "Active"
            	
            if edate:
                human_time2 = humanize.naturaltime(calc_true_time(edate))
                
            else:
                human_time2 = "Undefined"
            
            text = f"Task:\n[color=83AE74]{tv_title}[/color]\nDate Started:\n[color=83AE74]{sdate} | {human_time}[/color]\nCompletion Time:\n[color=83AE74]{edate} | {human_time2}[/color]\nDuration:\n[color=83AE74]{dur} [/color]\nState:\n[color=83AE74]{success}[/color]"
            
            text_list = [{"text": t} for t in text.split("\n")]
            
            show_info("About Entry", text_list)

        else:
            show_error("About Entry", Message.no_book_description)
            
    
class TaskContentView(Screen):
    def __init__(self, taskkey, **kwargs):
        super(TaskContentView, self).__init__(**kwargs)
        self.task_key = taskkey
        self.app = App.get_running_app()
        
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args): 
        self.app.root.ids.manager.get_screen('taskview').ids.task_content_container.clear_widgets()
            
        task_patt = "\[b\](.+)\[/b\]"
        
        query = re.search(task_patt, self.task_key)
        
        if query:
            query = query.group(1)
            
            taskobj = Task(DB)
            
            try:
                task_content = taskobj.load_task(query)[0]
                
                if task_content:
                    from collections import deque
                    
                    content_list = deque()
                    
                    for content in task_content.split("\n\n"):
                        content_list.append(content)
                        
                else:
                    content_list = Message.no_task_content
            
            except Exception as error:
                content_list = Error.task_review_error
            
        else:
            content_list = "[color=FF0000]This content cannot be displayed![/color]"
        
        self.app.root.ids.manager.get_screen('taskview').ids.task_titlelabel.text = self.task_key
        
        if type(content_list) == deque:
            for paragraph in content_list:
                self.app.root.ids.manager.get_screen('taskview').ids.task_content_container.add_widget(ContentLabelView(text=paragraph))
            
        else:
            self.app.root.ids.manager.get_screen('taskview').ids.task_content_container.add_widget(ContentLabelView(text=content_list))
            
        self.app.root.ids.manager.current = "taskview"
        
        