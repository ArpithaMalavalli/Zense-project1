from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
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
  

#wait = WebDriverWait( browser, 5 )
  
'''try:
	page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
	self.fail( "Loading timeout expired" )
  
self.assertEqual(browser.current_url,correct_page,msg = "Successful Login")

calender=browser.find_element_by_xpath("//*[@id=\"yui_3_17_2_1_1546452330098_156\"]/div/div[2]/div/a")
calender.click()'''

browser.get("https://accounts.google.com/signin/v2/sl/pwd?elo=1&flowName=GlifWebSignIn&flowEntry=AddSession&cid=0&navigationDirection=forward")
