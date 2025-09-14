from datetime import datetime

class AppColor:
    '''Defines all colors used in the SuperMe App'''
    
    #Yellow color: #EAC155
    
    yellow_fo = (234/255, 193/255, 85/255, 1.0)
    yellow_to = (234/255, 193/255, 85/255, 0.75)
    yellow_ho = (234/255, 193/255, 85/255, 0.5)
    yellow_qo = (234/255, 193/255, 85/255, 0.25)
    
    #Red color: #E64646
    
    red_fo = (230/255, 70/255, 70/255, 1.0)       
    red_to = (230/255, 70/255, 70/255, 0.75)
    red_ho = (230/255, 70/255, 70/255, 0.5)
    red_qo = (230/255, 70/255, 70/255, 0.25)
    red_bg = (230/255, 70/255, 70/255, 0.1)
    
    #Teal color: #26DDC7
    
    teal_fo = (38/255, 221/255, 199/255, 1.0)    
    teal_to = (38/255, 221/255, 199/255, 0.75)
    teal_ho = (38/255, 221/255, 199/255, 0.5)
    teal_qo = (38/255, 221/255, 199/255, 0.25)
    
    black_ho = (0, 0, 0, 0.5)
    
    #TEXT COLORS
    green_tc = "83AE74"
    lightred_tc = "EF8887"
    yellow_tc = "EAC155"
    white_tc = "E0C7EA"
    teal_tc = "26DDC7"
    
    background = "111111"
    text_color = "FFFFFF"
               

class Title:
    '''Defines all titles used in SuperMe App'''
    add_category = "Add Category"
    add_author = "Add Author"
    
    books = "Books"
    add_book = "Add Book"
    add_book_author = "Add Book Author"
    delete_book = "Delete Book"
    edit_book = "Edit Book"
    
    quotes = "Quotes"
    add_quote = "Add Quote"
    add_quote_author = "Add Quote Author"
    delete_quote = "Delete Quote"
    
    music = "Music"
    add_music = "Add Music"
    add_music_artist = "Add Music Artist"
    add_artist = "Add Music Artist"
    add_music_genre = "Add Music Genre"   
    delete_music = "Delete Song"
    
    events = "Events"
    add_event = "Add Event"
    edit_event = "Edit Event"
    delete_event = "Delete Event"
    about_event = "About Event"
    event_description = "Event Description"
    
    diaries = "Diaries"
    add_diary_entry = "Add Diary Entry"
    add_diary_categ = "Add Diary Category"
    delete_diary = "Delete Diary"
    
    tasks = "Tasks"
    add_task = "Add Task"
    add_task_categ = "Add Task Category"
    delete_task = "Delete Task"
    
    poems = "Poems"
    add_poem = "Add Poem"
    add_poem_author = "Add Poem Author"
    edit_poem = "Edit Poem"
    about_poem = "About Poem"
    delete_poem = "Delete Poem"
    
    articles =  "Articles"
    add_article = "Add Article" 
    add_article_writer = "Add Article Writer"
    edit_article = "Edit Article"
    delete_article = "Delete Article" 
    article_information = "Article Information"
    
    add_clip = "Add Clip"


