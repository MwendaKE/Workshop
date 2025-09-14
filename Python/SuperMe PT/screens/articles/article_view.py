from kivy.app import App

from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty

from modules.datamanager import Article
from modules.helpers import ContentLabelView, show_error, show_info, confirm_delete
from modules.definations import AppColor, Message, Error, Title

from kivy.clock import Clock

from collections import deque
            
import re

DB = "SuperMe.db"


class ArticleViewWindow(Screen):
    article_title_label = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(ArticleViewWindow, self).__init__(**kwargs)
        self.article_patt = "\[b\](.+)\[\/b\] by \[b\](.+)\[\/b\]"
        
    def delete_article(self):
        query = re.search(self.article_patt, self.article_title_label.text)
        
        if query:
            atitle = query.group(1)
            
            txt = f"Delete [color=EF8887][b]{atitle}[/b][/color] from articles?"
            
            confirm_delete(Title.delete_article, txt, "Article", atitle, "")
            
        else:
            show_error(Title.delete_article, Error.query_patt_error)
        
    def about_article(self):
        query = re.search(self.article_patt, self.article_title_label.text)
        
        if query:
            atitle = query.group(1)
            
            artobj = Article(DB)
            categ, writer, date = artobj.about_query(atitle)
            
            text = f"Article Writer:\n[color={AppColor.green_tc}]{writer}[/color]\nCategory:\n[color={AppColor.green_tc}]{categ}[/color]\nDate Written:\n[color={AppColor.green_tc}]{date}[/color]"
            
            text_list = [{"text": t} for t in text.split("\n")]
            
            show_info(Title.article_information, text_list)

        else:
            show_error(Title.article_information, Error.query_patt_error)
       
     
class ArticleContentView(Screen):
    def __init__(self, artitle, **kwargs):
        super(ArticleContentView, self).__init__(**kwargs)
        self.artitle = artitle
        Clock.schedule_once(self.show_content, 0.1)
      
    def show_content(self, *args):
        app = App.get_running_app()
        app.root.ids.manager.get_screen('articleview').ids.article_content_container.clear_widgets()
        
        art_patt = "\[b\](.+)\[\/b\]"
        
        writer = "Undefined"
        
        query = re.search(art_patt, self.artitle)
      
        if query:
            atitle = query.group(1)
            artobj = Article(DB)
            
            try:
                body, writer, ref = artobj.load_article(atitle)
                art_content = deque()
                    
                for paragraph in body.split("\n\n"):
                    art_content.append(paragraph)

                if ref:
                    art_content.append(f"[b]References:[/b] \n\n{ref}")
                  
            except Exception as e:
                art_content = f"{Error.article_view_error}: {e}"
                  
        else:
            art_content = "Undefined article."
            
        app.root.ids.manager.get_screen('articleview').ids.article_titlelabel.text = f"{self.artitle} by [b]{writer}[/b]"
        
        if type(art_content) == deque:
            for paragraph in art_content:
                app.root.ids.manager.get_screen('articleview').ids.article_content_container.add_widget(ContentLabelView(text=paragraph))
                
        else:
            app.root.ids.manager.get_screen('articleview').ids.article_content_container.add_widget(ContentLabelView(text=art_content))
            
        app.root.ids.manager.current = "articleview"
            
            
        