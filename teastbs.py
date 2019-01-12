'''from bs4 import BeautifulSoup
import requests
r = requests.get("https://koppl.in/indigo/")

soup = BeautifulSoup(r.content,'lxml')
s=soup.prettify()
l=soup.find("div", class_="page home")
x=l.find_all("a")
for i in x:
	print(i['href'])'''

import requests,datetime
from bs4 import BeautifulSoup
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
import warnings
warnings.filterwarnings('ignore')

with requests.Session() as session:
	login_url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
	request_url = 'https://lms.iiitb.ac.in/moodle/my/'
	usr = {'username':'IMT2018504',
	       'password':'arpabh1019' }
	
	log = session.get(login_url,verify = False)
	login = session.post(login_url,data = usr,verify = False)
	page = session.get(request_url,verify = False)
final_page = BeautifulSoup(page.content, 'html5lib')
l=final_page.find("div", class_="homelink").a['href']
browser = webdriver.Chrome('./chromedriver')
browser.get(request_url)

