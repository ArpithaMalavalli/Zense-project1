from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from datetime import date
import calendar
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib2
from lxml import html 
import time

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

def check():
 
    print('Getting the upcoming 2 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=2, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

class Weekday:
	def __init__(self,event_list,stime_list,etime_list):
		self.eventl=event_list
		self.startl=stime_list
		self.endl=etime_list

Sunday=Weekday(['MAD'],['09:00:00'],['12:00:00'])
Monday=Weekday(['Computer Network','Digital Design','DSA lab'],['09:15:00','11:00:00','13:30:00'],['10:45:00','12:30:00','15:30:00'])
Tuesday=Weekday(['DSA','Math-2','PE'],['09:15:00','11:00:00','16:00:00'],['10:45:00','12:30:00','17:30:00'])
Wednesday=Weekday(['Computer Network','Technical communication'],['09:15:00','13:30:00'],['10:45:00','15:30:00'])
Thursday=Weekday(['DSA','Digital Design','DSA tutorial','Comp networks tutorial'],['09:15:00','11:00:00','13:30:00','14:30:00'],['10:45:00','12:30:00','14:30:00','15:30:00'])
Friday=Weekday(['Math-2','computational chemistry','Digital design tutorial','Math tutorial'],['09:15:00','11:00:00','13:30:00','14:30:00'],['10:45:00','12:30:00','14:30:00','15:30:00'])
Saturday=Weekday(['MAD'],['09:00:00'],['12:00:00'])

day_to_obj={'Sunday':Sunday,'Monday':Monday,'Tuesday':Tuesday,'Wednesday':Wednesday,'Thursday':Thursday,'Friday':Friday,'Saturday':Saturday}	
week_name={'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}
month_no={'January':'1','February':'2','March':'3','April':'4','May':'5','June':'6','July':'7','August':'8','September':'9','October':'10','November':'11','December':'12'}
def addtt(wday):
	print (wday.eventl)
	for i in range(len(wday.eventl)): 
		event = {
		  
		  'summary': wday.eventl[i],
		 # 'location': '800 Howard St., San Francisco, CA 94103',
		 # 'description': 'A chance to hear more about Google\'s developer products.',
		  'start': {
		    'dateTime':str(date.today())+'T'+wday.startl[i]+'+05:30',
		    'timeZone':'Asia/Kolkata',
		  },
		
		  'end': {
		    'dateTime':str(date.today())+'T'+wday.endl[i]+'+05:30',
		    'timeZone': 'Asia/Kolkata',
		  },
		#  'recurrence': [
		#  "RRULE:FREQ=WEEKLY;UNTIL=20191030T065959Z"
		# ],
		  'reminders': {
		    'useDefault': False,
		    'overrides': [
		      {'method': 'email', 'minutes': 24 * 60},
		      {'method': 'popup', 'minutes': 10},
		    ],
		  },
		}

		event = service.events().insert(calendarId='primary', body=event).execute()
	print ('Events for the day created:',(event.get('htmlLink')))

def add(event_name,day,date1):

		event = {
		  'kind':'Tasks',
		  'summary': event_name,
		 # 'location': '800 Howard St., San Francisco, CA 94103',
		 # 'description': 'A chance to hear more about Google\'s developer products.',
		  'start': {
		    'date':str(date1),
		    'timeZone':'Asia/Kolkata',
		  },
		
		  'end': {
		    'date':str(date1),
		    'timeZone': 'Asia/Kolkata',
		  },
		#  'recurrence': [
		#  "RRULE:FREQ=WEEKLY;UNTIL=20191030T065959Z"
		# ],
		  'reminders': {
		    'useDefault': False,
		    'overrides': [
		      {'method': 'email', 'minutes': 24 * 60},
		      {'method': 'popup', 'minutes': 10},
		    ],
		  },
		}

		event = service.events().insert(calendarId='primary', body=event).execute()
		
		print ('Events for the day created:')


def getKey(dict1,val):
	for key in dict1.keys():
          if dict1[key] == targetval:
            return key

def get_event():
	event=Weekday([],[],[])
	browser = webdriver.Chrome('./chromedriver')
	browser.get("https://lms.iiitb.ac.in/moodle/login/index.php")
	  
	username = browser.find_element_by_name("username")
	password = browser.find_element_by_name("password")
	submit   = browser.find_element_by_id("loginbtn")

	username.clear()  
	username.send_keys("IMT2018504")
	password.clear()
	password.send_keys("Arpabh-123")



	submit.click()
	time.sleep(3) 

	final_page = BeautifulSoup(browser.page_source,'lxml')
	all_events=final_page.find("div",class_="card-text content calendarwrapper")
	l=all_events.find_all("div",class_="event")
	now=datetime.datetime.now()
	for i in l:
			
			event_name=[i.a.text]
			my_string=i.find("div",class_="date").text
			my_list = my_string.split(",")
			if len(my_list)==2:
				if my_list[0]=="Tomorrow":
					date1=str(datetime.datetime.today() + datetime.timedelta(days=1))
					val=week_name[calendar.day_name[date.today().weekday()]]
					day=getKey(week_name,val+1)
				elif my_list[0]=="Today":
					date1=date.today()
					day=calendar.day_name[date1.weekday()]
			elif len(my_list)==3:
				day=my_list[0]
				x=my_list[1].split(' ')
				month=month_no[x[2]]
				day1=x[1]
				year=str(now.year)
				date1=year+'-'+month+'-'+day1
			print(date1)
			add(event_name,day,date1)
			
			
		


	
if __name__ == '__main__':
	#check()
	my_date = date.today() 
	addtt(day_to_obj[calendar.day_name[my_date.weekday()]])
	get_event()
    
