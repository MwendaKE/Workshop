from kivy.app import App
from kivy.properties import StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBody 
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from modules.datamanager import Book, Music, Quote, Poem, Diary, Event, Article, Clip, Task, Category

DB = "SuperMe.db"


class MenuRightLabel(IRightBody, MDLabel):
    pass
    
    
class MenuListItem(OneLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super(MenuListItem, self).__init__(**kwargs)
        
   
class MenuContentDrawer(MDBoxLayout, Screen):
    def __init__(self, **kwargs):
        super(MenuContentDrawer, self).__init__(**kwargs)
        self.app = App.get_running_app()
    
     #------- SWITCH SCREENS ------
     
     # -- People --
     
    def open_authors_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "authors"
        
        return
        
    def open_artists_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "artists"
        
        return
        
    def open_poets_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "poets"
        
        return 
        
    def open_writers_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "writers"
        
        return 
        
    def open_categories_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "categories"
        
        return 
        
    def open_genres_window(self):
        self.app.root.ids.side_menu.set_state("close")
        self.app.root.ids.manager.current = "genres"
        
        return 
        
    # -- Applications --
    
    def open_books_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "books"
        
        return
        
    def open_music_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "music"
        
        return
        
    def open_quotes_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "quotes"
        
        return
        
    def open_diaries_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "diaries"
        
        return
        
    def open_clips_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "clips"
        
        return
        
    def open_poems_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "poems"
        
        return
        
    def open_tasks_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "tasks"
        
        return
        
    def open_articles_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "articles"
        
        return
        
    def open_events_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "events"
        
        return
        
    def open_about_window(self):
        app = App.get_running_app()
        
        app.root.ids.side_menu.set_state("close")
        app.root.ids.manager.current = "about"
        
        return
       
       
    #------- COUNTS ------
     
    def get_books_count(self):
        bo = Book(DB)
        
        return bo.get_books_count()
        
    def get_music_count(self):
        mo = Music(DB)
        
        return mo.get_music_count()
        
    def get_genres_count(self):
        mo = Music(DB)
        
        return mo.get_genres_count()
        
    def get_quotes_count(self):
        qo = Quote(DB)
        
        return qo.get_quotes_count()
        
    def get_poems_count(self):
        po = Poem(DB)
        
        return po.get_poems_count()
        
    def get_poets_count(self):
        po = Poem(DB)
        
        return po.get_poets_count()
        
    def get_tasks_count(self):
        to = Task(DB)
        
        return to.get_tasks_count()
        
    def get_diaries_count(self):
        do = Diary(DB)
        
        return do.get_entry_count()
        
    def get_events_count(self):
        eo = Event(DB)
        
        return eo.get_events_count()
        
    def get_articles_count(self):
        ao = Article(DB)
        
        return ao.get_articles_count()
        
        #--HELPERS
    
    def get_authors_count(self):
        ao = Book(DB)
        qo = Quote(DB)
        
        authors_count = str(int(ao.get_bookauthors_count()) + int(qo.get_authors_count()))
        
        return authors_count
    
    def get_categs_count(self):
        co = Category(DB)
        
        return co.get_categories_count()
        
    def get_artists_count(self):
        ao = Music(DB)
        
        return ao.get_artists_count()
        
    def get_writers_count(self):
        wo = Article(DB)
        
        return wo.get_writers_count()
        
    def get_clips_count(self):
        co = Clip(DB)
        
        return co.get_clips_count()
        
    def get_authors(self):
        pass
        
        
        
        
        
        