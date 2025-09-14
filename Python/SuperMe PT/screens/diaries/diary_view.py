from kivy.app import App

from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty, StringProperty

from modules.datamanager import Diary
from modules.helpers import ContentLabelView, show_error, show_info, confirm_delete, show_message
from modules.definations import Message, Error, Title

from kivy.clock import Clock

import re
from collections import deque

DB = "SuperMe.db"


class DiaryViewWindow(Screen):
    dv_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DiaryViewWindow, self).__init__(**kwargs)
        self.diary_patt = "\[b\](.+)\[/b\]"
        Clock.schedule_once(self.edit_entry, 0.1)
   
    def edit_entry(self, *args):
        try:
            query = re.search(self.diary_patt, self.dv_title.text)
        
        except:
            query = ""
            
        if query:    
            dtitle = query.group(1)
            
            diaryobj = Diary(DB)
            
            try:
                did, categ, mood, desc = diaryobj.edit_query(dtitle)
                
                app = App.get_running_app()
                
                app.root.ids.manager.get_screen('editdiaryentry').ids.diary_id_label.text = str(did)
                app.root.ids.manager.get_screen('editdiaryentry').ids.diary_title_input.text = dtitle
                app.root.ids.manager.get_screen('editdiaryentry').ids.diary_categ_spinner.text = categ
                app.root.ids.manager.get_screen('editdiaryentry').ids.diary_mood_spinner.text = mood
                app.root.ids.manager.get_screen('editdiaryentry').ids.diary_desc_input.text = desc
               
                app.root.ids.manager.current = "editdiaryentry"
    
            except Exception as e:
                show_error("Edit Diary", f"Error: Cannot edit this entry.")
           
        else:
            diary_content = "[color=FF0000]Content for this Diary cannot be edited![/color]"
           
    def delete_entry(self):
        query = re.search(self.diary_patt, self.dv_title.text)
        
        if query:
            dv_title = query.group(1)
            
            txt = f"Delete [color=EF8887][b]{dv_title}[/b][/color] diary?"
            
            confirm_delete("Delete Entry", txt, "Diary", dv_title, "")
            
        else:
            show_error("Delete Entry", "This entry cannot be deleted.")
        
    def about_entry(self):
        import humanize
        from modules.helpers import calc_true_datetime
        
        query = re.search(self.diary_patt, self.dv_title.text)
    
        if query:
            dv_title = query.group(1)
            
            diaryobj = Diary(DB)
            dat, tim, cat, mood = diaryobj.about_query(dv_title)
            
            human_time = humanize.naturaltime(calc_true_datetime(dat, tim))
            
            text = f"Entry Name:\n[color=83AE74]{dv_title}[/color]\nDatetime:\n[color=83AE74]{dat}, {tim} Hrs | {human_time}[/color]\nMood:\n[color=83AE74]{mood}[/color]"
            
            text_list = [{"text": t} for t in text.split("\n")]
            
            show_info("About Entry", text_list)

        else:
            show_error("About Entry", Message.no_diary_description)
       
     
class DiaryContentView(Screen):
    def __init__(self, diarykey, **kwargs):
        super(DiaryContentView, self).__init__(**kwargs)
        self.diary_key = diarykey
        self.app = App.get_running_app()
        
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen('diaryview').ids.diary_content_container.clear_widgets()
                
        diary_patt = "\[b\](.+)\[/b\]"
        
        query = re.search(diary_patt, self.diary_key)
        
        if query:
            query = query.group(1)
            
            content_list = deque()
            
            diaryobj = Diary(DB)
            content_str = diaryobj.load_diary(query)[0].split("\n\n")
            	
            for item in content_str:
                content_list.append(item)
            	    
        else:
            content_list = Message.no_diary_content
        
        self.app.root.ids.manager.get_screen('diaryview').ids.diary_titlelabel.text = self.diary_key
        
        if type(content_list) == deque:
            for paragraph in content_list:
                self.app.root.ids.manager.get_screen('diaryview').ids.diary_content_container.add_widget(ContentLabelView(text=paragraph))
                
        else:
            self.app.root.ids.manager.get_screen('diaryview').ids.diary_content_container.add_widget(ContentLabelView(text=content_list))
                
        self.app.root.ids.manager.current = "diaryview"
  
        return