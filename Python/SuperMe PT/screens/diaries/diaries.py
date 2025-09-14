from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineIconListItem

from modules.datamanager import Diary
from modules.definations import AppColor, Message

from collections import deque
from datetime import datetime

DB = "SuperMe.db"


class TwoLineDiaryView(TwoLineIconListItem):
    def __init__(self, **kwargs):
        super(TwoLineDiaryView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.diaries.diary_view import DiaryContentView
        
        if not Message.no_diary in self.text:
            DiaryContentView(self.text)
            
        return
            
            
class DiariesWindow(Screen):
    def __init__(self, **kwargs):
        super(DiariesWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        diaryobj = Diary(DB)
        entries = diaryobj.load_entries()
        
        if entries:
            entry_count = diaryobj.get_entry_count()
        
            self.data = deque()
            
            self.ids.entry_count.text = entry_count
        
            for entry, date, time, mood in entries:
                dt_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H%M").strftime("%a, %d %b %Y, %I:%M %p")
                
                if mood == "Sad":
                    self.data.append((f"[color={AppColor.lightred_tc}][b]{entry}[/b][/color], [i]{mood}[/i]", f"[i]{dt_time}[/i]"))                   
                elif mood == "Happy":
                    self.data.append((f"[color={AppColor.green_tc}][b]{entry}[/b][/color], [i]{mood}[/i]", f"[i]{dt_time}[/i]"))
                    
                elif mood == "Confused":
                    self.data.append((f"[color={AppColor.white_tc}][b]{entry}[/b][/color], [i]{mood}[/i]", f"[i]{dt_time}[/i]"))
                    
                else:
                    self.data.append((f"[color={AppColor.yellow_tc}][b]{entry}[/b][/color], [i]{mood}[/i]", f"[i]{dt_time}[/i]"))
          
            for diary, time in self.data:
                self.ids.diaries_container.add_widget(TwoLineDiaryView(text=diary, secondary_text=time))
            
        else:
            self.ids.diaries_container.add_widget(TwoLineDiaryView(text=Message.no_diary, secondary_text=""))
            
        return

    def on_pre_leave(self, *args):
        self.ids.diaries_container.clear_widgets()
        
        return            