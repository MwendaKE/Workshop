from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.clock import Clock

from modules.datamanager import Quote, Book, Clip

import random
from collections import deque

DB = "SuperMe.db"

class CarouselLabel(Label):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        

class CarouselWidget(Carousel):
    def __init__(self, **kwargs):
        super(CarouselWidget, self).__init__(**kwargs)
        self.build_corousel()
        
        Clock.schedule_interval(self.load_next, 5)
    
    def build_corousel(self):
        data = self.fetch_data()
        
        random.shuffle(data)
        
        for title, author, body in data:
            if title == "":
                text = f'[color=#FFFFFF]{body}[/color] [color=83AE74] ~ [i]{author}[/i][/color]'
            
            else:
                text = f'[color=#FFFFFF]{body}[/color], [i][color=EF8887]{title}[/color], [color=83AE74]{author}[/color][/i]'
                
            
            self.add_widget(CarouselLabel(text))
           
    def fetch_data(self):
        data = deque([("Atomic Habits",
                        "James Clear",
                        "One of the most practical ways to eliminate a bad habit is to reduce exposure to the cue that causes it. Make the cues of your good habits obvious and the cues of your bad habits invisible."
                        ),
                        ("",
                        "Aristotle",
                        "Happiness is the meaning and the purpose of life, the whole aim and end of human existence."
                        )])
           
        # --- QUOTES ---
        
        qo = Quote(DB)
        quotes = qo.load_quotes_for_carousel()
        
        if quotes:
            random.shuffle(quotes)
            
            if len(quotes) > 100:
                quotes = quotes[0:100]
                
            for categ, author, quot in quotes:
                quote = ("", author, quot)
                data.append(quote)
                
        # --- BOOKS ---
               
        bo = Book(DB)
        books = bo.load_books_for_carousel()
   
        if books:
            random.shuffle(books)
            
            if len(books) > 100:
                books = books[0:100]
                
            for title, author, review in books:
                reviews = review.split("\n\n")
                
                random.shuffle(reviews)
                
                for rv in reviews:
                    if len(rv) > 50 and len(rv) < 300:
                        book = (title, author, rv)
                        data.append(book)
                        
                    else:
                        break
                        
        co = Clip(DB)
        clips = co.load_clips()
        
        if clips:
            random.shuffle(clips)
            
            if len(clips) > 50:
                clips = clips[0:50]
                
            for clip, writer, srctitle, srcname in clips:
                if len(clip) < 300:
                    clp = (f"{srcname}: {srctitle}", writer, clip)
                    data.append(clp)
                
        return data
        