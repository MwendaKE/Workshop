from kivymd.uix.navigationdrawer import MDNavigationDrawer

from modules.datamanager import Book, Music, Quote, Poem, Diary, Event, Article, Clip, Task, Category

DB = "SuperMe.db"

class SideMenu(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super(SideMenu, self).__init__(**kwargs)
        self.type = "standard"
        
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
        
        
        
        