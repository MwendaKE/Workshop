from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineIconListItem

from modules.datamanager import Event
from modules.definations import AppColor, Message
from modules.helpers import calc_true_datetime, calc_true_date
from modules.verifier import verify_event_attendance
   
import humanize
from collections import deque
from datetime import datetime

DB = "SuperMe.db"


class ThreeLineEventView(ThreeLineIconListItem):
    def __init__(self, **kwargs):
        super(ThreeLineEventView, self).__init__(**kwargs)
        
    def on_release(self):
    	from screens.events.event_view import EventContentView
    	
    	if not Message.no_events in self.text:
    	    EventContentView(self.text)
    	    
    	return
	

class EventsWindow(Screen):
    def __init__(self, **kwargs):
        super(EventsWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args): 
        eventsobj = Event(DB)
        events = eventsobj.load_events()
        
        if events:
            events_count = eventsobj.get_events_count()
        
            self.data = deque()
            
            self.ids.events_count.text = events_count
            
            for event, date, time, venue, att in events:
                human_time = humanize.naturaltime(calc_true_datetime(date, time))
                human_date = humanize.naturaldate(calc_true_date(date))
                
                if att == 0:
                	self.data.append((f"[b]{event}[/b]", f"[color={AppColor.teal_tc}]{venue}, [i]{verify_event_attendance(att)}[/color][/i]", f"[i]{human_date}, {human_time}[/i]"))
                
                elif att == 1:
                	self.data.append((f"[b]{event}[/b]", f"[color={AppColor.teal_tc}]{venue}, [i]{verify_event_attendance(att)}[/color][/i]", f"[i]{human_date}, {human_time}[/i]"))
                	
                elif att == 2:
                	self.data.append((f"[b]{event}[/b]", f"[color={AppColor.teal_tc}]{venue}, [i]{verify_event_attendance(att)}[/color][/i]", f"[i]{human_date}, {human_time}[/i]"))
                	
                else:
                	self.data.append((f"[b]{event}[/b]", f"[color={AppColor.yellow_tc}]{venue}, [i]{verify_event_attendance(att)}[/color][/i]", f"[i]{human_date}, {human_time}[/i]"))
              
          
            for event, venue, time in self.data:
                self.ids.events_container.add_widget(ThreeLineEventView(text=event, secondary_text=venue, tertiary_text=time))
 
        else:
            self.ids.events_container.add_widget(ThreeLineEventView(text=Message.no_events, secondary_text="", tertiary_text=""))
            
        return
            
    def on_pre_leave(self, *args):
        self.ids.events_container.clear_widgets()
        
        return