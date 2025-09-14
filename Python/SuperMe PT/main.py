from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase


Window.softinput_mode = "below_target"
#LabelBase.register(name​=​"./assets/fonts/The_Winter.ttf")
 

class SupermeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        
        return Builder.load_file("./templates/other/screen_manager.kv")
   
    def open_side_menu(self):
        app = App.get_running_app()
        app.root.ids.side_menu.set_state("open")
        
        return
        
    def open_search_window(self):
        app = App.get_running_app()
        app.root.ids.manager.current = "searchquery"
        
        return
         
                                                                                       
if __name__ == '__main__':
    app = SupermeApp()
    from modules import bugs
    bugs.fixBugs()
    app.run()