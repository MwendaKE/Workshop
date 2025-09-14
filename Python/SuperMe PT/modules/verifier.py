import re

def verify_date(date):
    '''Verify if date is in format 'yyyy-mm-dd' '''
    
    date_patt = "\d{4}-\d{2}-\d{2}"
    
    if re.match(date_patt, date):
        date_year = date.split("-")[0]
        date_month = date.split("-")[1]
        date_day = date.split("-")[2]
        
        if int(date_month) > 12 or int(date_day) > 31:
            return False
            
        return True
        
    else:
        return False
        
def verify_time(time):
    '''Verify if time is 4 digits and not greater that 2359 - 24 hour time upper range'''
    
    time_patt = "\d{4}"
  
    if re.match(time_patt, time): 
        if int(time) > 2359:
            return False
            
        return True   
        
    else:
        return False  
        
     
def verify_event_attendance(attendance):
	'''Convert str(attendance) to integer'''
	
	if isinstance(attendance, int):
	    if attendance == 0:
	        attended = "Not Attended"
	    
	    if attendance == 1:
	        attended = "Attended"
	        
	    if attendance == 2:
	        attended = "No Need To Attend"
	    
	elif isinstance(attendance, str):
	    if attendance == "Not Attended":
	        attended = 0
	    
	    if attendance == "Attended":
	        attended = 1
	    
	    if attendance == "No Need To Attend":
	    	attended = 2
	    	
	return attended
	  