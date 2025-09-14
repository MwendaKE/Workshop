from kivy.app import App
        
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog

from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.spinner import Spinner    
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, StringProperty

from modules.datamanager import Article, Category, Book, Poem, Music, Diary, Task, Event
from modules.definations import AppColor, Title, Error

import datetime

DB = "SuperMe.db"


# ---- RECYCLE VIEWS ----

class RecycleLabelView(RecycleView):
    pass
    
  
class RecycleContentView(RecycleView):
    pass
    

# ---- GENERAL WIDGETS ----
    
class ContentLabelView(MDLabel):
    def __init__(self, **kwargs):
        super(ContentLabelView, self).__init__(**kwargs)
        
 
class GeneralCategorySpinner(Spinner):
    def __init__(self, **kwargs):
        super(GeneralCategorySpinner, self).__init__(**kwargs)
        self.add_spinner_items()
        
    def add_spinner_items(self):
        categobj = Category(DB)
        self.values = categobj.load_categories() 
        

class MessagePopup(Popup):
    title = StringProperty("")
    message = ObjectProperty(None)
    
    def __init__(self, title, text, **kwargs):
        super(MessagePopup, self).__init__(**kwargs)
        self.title = title
        self.message.data = [{'text': text}]  
   
       
class WarningPopup(Popup):
    title = StringProperty("")
    message = ObjectProperty(None)
    
    def __init__(self, title, message, **kwargs):
        super(WarningPopup, self).__init__(**kwargs)
        self.title = title
        self.message.data = [{"text": message}]
        
    def accept_warning(self):
        return True
        
    def cancel_warning(self):
        return False
        
        
class ErrorPopup(Popup):
    title = StringProperty("")
    message = ObjectProperty(None)
    
    def __init__(self, title, text, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        self.title = title
        self.message.data = [{'text': text}]  
   
             
class InfoPopup(Popup):
    title = StringProperty("")
    message = ObjectProperty(None)
    
    def __init__(self, title, content_list, **kwargs):
        super(InfoPopup, self).__init__(**kwargs)
        self.title = title
        self.message.data = content_list
       
          
class DeletePopup(Popup):
    title = StringProperty("")
    text = StringProperty("")
    message = ObjectProperty(None)
    obj = StringProperty("")
    
    def __init__(self, title, text, obj, bktitle, bkauthor, **kwargs):
        super(DeletePopup, self).__init__(**kwargs)
        self.title = title
        self.message.data = [{"text": text}]
        self.obj = obj
        self.objtitle = bktitle
        self.objauthor = bkauthor
        self.app = App.get_running_app()
        
    def accept_delete(self):
        if self.obj == "Poem":
            obj = Poem(DB)
            
            try:
                obj.delete_query(self.objtitle, self.objauthor)
                
                self.app.root.ids.manager.current = "poems"
                
            except Exception as e:
                show_error(Title.delete_poem, Error.poem_delete_error)
              
        elif self.obj == "Book":
            obj = Book(DB)
            
            try:
                obj.delete_query(self.objtitle, self.objauthor)
                
                self.app.root.ids.manager.current = "books"
                
            except Exception as e:
                show_error(Title.delete_book, Error.cannot_delete_book)
           
        elif self.obj == "Music":
            obj = Music(DB)
            
            try:
                obj.delete_query(self.objtitle, self.objauthor)
                
                self.app.root.ids.manager.current = "music"
                
            except Exception as e:
                show_error(Title.delete_music, Error.cannot_delete_music)
                
        elif self.obj == "Diary":
            obj = Diary(DB)
            
            try:
                obj.delete_query(self.objtitle)
                
                self.app.root.ids.manager.current = "diaries"
                
            except Exception as e:
                show_error(Title.delete_diary, Error.cannot_delete_diary)
        
        elif self.obj == "Task":
            obj = Task(DB)
            
            try:
                obj.delete_query(self.objtitle)
                
                self.app.root.ids.manager.current = "tasks"
                
            except Exception as e:
                show_error(Title.delete_task, Error.cannot_delete_task)
                
        elif self.obj == "Event":
            obj = Event(DB)
            
            try:
                obj.delete_query(self.objtitle)
                
                self.app.root.ids.manager.current = "events"
                
            except Exception as e:
                show_error(Title.delete_event, Error.event_delete_error)
        
        elif self.obj == "Article":
            obj = Article(DB)
            
            try:
                obj.delete_query(self.objtitle)
                
                self.app.root.ids.manager.current = "articles"
                
            except Exception as e:
                show_error(Title.delete_article, Error.article_delete_error)
                
        else:
            show_message("Delete Object", "This is not an object.")
           
        return True
            
    def cancel_delete(self):
        return False
        
        
    
class DeletePoemDialog(Popup):
    message = ObjectProperty(None)
    
    def __init__(self, message, pmtitle, poet, **kwargs):
        super(DeletePoemDialog, self).__init__(**kwargs)
        self.title = Title.delete_poem
        self.message.data = [{"text": message}]
        self.pmtitle = pmtitle
        self.poet = poet
        
        self.app = App.get_running_app()
        
    def accept_delete(self):
        obj = Poem(DB)
        
        try:
            obj.delete_poem(self.pmtitle, self.poet)
                
            self.app.root.ids.manager.current = "poems"
                
        except Exception as e:
            show_error(Title.delete_poem, Error.poem_delete_error)
    
    def cancel_delete(self):
        return False
               


class InputTextEdit(TextInput):
    def _hide_cut_copy_paste(self, win=None):
        bubble = self._bubble
        if not bubble:
            return
            #bubble_hide()
            
       
# ---- POPUP FUNCTIONS ----
   
def show_message(title, message):
    msg = MessagePopup(title, message)
    msg.open()
    
def show_warning(title, message):
    msg = MessagePopup(title, message)
    msg.open()
             
def show_error(title, message):
    error = ErrorPopup(title, message)
    error.open()
    
def show_info(title, message):
    error = InfoPopup(title, message)
    error.open()
    
def confirm_delete(title, text, obj, bktitle, bkauthor):
    delete = DeletePopup(title, text, obj, bktitle, bkauthor)
    delete.open()
    
def confirm_delete_poem(msg, ptitle, poet):
    delete = DeletePoemDialog(msg, ptitle, poet)
    delete.open()
    
# ---- DATETIME FUNCTIONS ----
    
def calc_true_time(rdate):
    datelst = rdate.split("-")
    dt_time = datetime.datetime(int(datelst[0]), int(datelst[1]), int(datelst[2])) 
        
    return dt_time
        
def calc_true_date(rdate):
    datelst = rdate.split("-")
    dt_date = datetime.date(int(datelst[0]), int(datelst[1]), int(datelst[2])) 
        
    return dt_date 
        
def calc_days_active(edate):
    edate = calc_true_date(edate)
    today = datetime.date.today()
        
    rem_time = (edate - today).days
        
    return rem_time
    
def calc_true_datetime(date, time):
    datelst = date.split("-")
    trtime = datetime.datetime(int(datelst[0]), int(datelst[1]), int(datelst[2]), int(time[:2]), int(time[2:])) 
        
    return trtime
    
   
# ---- GENERAL FUNCTIONS ----