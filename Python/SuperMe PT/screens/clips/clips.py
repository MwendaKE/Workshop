from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from modules.datamanager import Clip
from modules.definations import AppColor, Message

from collections import deque

DB = "SuperMe.db"
 
 
class ClipLabelView(MDLabel):
    def __init__(self, **kwargs):
        super(ClipLabelView, self).__init__(**kwargs)
         
                                                   
class ClipsWindow(Screen):
    def __init__(self, **kwargs):
        super(ClipsWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        clipobj = Clip(DB)
        clips = clipobj.load_clips()
        
        if clips:
            clips_count = clipobj.get_clips_count()
        
            self.data = set()
            
            for clip, writer, stitle, stype in clips:
                self.data.add((f"[color=#83AE74]{clip}[/color], [color=#26DDC7][i]{writer}[/color][color=#EAC155], {stype}: {stitle}[/i][/color]"))
                
            self.ids.clips_count.text = str(clips_count)
            
            for clip in self.data:
            	self.ids.clips_container.add_widget(ClipLabelView(text=clip))
         
        else:
            self.ids.clips_container.add_widget(ClipLabelView(text=Message.no_clips))
            
    def on_pre_leave(self, *args):
        self.ids.clips_container.clear_widgets()
        
        return