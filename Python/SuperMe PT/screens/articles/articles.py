from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineIconListItem

from modules.datamanager import Article
from modules.definations import Message

from collections import deque

DB = "SuperMe.db"
 
 
class ThreeLineArticleView(ThreeLineIconListItem):
    def __init__(self, **kwargs):
        super(ThreeLineArticleView, self).__init__(**kwargs)
        
    def on_release(self):
        from screens.articles.article_view import ArticleContentView
        
        if not Message.no_articles in self.text:
            ArticleContentView(self.text)
    
        return
        
                                                      
class ArticleWindow(Screen):
    def __init__(self, **kwargs):
        super(ArticleWindow, self).__init__(**kwargs)
       
    def on_pre_enter(self, *args):
        artobj = Article(DB)
        articles = artobj.load_articles()
        
        if articles:
            article_count = artobj.get_articles_count()
        
            self.data = deque()
            
            for title, categ, writer, datew in articles:
                self.data.append((f"[b]{title}[/b]", f"[i]{categ}[/i]", f"[i]By {writer}, {datew}[/i]"))
                
            self.ids.article_count.text = str(article_count)
            
            for title, categ, datew in self.data:
                self.ids.articles_container.add_widget(ThreeLineArticleView(text=title, secondary_text=categ, tertiary_text=datew))
         
        else:
            self.ids.articles_container.add_widget(ThreeLineArticleView(text=f"{Message.no_articles}", secondary_text="None", tertiary_text="None"))
        
        return
        
    def on_pre_leave(self, *args):
        self.ids.articles_container.clear_widgets()
        
        return