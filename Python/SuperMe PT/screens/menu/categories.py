from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem
from modules.datamanager import Category

DB = "SuperMe.db"


class OneLineCategoriesView(OneLineIconListItem):
    def __init__(self, **kwargs):
        super(OneLineCategoriesView, self).__init__(**kwargs)
        
        
class CategoryWindow(Screen):
    def __init__(self, **kwargs):
        super(CategoryWindow, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        self.ids.categs_container.clear_widgets()
        
        ao = Category(DB)
        categories = ao.load_categories()
        
        self.ids.categs_count.text = str(len(categories))
        
        for categ in categories:
            self.ids.categs_container.add_widget(OneLineCategoriesView(text=categ))
            
        return