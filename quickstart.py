from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from datetime import date
import calendar

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
Saturday=Weekday([],[],[])

day_to_obj={'Sunday':Sunday}	


def add(wday):
	print (wday.eventl)
	for i in range(len(wday.eventl)): 
		event = {
		  'summary': wday.eventl[i],
		 # 'location': '800 Howard St., San Francisco, CA 94103',
		 # 'description': 'A chance to hear more about Google\'s developer products.',
		  'start': {
		    'dateTime': '2019-01-06T'+wday.startl[i]+'+05:30',
		    'timeZone':'Asia/Kolkata',
		  },
		
		  'end': {
		    'dateTime': '2019-01-06T'+wday.endl[i]+'+05:30',
		    'timeZone': 'Asia/Kolkata',
		  },
		 # 'recurrence': [
		 #   "RRULE:FREQ=WEEKLY;UNTIL=20191030T065959Z"
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
	print ('Events for the day created:')#,(event.get('htmlLink')))


	
if __name__ == '__main__':
	check()
	my_date = date.today() 
	add(day_to_obj[calendar.day_name[my_date.weekday()]])
    
