from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

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
def add():
	date=datetime.datetime.now()
	str1='2019-'+str(format(date.month,'02d'))+'-06T10:00:00+05:30'
	event = {
	  'summary': 'Google I/O 2015',
	  'location': '800 Howard St., San Francisco, CA 94103',
	  'description': 'A chance to hear more about Google\'s developer products.',
	  'start': {
	    'dateTime': '2019-01-06T09:00:00+05:30',
	    'timeZone':'Asia/Kolkata',
	  },
	
	  'end': {
	    'dateTime': str1,
	    'timeZone': 'Asia/Kolkata',
	  },
	  'recurrence': [
	    "RRULE:FREQ=WEEKLY;UNTIL=20191030T065959Z"
	  ],
	  'reminders': {
	    'useDefault': False,
	    'overrides': [
	      {'method': 'email', 'minutes': 24 * 60},
	      {'method': 'popup', 'minutes': 10},
	    ],
	  },
	}

	event = service.events().insert(calendarId='primary', body=event).execute()
	print ('Event created:',(event.get('htmlLink')))


if __name__ == '__main__':
    check()
    add()
    
