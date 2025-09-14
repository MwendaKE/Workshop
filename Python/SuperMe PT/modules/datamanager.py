import re
import sqlite3
from collections import deque


def regexp(expr, item):
    reg = re.compile(expr, re.I|re.M)
    return reg.search(item) is not None


class Clip(object):
    def __init__(self, database, **kwargs):
        super(Clip, self).__init__(**kwargs)
        self.database = database
        self.create_table_clips()
       
    def create_table_clips(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS clips (
                                   clip TEXT NOT NULL,
                                   writer TEXT NOT NULL,
                                   source_title TEXT NOT NULL,
                                   source_type TEXT NOT NULL);
                         """)
                         
    def add_clip(self, clip, writer, stitle, stype):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO clips (clip, writer, source_title, source_type) VALUES (?, ?, ?, ?);", (clip, writer, stitle, stype))
            
    def load_clips(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT clip, writer, source_title, source_type FROM clips ORDER BY writer ASC;")
            clips = cursor.fetchall()
            
        return clips
     
    def get_clips_count(self):
        return str(len(self.load_clips()))
        
    def search_general(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT clip, writer, source_title, source_type FROM clips;")
            search_rsts = cursor.fetchall()
            
        for clip, writer, stitle, stype in search_rsts:
            for word in words:
                if word.lower() in clip.lower():
                    text = f"{clip}, [i][color=#26DDC7]{writer}[/color], [color=#83AE74]{stype}: {stitle}[/color][/i]"
                    results.append(text)
        
        return results
        

class Article(object):
    def __init__(self, database, **kwargs):
        super(Article, self).__init__(**kwargs)
        self.database = database
        self.create_table_articles()
        self.create_table_writers()
        
    def create_table_articles(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS articles (
                                   title TEXT NOT NULL,
                                   category TEXT NOT NULL,
                                   body TEXT NOT NULL,
                                   writer TEXT NOT NULL,
                                   date_written TEXT NOT NULL,
                                   reference TEXT NOT NULL,
                                    FOREIGN KEY (writer) REFERENCES article_writers (writer_name) ON UPDATE SET NULL ON DELETE SET NULL);
                         """) 
                         
    def create_table_writers(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS article_writers (
                                   writer_name TEXT(50) NOT NULL,
                                   country TEXT(100) NOT NULL,
                                   description TEXT NULL);
                         """)   

                                                                                                              
    def add_article(self, title, categ, body, writer, datew, ref):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO articles (title, category, body, writer, date_written, reference) VALUES (?, ?, ?, ?, ?, ?);", (title, categ, body, writer, datew, ref))
            
    def add_article_writer(self, name, country, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO article_writers (writer_name, country, description) VALUES (?, ?, ?);", (name, country, desc))
         
    def load_articles(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, category, writer, date_written FROM articles ORDER BY date_written DESC;")
            articles = cursor.fetchall()
            
        return articles
        
    def load_writers(self):
        writers = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT writer_name FROM article_writers ORDER BY writer_name ASC;")
            writers_data = cursor.fetchall()
            
            for writer in writers_data:
                writers.append(writer[0])
            
        return writers
        
    def load_writers_lower(self):
        writers = set()
        
        store = self.load_writers()
        
        for writer in store:
            writers.add(writer.lower())  
            
        return writers   
        
    def get_writers_count(self):
        return str(len(self.load_writers()))
        
    def get_writer_details(self, wwriter):
        writers = set()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT country, description FROM article_writers WHERE writer_name = ?;", (wwriter,))
            writer_data = cursor.fetchone()
            
        return writer_data
        
    def get_articles_count(self):
        return str(len(self.load_articles()))
        
    def edit_query(self, atitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, category, body, writer, date_written, reference FROM articles WHERE title = ?;", (atitle,))
            bte = cursor.fetchone()
            
        return bte
        
    def update_query(self, aid, title, categ, body, writer, date, ref):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE articles SET title = ?, category = ?, body = ?, writer = ?, date_written = ?, reference = ? WHERE rowid = ?;", (title, categ, body, writer, date, ref, aid))
         
    def load_article(self, atitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT body, writer, reference FROM articles WHERE title = ?;", (atitle,))
            task_content = cursor.fetchone()
            
        return task_content
        
    def delete_query(self, atitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM articles WHERE title = ?;", (atitle,))
     
    def about_query(self, atitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT category, writer, date_written FROM articles WHERE title = ?;", (atitle,))
            bte = cursor.fetchone()
            
            return bte 
            
    def search_general(self, words=[]):
        search_results = deque()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, body, writer FROM articles;")
            search_rsts = cursor.fetchall()
            
        for title, art, writer in search_rsts:
            art_list = re.split("\n\n", str(art))
            
            for result in art_list:
                for word in words:
                    if word.lower() in result.lower():
                        text = f"{result}, [i][color=26DDC7]Article:[/color] [color=EF8887]{title}[/color], [color=83AE74]{writer}[/color][/i]"
                        search_results.append(text)
                              
        return search_results
        
    def search_in_writers(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT writer_name, country, description FROM article_writers;")
            search_rsts = cursor.fetchall()
            
        for wrt, cnt, desc in search_rsts:
            rsts_list = re.split("\n\n", str(desc))
            
            for info in rsts_list:
                for word in words:
                    if word.lower() in info.lower():
                        text = f"[color=#83AE74]{wrt}[/color], [color=#26DDC7]Writer, [/color][color=#EF8887]{cnt}[/color]: [color=#EAC155]{info}[/color]"
                        results.append(text)
                
        return results
            
              
class Task(object):
    def __init__(self, database, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.database = database
        self.create_table_tasks()
        
    def create_table_tasks(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
                                   task_name TEXT NOT NULL,
                                   start_date TEXT NOT NULL,
                                   start_time TEXT NOT NULL,
                                   end_date TEXT NOT NULL,
                                   duration TEXT NOT NULL,
                                   category TEXT NOT NULL,
                                   success INTEGER NOT NULL,
                                   description TEXT NOT NULL);
                         """)
            
    def add_task(self, name, date1, ctime, date2, dur, categ, success, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO tasks (task_name, start_date, start_time, end_date, duration, category, success, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (name, date1, ctime, date2, dur, categ, success, desc))
            
    def load_tasks(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name, start_date, end_date, category, duration, success FROM tasks ORDER BY end_date DESC;")
            tasks = cursor.fetchall()
            
        return tasks
        
    def load_task(self, task):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT description FROM tasks WHERE task_name = ?;", (task,))
            task_content = cursor.fetchone()
            
        return task_content
        
    def load_tasks_names(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name FROM tasks;")
            tasks = cursor.fetchall()
            
        return tasks
    
    def load_tasks_date_duration(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT start_date, duration FROM tasks;")
            tasks = cursor.fetchall()
            
        return tasks
        
    def get_tasks_count(self):
        return str(len(self.load_tasks()))
        
    def update_active_status(self, status, ttitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET success = ? WHERE task_name = ?;", (status, ttitle))
         
    def get_completetasks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name FROM tasks WHERE success = 1;")
            count = len(cursor.fetchall())
        
        try:
            perc_count = int((count / int(self.get_tasks_count())) * 100)
        
        except:
            perc_count = 0
            
        return f"{perc_count}%"
        
    def get_failedtasks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name FROM tasks WHERE success = 0;")
            count = len(cursor.fetchall())
         
        try:   
            perc_count = int((count / int(self.get_tasks_count())) * 100)
        
        except:
            perc_count = 0
            
        return f"{perc_count}%"
        
    def get_activetasks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name FROM tasks WHERE success = 2;")
            count = len(cursor.fetchall())
           
        try: 
            perc_count = int((count / int(self.get_tasks_count())) * 100)
        
        except:
            perc_count = 0
            
        return f"{perc_count}%"
        
    def edit_query(self, ttitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, duration, category, description FROM tasks WHERE task_name = ?;", (ttitle,))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, tid, ttitle, categ, desc, state):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET task_name = ?, category = ?, description = ?, success = ? WHERE rowid = ?;", (ttitle, categ, desc, state, tid))
            
    def about_query(self, ttitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT start_date, start_time, end_date, duration, category, success FROM tasks WHERE task_name = ?;", (ttitle,))
            bte = cursor.fetchone()
            
            return bte 
            
    def delete_query(self, ttitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE task_name = ?;", (ttitle,))
     
    def search_general(self, words=[]):
        results = deque()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name, duration, description FROM tasks;")
            search_rsts = cursor.fetchall()
            
        for tn, dr, desc in search_rsts:
            tl_list = re.split("\n\n", str(desc))
            
            for tsk in tl_list:
                for word in words:
                    if word.lower() in tsk.lower():
                        text = f"{tsk}, [i][color=26DDC7]Task:[/color] [color=EF8887]{tn}[/color], [color=83AE74]{dr}[/color][/i]"
                        results.append(text)
                              
        return results
    
    
class Diary(object):
    def __init__(self, database, **kwargs):
        super(Diary, self).__init__(**kwargs)
        self.database = database
        self.create_table_diaries()
        
    def create_table_diaries(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS diaries (
                                   title TEXT NOT NULL,
                                   entry_date TEXT NOT NULL,
                                   entry_time TEXT NOT NULL,
                                   category TEXT NOT NULL,
                                   mood TEXT NOT NULL,
                                   description TEXT NOT NULL);
                         """)
                         
    def add_entry(self, title, date, time, categ, mood, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO diaries (title, entry_date, entry_time, category, mood, description) VALUES (?, ?, ?, ?, ?, ?);", (title, date, time, categ, mood, desc))
            
    def load_entries(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, entry_date, entry_time, mood FROM diaries ORDER BY entry_date DESC;")
            entries = cursor.fetchall()
            
        return entries
        
    def load_diary(self, diary):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT description FROM diaries WHERE title = ?;", (diary,))
            diary_content = cursor.fetchone()
            
        return diary_content
        
    def get_entry_count(self):
        count = len(self.load_entries())
        
        return str(count)
        
        
    def load_entries_titlecatmood(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, category, mood FROM diaries;")
            entries = cursor.fetchall()
            
        return entries
        
    def get_diary_id(self, dtitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid FROM diaries WHERE title = ?;", (dtitle,))
            bte = cursor.fetchone()
            
        return bte[0]
        
    def edit_query(self, dtitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, category, mood, description FROM diaries WHERE title = ?;", (dtitle,))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, did, dtitle, categ, mood, desc):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE diaries SET title = ?, category = ?, mood = ?, description = ? WHERE rowid = ?;",(dtitle, categ, mood, desc, did))
            
    def about_query(self, dtitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT entry_date, entry_time, category, mood FROM diaries WHERE title = ?;", (dtitle,))
            bte = cursor.fetchone()
            
            return bte 
           
    def delete_query(self, dtitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM diaries WHERE title = ?;", (dtitle,))

    def search_general(self, words=[]):
        results = deque()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, entry_date, description FROM diaries;")
            search_rsts = cursor.fetchall()
            
        for tt, dt, desc in search_rsts:
            dr_list = re.split("\n\n", str(desc))
            
            for dl in dr_list:
                for word in words:
                    if word.lower() in dl.lower():
                        text = f"{dl}, [i][color=26DDC7]Diaries:[/color] [color=EF8887]{tt}[/color], [color=83AE74]{dt}[/color][/i]"
                        results.append(text)
                              
        return results
    
    
class Event(object):
    def __init__(self, database, **kwargs):
        super(Event, self).__init__(**kwargs)
        self.database = database
        self.create_table_events()
        
    def create_table_events(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS events (
                                   event_name TEXT NOT NULL,
                                   event_date TEXT NOT NULL,
                                   event_time TEXT NOT NULL,
                                   event_notes TEXT NOT NULL,
                                   venue TEXT NOT NULL,
                                   address TEXT NOT NULL,
                                   budget TEXT NOT NULL,
                                   attended INTEGER NULL);
                         """)
                             
    def add_event(self, event, date, time, venue, address, notes, budget, att):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO events (event_name, event_date, event_time, venue, address, event_notes, budget, attended) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (event, date, time, venue, address, notes, budget, att))
            
    def load_event(self, event):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event_notes FROM events WHERE event_name = ?;", (event,))
            event = cursor.fetchone()
            
        return f"{event[0]}"
    
    def load_events(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event_name, event_date, event_time, venue, attended FROM events ORDER BY event_date DESC;")
            events = cursor.fetchall()
            
        return events
        
    def load_events_venuedate(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event_name, event_date, venue FROM events;")
            events = cursor.fetchall()
            
        return events
        
    def get_events_count(self):
        count = len(self.load_events())
        
        return str(count)
        
    def edit_query(self, etitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, event_date, event_time, venue, address, budget, event_notes, attended FROM events WHERE event_name = ?;", (etitle,))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, eid, etitle, edate, etime, venue, addr, budg, notes, att):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE events SET event_name = ?, event_date = ?, event_time = ?, venue = ?, address = ?, budget = ?, event_notes = ?, attended = ? WHERE rowid = ?;", (etitle, edate, etime, venue, addr, budg, notes, att, eid))
            
    def about_query(self, etitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, event_date, event_time, venue, address, budget, attended FROM events WHERE event_name = ?;", (etitle,))
            bte = cursor.fetchone()
            
            return bte 
            
    def delete_query(self, etitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM events WHERE event_name = ?;", (etitle,))
            
    def search_general(self, words=[]):
        results = deque()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT event_name, event_date, event_notes, venue FROM events;")
            search_rsts = cursor.fetchall()
            
        for en, dt, nts, ven in search_rsts:
            ev_list = re.split("\n\n", str(nts))
    
            for el in ev_list:
                for word in words:
                    if word.lower() in el.lower():
                        text = f"{el}, [i][color=26DDC7]Events:[/color] [color=E0C7EA]{en}[/color], [color=EF8887]{ven}[/color], [color=83AE74]{dt}[/color][/i]"
                        results.append(text)
                              
        return results
     
         
class Category(object):
    def __init__(self, database, **kwargs):
        super(Category, self).__init__(**kwargs)
        self.database = database
        self.create_table_all_categories()
        
    def create_table_all_categories(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS all_categories (
                                   category TEXT NOT NULL);
                         """) 
                         
    def add_category(self, categ):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO all_categories (category) VALUES (?);", (categ,))                         
      
    def load_categories(self):
        categories = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT category FROM all_categories ORDER BY category ASC;")
            categ_data = cursor.fetchall()
            
            for categ in categ_data:
                categories.append(categ[0])
            
        return categories
        
    def load_categories_lower(self):
        categories = set()
        store = self.load_categories()
        
        for categ in store:
            categories.add(categ.lower())
            
        return categories
        
    def get_categories_count(self):
        return str(len(self.load_categories()))
                    

class Music(object):
    def __init__(self, database, **kwargs):
        super(Music, self).__init__(**kwargs)
        self.database = database
        self.create_table_songs()
        self.create_table_songs_genres()
        self.create_table_songs_artists()
        
    def create_table_songs(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS songs (
                                   artist_name TEXT NOT NULL, 
                                   song_title TEXT NOT NULL, 
                                   lyries TEXT NOT NULL, 
                                   genre TEXT NOT NULL,
                                    FOREIGN KEY (artist_name) REFERENCES songs_artists (artist_name) ON UPDATE SET NULL ON DELETE SET NULL,
                                    FOREIGN KEY (genre) REFERENCES songs_genres (genre) ON UPDATE SET NULL ON DELETE SET NULL);
                         """)
                         
    def create_table_songs_genres(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS songs_genres (
                                   genre TEXT(20) NOT NULL);
                         """)
                         
    def create_table_songs_artists(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS songs_artists (
                                   artist_name TEXT(50) NOT NULL,
                                   country TEXT(100) NOT NULL,
                                   description TEXT NULL);
                         """)                 
                         
    def add_song(self, artist, title, lyries, genre):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO songs (artist_name, song_title, lyries, genre) VALUES (?, ?, ?, ?);", (artist, title, lyries, genre))
            
    def add_song_genre(self, genre):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO songs_genres (genre) VALUES (?);", (genre,))                         
          
    def add_song_artist(self, name, country, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO songs_artists (artist_name, country, description) VALUES (?, ?, ?);", (name, country, desc))
            
    def load_song(self, song):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT artist_name, lyries FROM songs WHERE song_title = ?;", (song,))
            song_pack = cursor.fetchone()
            
        return song_pack
        
    def load_songs(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT artist_name, song_title FROM songs ORDER BY song_title ASC;")
            songs = cursor.fetchall()
            
        return songs
    
    def load_genres(self):
        genres = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT genre FROM songs_genres ORDER BY genre ASC;")
            genre_data = cursor.fetchall()
            
            for genre in genre_data:
                genres.append(genre[0])
            
        return genres
        
    def load_genres_lower(self):
        genres = deque()
        store = self.load_genres()
        
        for genre in store:
            genres.append(genre.lower())
            
        return genres
        
    def get_genres_count(self):
        return str(len(self.load_genres()))
        
    def load_artists(self):
        artists = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT artist_name FROM songs_artists ORDER BY artist_name ASC;")
            artists_data = cursor.fetchall()
            
            for artist in artists_data:
                artists.append(artist[0])
            
        return artists

    def get_artists_count(self):
        return str(len(self.load_artists()))
        
    def get_artist_details(self, artist):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT country, description FROM songs_artists WHERE artist_name = ?;", (artist,))
            artist_data = cursor.fetchone()
        
        return artist_data
        
    def load_artists_lower(self):
        artists = set()
        store = self.load_artists()
        
        for artist in store:
            artists.add(artist.lower())
            
        return artists
        
    def get_music_count(self):
        count = len(self.load_songs())
        
        return str(count)
        
    def edit_query(self, mstitle, artist):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, artist_name, song_title, lyries, genre FROM songs WHERE song_title = ? and artist_name = ?;", (mstitle, artist))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, msid, artist, mstitle, genre, lyries):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE songs SET artist_name = '{artist}', song_title = '{mstitle}', genre = '{genre}', lyries = '{lyries}' WHERE rowid = {msid};")
            
    def about_query(self, mstitle, artist):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT  artist_name, song_title, genre FROM songs WHERE song_title = ? AND artist_name = ?;", (mstitle, artist))
            bte = cursor.fetchone()
            
            return bte 
            
    def delete_query(self, mstitle, artist):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM songs WHERE song_title = ? AND artist_name = ?;", (mstitle, artist))
            
    def search_general(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT artist_name, song_title, lyries FROM songs;")
            search_rsts = cursor.fetchall()
            
        for art, stt, lyr in search_rsts:
            rsts_list = re.split("\n\n", str(lyr))
            
            for rvt in rsts_list:
                for word in words:
                    if word.lower() in rvt.lower():
                        text = f"{rvt}, [i][color=26DDC7]Music:[/color] [color=EF8887]{stt}[/color], [color=83AE74]{art}[/color][/i]"
                        results.append(text)
                
        return results
        
    def search_in_artists(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT artist_name, country, description FROM songs_artists;")
            search_rsts = cursor.fetchall()
            
        for art, cnt, desc in search_rsts:
            rsts_list = re.split("\n\n", str(desc))
            
            for info in rsts_list:
                for word in words:
                    if word.lower() in info.lower():
                        text = f"[color=#83AE74]{art}[/color], [color=#26DDC7]Artist, [/color][color=#EF8887]{cnt}[/color]: [color=#EAC155]{info}[/color]"
                        results.append(text)
                
        return results
        

class Poem(object):
    def __init__(self, database, **kwargs):
        super(Poem, self).__init__(**kwargs)
        self.database = database
        self.create_table_poems()
        self.create_table_poets()
        
    def create_table_poems(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS poems (
                                   title TEXT NOT NULL,
                                   body TEXT NOT NULL,
                                   author TEXT NOT NULL,
                                    FOREIGN KEY (author) REFERENCES poets (poet_name) ON UPDATE SET NULL ON DELETE SET NULL);
                         """)
                         
    def create_table_poets(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS poets (
                                   poet_name TEXT(50) NOT NULL,
                                   country TEXT(100) NOT NULL,
                                   description TEXT NULL);
                         """)   
                         
    def add_poem(self, title, body, author):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO poems (title, body, author) VALUES (?, ?, ?);", (title, body, author))
            
    def add_poet(self, name, country, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO poets (poet_name, country, description) VALUES (?, ?, ?);", (name, country, desc))
             
    def load_poems(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, author FROM poems ORDER BY title ASC;")
            poems = cursor.fetchall()
            
        return poems
        
    def load_poem_content(self, title):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT body, author FROM poems WHERE title = ?;", (title,))
            review = cursor.fetchone()
           
        return review
        
    def edit_query(self, ptitle):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, body, author FROM poems WHERE title = ?;", (ptitle,))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, id, title, body, poet):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE poems SET title = ?, body = ?, author = ? WHERE rowid = ?;",(title, body, poet, id))
            
    def load_poets(self):
        poets = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT poet_name FROM poets ORDER BY poet_name ASC;")
            poets_data = cursor.fetchall()
            
            for poet in poets_data:
                poets.append(poet[0])
            
        return poets
        
    def get_poet_details(self, ppoet):
        poets = set()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT country, description FROM poets WHERE poet_name = ?;", (ppoet,))
            poet_data = cursor.fetchone()
            
        return poet_data
        
    def load_poets_lower(self):
        poets = set()
        store = self.load_poets()
        
        for poet in store:
            poets.add(poet.lower())
            
        return poets
   
    def get_poems_count(self):
        return str(len(self.load_poems()))
        
    def get_poets_count(self):
        return str(len(self.load_poets()))
        
    def delete_poem(self, ptitle, ppoet):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM poems WHERE title = ? AND author = ?;", (ptitle, ppoet))
        
    def about_poem(self):
        pass
        
    def search_general(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, body, author FROM poems;")
            search_rsts = cursor.fetchall()
            
        for title, body, author in search_rsts:
            if len(body) > 400:
                continue 
                
            pm_list = re.split("\n\n", str(body))
            
            for result in pm_list:
                for word in words:
                    if word.lower() in result.lower():
                        text = f"{result}, [i][color=26DDC7]Poem:[/color] [color=EF8887]{title}[/color], [color=83AE74]{author}[/color][/i]"
                        results.append(text)
                              
        
        return results
        
    def search_in_poets(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT poet_name, country, description FROM poets;")
            search_rsts = cursor.fetchall()
            
        for pt, cnt, desc in search_rsts:
            rsts_list = re.split("\n\n", str(desc))
            
            for info in rsts_list:
                for word in words:
                    if word.lower() in info.lower():
                        text = f"[color=#83AE74]{pt}[/color], [color=#26DDC7]Poet, [/color][color=#EF8887]{cnt}[/color]: [color=#EAC155]{info}[/color]"
                        results.append(text)
                
        return results
                
             
class Quote(object):
    def __init__(self, database, **kwargs):
        super(Quote, self).__init__(**kwargs)
        self.database = database
        self.create_table_quotes_authors()
        self.create_table_quotes()
    
    def create_table_quotes_authors(self):       
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS quotes_authors (
                                   author_name TEXT NOT NULL, 
                                   occupation TEXT NOT NULL, 
                                   country TEXT NOT NULL, 
                                   description TEXT NULL);
                         """)
                           
    def create_table_quotes(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS quotes (
                                   author TEXT NOT NULL,
                                   quote TEXT NOT NULL, 
                                   category TEXT NOT NULL, 
                                    FOREIGN KEY (author) REFERENCES quotes_authors (author_name) ON UPDATE SET NULL ON DELETE SET NULL,
                                    FOREIGN KEY (category) REFERENCES all_categories (category) ON UPDATE SET NULL ON DELETE SET NULL);
                         """) 
    
    def add_quote_author(self, author, occupation, country, desc):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO quotes_authors (author_name, occupation, country, description) VALUES (?, ?, ?, ?);", (author, occupation, country, desc))                                 
    
    def add_quote(self, author, quote, category):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO quotes (author, quote, category) VALUES (?, ?, ?);", (author, quote, category))
            
    def load_quotes(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author, quote FROM quotes ORDER BY author ASC;")
            quotes = cursor.fetchall()
            
        return quotes
        
    def get_author_details(self, author):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT occupation, country, description FROM quotes_authors WHERE author_name = ?;", (author,))
            author_data = cursor.fetchone()
            
            return author_data
            
    def load_quotes_for_carousel(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT category, author, quote FROM quotes;")
            quotes = cursor.fetchall()
            
        return quotes
            
    def load_authors(self):
        authors = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name FROM quotes_authors ORDER BY author_name ASC;")
            authors_data = cursor.fetchall()
            
            for author in authors_data:
                authors.append(author[0])
            
        return authors
        
    def load_quotes_authors_info(self):
        authors_info = set()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name, occupation, country, description FROM quotes_authors ORDER BY author_name ASC;")
            authors_data = cursor.fetchall()
            
            for author_info in authors_data:
                authors_info.add(author_info)
            
        return authors_info
        
    def load_authors_lower(self):
       authors = deque()
       store = self.load_authors()
       
       for author in store:
           authors.append(author.lower())
           
       return authors
       
    def get_authors_count(self):
       return str(len(self.load_authors()))
       
    def get_quotes_count(self):
        count = len(self.load_quotes())
        
        return str(count)
        
    def search_general(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author, quote FROM quotes;")
            search_rsts = cursor.fetchall()
            
        for auth, quote in search_rsts:
            for word in words:
                if word.lower() in quote.lower():
                    text = f"{quote}, [i][color=26DDC7]Quotes:[/color] [color=83AE74]{auth}[/color][/i]"
                    results.append(text)
        
        return results
        
    def search_in_quote_authors(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name, country, description FROM quotes_authors;")
            search_rsts = cursor.fetchall()
            
        for auth, cnt, desc in search_rsts:
            rsts_list = re.split("\n\n", str(desc))
            
            for info in rsts_list:
                for word in words:
                    if word.lower() in info.lower():
                        text = f"[color=#83AE74]{auth}[/color], [color=#26DDC7]Author, [/color][color=#EF8887]{cnt}[/color]: [color=#EAC155]{info}[/color]"
                        results.append(text)
                
        return results
        

class Book(object):
    def __init__(self, database, **kwargs):
        super(Book, self).__init__(**kwargs)
        self.database = database
        self.create_table_books_authors()
        self.create_table_books()
        
    def create_table_books_authors(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS books_authors (
                                   author_name TEXT(20) NOT NULL, 
                                   occupation TEXT(20) NOT NULL, 
                                   country TEXT(20) NOT NULL, 
                                   description TEXT NULL);
                         """)
             
    def create_table_books(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS books (
                                   author TEXT(20) NOT NULL,
                                   book_title TEXT(50) NOT NULL, 
                                   category TEXT(20) NOT NULL,
                                   isbn TEXT(20) NOT NULL,
                                   review TEXT NOT NULL,
                                   book_read INTEGER NOT NULL, 
                                   description TEXT NOT NULL,
                                    FOREIGN KEY (author) REFERENCES books_authors (author_name) ON UPDATE RESTRICT ON DELETE RESTRICT,
                                    FOREIGN KEY (category) REFERENCES all_categories (category) ON UPDATE SET NULL ON DELETE SET NULL);
                         """)
                           
    def add_book_author(self, author, occupation, country, desc):
         with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO books_authors (author_name, occupation, country, description) VALUES (?, ?, ?, ?);", (author, occupation, country, desc))                         
                         
    def add_book(self, author, title, category, isbn, review, about, read):
        with sqlite3.connect(self.database) as conn:
            conn.execute("INSERT INTO books (author, book_title, category, isbn, review, description, book_read) VALUES (?, ?, ?, ?, ?, ?, ?);", (author, title, category, isbn, review, about, read))            
                    
    def load_book_authors(self):
        authors = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name FROM books_authors ORDER BY author_name ASC;")
            authors_data = cursor.fetchall()
            
            for author in authors_data:
                authors.append(author[0].title())
           
        return authors
        
    def load_book_authors_info(self):
        authors_info = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name, occupation, country, description FROM books_authors ORDER BY author_name ASC;")
            authors_data = cursor.fetchall()
            
            for author_info in authors_data:
                authors_info.append(author_info)
           
        return authors_info
        
    def get_bookauthors_count(self):
        return str(len(self.load_book_authors()))
        
    def get_author_details(self, author):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT occupation, country, description FROM books_authors WHERE author_name = ?;", (author,))
            author_data = cursor.fetchone()
            
        return author_data
          
    def load_book_authors_lower(self):
        authors = deque()
        
        store = self.load_book_authors()
        
        for author in store:
            authors.append(author.lower())  
            
        return authors    
            
    def load_books(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author, book_title FROM books ORDER BY book_title ASC;")
            books = cursor.fetchall()
            
        return books
        
    def load_books_for_carousel(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title, author, review FROM books;")
            books = cursor.fetchall()
            
        return books
    
    def load_book_content(self, bookid):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title, author, review FROM books WHERE rowid = ?;", (bookid,))
            review = cursor.fetchone()
           
        return review
      
    def load_books_with_status(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, author, book_title, book_read FROM books ORDER BY book_title ASC;")
            books = cursor.fetchall()
            
        return books
        
    def get_books_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title FROM books;")
            count = len(cursor.fetchall())
            
        return f"{count}"
        
    def get_readbooks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title FROM books WHERE book_read = 1;")
            count = len(cursor.fetchall())
         
        try:   
            perc_count = int((count / int(self.get_books_count())) * 100)
        
        except:
            perc_count = 0
            
        return f"{perc_count}%"
        
    def get_readingbooks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title FROM books WHERE book_read = 2;")
            count = len(cursor.fetchall())
        
        try:
            perc_count = int((count / int(self.get_books_count())) * 100)
            
        except:
            perc_count = 0
        
        return f"{perc_count}%"
        
    def get_unreadbooks_count(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT book_title FROM books WHERE book_read = 0;")
            count = len(cursor.fetchall())
        
        try: 
            perc_count = int((count / int(self.get_books_count())) * 100)
            
        except:
            perc_count = 0
        
        return f"{perc_count}%"
      
    def edit_query(self, title, author):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, author, book_title, category, isbn, review, book_read, description FROM books WHERE book_title = ? and author = ?;", (title, author))
            bte = cursor.fetchone()
            
        return bte
       
    def update_query(self, bkid, author, new_title, category, isbn, review, book_read, description):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET author = ?, book_title = ?, category = ?, isbn = ?, review = ?, book_read = ?, description = ? WHERE rowid = ?;",(author, new_title, category, isbn, review, book_read, description, bkid))
            
    def about_query(self, title, author):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT description FROM books WHERE book_title = ? AND author = ?;", (title, author))
            bte = cursor.fetchone()
            
            return f"{bte[0]}"
            
    def delete_query(self, title, author):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE book_title = ? AND author = ?;", (title, author))
            
    def search_general(self, words=[]):
        search_results = deque()

        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author, book_title, review, description FROM books;")
            search_rsts = cursor.fetchall()
            
        for auth, bkt, rev, desc in search_rsts:
            rev_list = re.split("\n\n", str(rev))
            desc_list = re.split("\n\n", str(desc))
            
            rev_list.extend(desc_list)
            
            for result in rev_list:
                for word in words:
                    if word.lower() in result.lower():
                        text = f"{result}, [i][color=26DDC7]Books:[/color] [color=EF8887]{bkt}[/color], [color=83AE74]{auth}[/color][/i]"
                        search_results.append(text)
                              
        return search_results
        
    def search_in_book_authors(self, words=[]):
        results = deque()
        
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT author_name, country, description FROM books_authors;")
            search_rsts = cursor.fetchall()
            
        for auth, cnt, desc in search_rsts:
            rsts_list = re.split("\n\n", str(desc))
            
            for info in rsts_list:
                for word in words:
                    if word.lower() in info.lower():
                        text = f"[color=#83AE74]{auth}[/color], [color=#26DDC7]Author, [/color][color=#EF8887]{cnt}[/color]: [color=#EAC155]{info}[/color]"
                        results.append(text)
                
        return results
        
    def search_regex(self, regex):
        # This function will allow searching using regular expressions
        # The function will be impremented in the next version
        
        with sqlite3.connect(self.database) as conn:
            conn.create_function("REGEXP", 2, regexp)
            
            cursor = conn.cursor()
            cursor.execute("SELECT review FROM books WHERE review REGEXP ?;", (regex,))
            search_results = cursor.fetchall()
        
        return [x[0] for x in search_results]
        