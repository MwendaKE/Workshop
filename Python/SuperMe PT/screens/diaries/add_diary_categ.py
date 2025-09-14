from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty

from modules.datamanager import Category
from modules.helpers import show_error
from modules.definations import Error, Text, Title


DB = "SuperMe.db"


class AddDiaryCategWindow(Screen):
    category = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AddDiaryCategWindow, self).__init__(**kwargs)
        self.categdata = Text.select_category
        
    def add_category(self):
        if self.category.text == "" or self.category.text.isspace():
            show_error(Title.add_category, Error.required)
            
        else:
            self.categdata = self.category.text.title()
            
            categobj = Category(DB)
            allcategs = categobj.load_categories_lower()
            
            if self.categdata.lower() in allcategs:
                show_error(Title.add_category, Error.category_exists)
                
            else:
                categobj.add_category(self.categdata)
                
                self.category.text = ""
                
            self.refresh_all_categories()
                
    def refresh_all_categories(self):
        ao = Category(DB)
        
        self.manager.get_screen('addiary').ids.diary_categ_spinner.values = ao.load_categories()
        self.manager.get_screen('addiary').ids.diary_categ_spinner.text = self.categdata
        
        self.manager.current = "addiary"
    