class Error:
    now = datetime.now()
    
    '''Defines errors used in SuperMe App'''
    category_exists = "A category with this name already exists in the database!"
    book_exists = "A book with this title already exists in the Books library!"
    quote_exists = "This quote already exists in the quotes library!"
    author_exists = "An author with this name already exists in the database!"
    music_exists = "A song with this title already exists in the music library!"
    artist_exists = "An Artist with this name already exists in the database!"
    genre_exists = "A Genre with this name already exists in the database!"
    event_exists = "There is an event with the same title in the database!"
    diary_exists = "A diary entry with this title is already in the database!"
    task_exists = "A task with this name is already in the database. Please create a unique task."
    poem_exists =  "A poem with this name is already in the database. Please create a unique poem." 
    article_exists =  "An article with this name is already in the database. Please create a unique article." 
    writer_exists =  "A writer with this name is already in the database. Please create a unique writer." 
    clip_exists =  "A clip with this text is already in the database. Please create a unique clip." 
    
    book_review_error = "[color=FA0000][b] An error occured while opening review for this book.[/b][/color]"
    task_review_error = "[color=FA0000][b] An error occured while opening this task.[/b][/color]"
    article_view_error = "[color=FA0000][b] An error occured while viewing this article.[/b][/color]"
    wrong_date_format = f"Wrong date format! Please enter the correct date using the format 'yyyy-mm-dd'. E.g. {now.year}-02-10 or {now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}."
    wrong_time_format = "Wrong time format! Please enter the correct time using the 24-hour format 'hhhh'. E.g. 0800 for 8AM or 1700 for 5PM."
    
    cannot_delete_book = "Error! This book cannot be deleted."
    cannot_delete_music = "Error! This song cannot be deleted."
    event_delete_error = "Error! This event cannot be deleted"
    article_delete_error = "Error! This article cannot be deleted."
    poem_delete_error = "Error! This poem cannot be deleted."
    
    event_edit_error = "Error! Cannot edit this event"
    
    query_patt_error = "Error: Query pattern error!"
    
    required = "Cannot add an empty field: All fields are required!"
   
    
class ErrorCode:
	query_patt_error = "E01QP"
	query_db_error = "E02QD"
	
	
class Message:
    no_books = "[b][i]No books. Click '+ Add' below to add.[/i][/b]"
    no_music = "[b][i]No music. Click '+ Add' below to add.[/i][/b]"
    no_diary = "[b][i]No diary. Click '+ Add' below to add.[/i][/b]"
    no_quotes = "[b][i]No quotes. Click '+ Add' below to add.[/i][/b]"
    no_tasks = "[b][i]No tasks. Click '+ Add' below to add.[/i][/b]"
    no_events = "[b][i]No events. Click '+ Add' below to add.[/i][/b]"
    no_poems = "[b][i]No poems. Click the '+ Add' below to add.[/i][/b]"
    no_articles =  "[b][i]No articles. Click '+ Add' below to add.[/i][/b]"  
    no_clips =  "[b][i]No clips. Click '+ Add' below to add.[/i][/b]"  
    
    no_authors = "[b][i]No authors. Click '+ Add' below to add.[/i][/b]"
    no_artists = "[b][i]No artists. Click '+ Add' below to add.[/i][/b]"
    no_poets = "[b][i]No poets. Click '+ Add' below to add.[/i][/b]"
    no_writers = "[b][i]No writers. Click '+ Add' below to add.[/i][/b]"
    
    no_book_content = "[color=FF0000]Content for this book cannot be displayed![/color]"
    no_poem_content = "[color=FF0000]Content for this poem cannot be displayed![/color]"
    no_event_content = "[color=FF0000]Content for this event cannot be displayed![/color]"
    no_diary_content = "[color=FF0000]Content for this diary cannot be displayed![/color]"
    no_task_content = "[color=FF0000]Content for this task cannot be displayed![/color]"
   
    no_book_description = "[b]This book has not been provided with a description.[/b]"
    no_diary_description = "[b]This diary has not been provided with a description.[/b]"
    no_book_review = "No book review to display."
    no_music_lyries = "No music lyries to view."
    no_author_content = "No information available for this author."
    no_artist_content = "No information available for this artist."
    no_poet_content = "No information available for this poet."
    no_writer_content = "No information available for this writer."
    
    
class Text:
    select_category = "Select Category"
    select_author = "Select Author"
    select_writer = "Select Writer"
    select_artist = "Select Artist"
    select_genre = "Select Genre"
    select_country = "Select Country"
    select_mood = "Select Mood"
    select_duration = "Select Duration"
    select_attendance = "Select Attendance"
    select_type = "Select Type"
 