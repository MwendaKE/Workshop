from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from modules.datamanager import Book, Music, Quote, Event, Diary, Task, Clip, Article, Poem
from modules.helpers import ContentLabelView, show_info, show_message

from kivy.clock import Clock
from collections import deque

import re
import random

DB = "SuperMe.db"
        

class SearchWindow(Screen):
    query = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(SearchWindow, self).__init__(**kwargs)
       
    def search(self, *args):
        self.ids.search_results_container.clear_widgets()
    
        if self.query.text and not self.query.text.isspace():
            import re
            
            queries = re.split(",", self.query.text)
            
            all_search_rsts = deque()
            
            #--- BOOKS ---
            
            booksobj = Book(DB)
            bks_search_rsts = booksobj.search_general(queries)
            
            bkauthors_search_rsts = booksobj.search_in_book_authors(queries)
            
            #--- MUSIC ---
            
            musicobj = Music(DB)
            msc_search_rsts = musicobj.search_general(queries)
            
            artists_search_rsts = musicobj.search_in_artists(queries)
            
            #--- QUOTES ---
            
            quotesobj = Quote(DB)
            qts_search_rsts = quotesobj.search_general(queries)
            
            qtauthors_search_rsts = quotesobj.search_in_quote_authors(queries)
            
            #--- EVENTS ---
            
            eventsobj = Event(DB)
            ets_search_rsts = eventsobj.search_general(queries)
       
            #--- DIARIES ---
            
            diaryobj = Diary(DB)
            drs_search_rsts = diaryobj.search_general(queries)
            
            #--- TASKS ---
            
            taskobj = Task(DB)
            tks_search_rsts = taskobj.search_general(queries)
            
            #--- CLIPS ---
            
            clipobj = Clip(DB)
            cls_search_rsts = clipobj.search_general(queries)
            
            #--- ARTS ---
            
            artobj = Article(DB)
            ats_search_rsts = artobj.search_general(queries)
            
            writers_search_rsts = artobj.search_in_writers(queries)
            
            #--- POEM ---
            
            pmobj = Poem(DB)
            pms_search_rsts = pmobj.search_general(queries)
            
            poets_search_rsts = pmobj.search_in_poets(queries)
            
            
            ##====>
            
            all_search_rsts.extend(bks_search_rsts)
            all_search_rsts.extend(msc_search_rsts)
            all_search_rsts.extend(qts_search_rsts)
            all_search_rsts.extend(ets_search_rsts)
            all_search_rsts.extend(drs_search_rsts)
            all_search_rsts.extend(tks_search_rsts)
            all_search_rsts.extend(cls_search_rsts)
            all_search_rsts.extend(ats_search_rsts)
            all_search_rsts.extend(pms_search_rsts)
            
            all_search_rsts.extend(artists_search_rsts)
            all_search_rsts.extend(writers_search_rsts)
            all_search_rsts.extend(bkauthors_search_rsts)
            all_search_rsts.extend(poets_search_rsts)
            all_search_rsts.extend(qtauthors_search_rsts)
            
            random.shuffle(all_search_rsts)
            
            if all_search_rsts:
                for rst in all_search_rsts:
                   self.ids.search_results_container.add_widget(ContentLabelView(text=rst))
                   
                self.ids.result_count.text = f"Search results: [color=#83AE74]{str(len(all_search_rsts))}[/color]"
            
            else:
            	show_message("Results", "No results found")
            	
            	self.ids.result_count.text = "Search results: 0"
       
        else:
            show_message("Search", f"Nothing to search")
            
            self.ids.result_count.text = "Search results: 0"
            
        return
            
    def clear_search_container(self):
        self.ids.search_input.text = ""
        self.ids.result_count.text = "Search results: 0"
        self.ids.search_results_container.clear_widgets()
        
        return 
            