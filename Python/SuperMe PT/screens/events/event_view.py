from kivy.app import App

from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty

from modules.datamanager import Event
from modules.helpers import ContentLabelView, show_error, show_info, confirm_delete, show_message
from modules.definations import AppColor, Message, Error, Title
from modules.verifier import verify_event_attendance

from kivy.clock import Clock

import re
from collections import deque


DB = "SuperMe.db"


class EventViewWindow(Screen):
    ev_title = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(EventViewWindow, self).__init__(**kwargs)
        self.event_patt = "\[b\](.+)\[/b\]"
        Clock.schedule_once(self.edit_event, 0.1)
      
    def edit_event(self, *args):
        query = re.search(self.event_patt, self.ev_title.text)
        
        if query:    
            etitle = query.group(1)
            
            eventobj = Event(DB)
            
            try:
                eid, edate, etime, venue, addr, budg, notes, att = eventobj.edit_query(etitle)
                
                attendance = verify_event_attendance(att)
                
                app = App.get_running_app()
      
                app.root.ids.manager.get_screen('editevent').ids.event_id_label.text = str(eid)
                app.root.ids.manager.get_screen('editevent').ids.event_name_input.text = etitle
                app.root.ids.manager.get_screen('editevent').ids.event_date_input.text = edate
                app.root.ids.manager.get_screen('editevent').ids.event_time_input.text = etime
                app.root.ids.manager.get_screen('editevent').ids.event_venue_input.text = venue
                app.root.ids.manager.get_screen('editevent').ids.event_address_input.text = addr
                app.root.ids.manager.get_screen('editevent').ids.event_budget_input.text = budg
                app.root.ids.manager.get_screen('editevent').ids.event_notes_input.text = notes
                app.root.ids.manager.get_screen('editevent').ids.event_att_spinner.text = attendance
               
                app.root.ids.manager.current = "editevent"
    
            except Exception as e:
                show_error(Title.edit_event, Error.event_edit_error + str(e))
            
        else:
            pass
            
    def delete_event(self):
        query = re.search(self.event_patt, self.ev_title.text)
        
        if query:
            etitle = query.group(1)
            
            txt = f"Delete [color=EF8887][b]{etitle}[/b][/color] from events?"
            
            confirm_delete(Title.delete_event, txt, "Event", etitle, "")
            
        else:
            show_error(Title.delete_event, Error.query_patt_error)
        
    def about_event(self):
        import humanize
        from modules.helpers import calc_true_datetime
        from datetime import datetime
        
        query = re.search(self.event_patt, self.ev_title.text)
    
        if query:
            etitle = query.group(1)
            
            eventobj = Event(DB)
            eid, date, time, venue, addr, budget, attended = eventobj.about_query(etitle)
            
            event_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H%M").strftime("%a, %d %b %Y, %I:%M %p")
            human_time = humanize.naturaltime(calc_true_datetime(date, time))
            human_money = humanize.intcomma(budget)
           
            text = f"Event ID:\n[color={AppColor.green_tc}]{str(eid).zfill(4)}[/color]\nEvent Name:\n[color={AppColor.green_tc}]{etitle}[/color]\nVenue, Address:\n[color={AppColor.green_tc}]{venue}, {addr}[/color]\nDatetime:\n[color=AppColor.green_tc]{event_datetime}[/color]\nBudget:\n[color={AppColor.green_tc}]Ksh.{human_money}[/color]"
            
            text_list = [{"text": t} for t in text.split("\n")]
            
            show_info(Title.event_description, text_list)

        else:
            show_error(Title.about_event, Error.query_patt_error)
       
     
class EventContentView(Screen):
    def __init__(self, eventkey, **kwargs):
        super(EventContentView, self).__init__(**kwargs)
        self.event_key = eventkey
        self.app = App.get_running_app()
        
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        self.app.root.ids.manager.get_screen("eventview").ids.event_content_container.clear_widgets()
        
        event_patt = "\[b\](.+)\[/b\]"
        
        query = re.search(event_patt, self.event_key)
        
        if query:
            query = query.group(1)
             
            eventobj = Event(DB)
            
            try:
                event_content = eventobj.load_event(query)
                
                if event_content:
                    from collections import deque
                    
                    content_list = deque()
                    
                    for content in event_content.split("\n\n"):
                        content_list.append(content)
                        
                else:
                    content_list = Message.no_event_content
                    
            except Exception as error:
                content_list = "[color=FF0000]This content cannot be displayed!;[/color]"
           
        else:
            content_list = "[color=FF0000]This content cannot be displayed![/color]"
        
        self.app.root.ids.manager.get_screen("eventview").ids.event_titlelabel.text = self.event_key
                
        if type(content_list) == deque:
            for paragraph in content_list:
                self.app.root.ids.manager.get_screen("eventview").ids.event_content_container.add_widget(ContentLabelView(text=paragraph))
            
        else:
            self.app.root.ids.manager.get_screen("eventview").ids.event_content_container.add_widget(ContentLabelView(text=content_list))
        
        self.app.root.ids.manager.current = "eventview"
      
     