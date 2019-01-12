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
week_name={'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}
month_no={'January':'1','February':'2','March':'3','April':'4','May':'5','June':'6','July':'7','August':'8','September':'9','October':'10','November':'11','December':'12'}

  
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
#print #"ref\t",i.find("a",class_="dimmed")['href']
for i in l:
		
		event_name=[i.a.text]
		my_string=i.find("div",class_="date").text
		my_list = my_string.split(",")
		print (my_list)
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
			print(x)
			month=month_no[x[2]]
			day1=x[1]
			year=str(now.year)
			date1=year+'-'+month+'-'+day1
		print(date1)


