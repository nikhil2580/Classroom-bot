
import time  
from datetime import datetime
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
link2 = '//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[2]/div[2]/div/span/a/div'


def attend(link1):
	opt = Options()
	opt.add_argument("--disable-infobars")
	opt.add_argument("start-maximized")
	opt.add_argument("--disable-extensions")
	opt.add_argument("--disable-notifications")
	opt.add_experimental_option("prefs", { \
		"profile.default_content_setting_values.media_stream_mic": 1, 
		"profile.default_content_setting_values.media_stream_camera": 1,
		"profile.default_content_setting_values.geolocation": 2, 
		"profile.default_content_setting_values.notifications": 2 
	})
	driver = webdriver.Chrome(options=opt)
	driver.get(link1)
	driver.find_element_by_id("identifierId").send_keys("Your-email",Keys.ENTER)  
	time.sleep(10)  
	driver.find_element_by_name("password").send_keys("Password",Keys.ENTER)
	time.sleep(25)
	driver.find_element_by_xpath(link2).click()
	time.sleep(35)
	


def classes(subject):
	
	if subject == 'simulation':
		attend("https://classroom.google.com/c/MjIwNzAzMjA3ODU1")

	if subject == 'webengineering': 
		attend("https://classroom.google.com/c/MjQ5Njc5NzEzMDA2")

	if subject ==  'compiler':
		attend("https://classroom.google.com/c/MjQ5NTYyMzc3Mzg5")	

	if subject ==  'energy':  
		attend("https://classroom.google.com/c/MjQ5NzE5MzMzNjQz")
		 
	if subject ==  'image':
		attend("https://classroom.google.com/c/MjQ5Mzg4MjU0MTc4")

	if subject ==  'soft':
		attend("https://classroom.google.com/c/MjQ5NTEyMDYyMTg1") 

def current_time_string():
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M:%S", named_tuple)
	return time_string

def date_return(s1,s2):
	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)	
	return tdelta.total_seconds()

timetable = [
				[['09:00:00','simulation'],['12:00:00','soft'],['14:00:00','webengineering'],['15:00:00','compiler'],['16:00:00','image']],
				[['10:00:00','webengineering'],['11:00:00','compiler'],['13:00:00','image'],['14:00:00','energy'],['17:00:00','compiler']],
				[['10:00:00','compiler'],['11:00:00','webengineering'],['12:00:00','energy'],['13:00:00','soft']],
				[['09:00:00','simulation'],['11:00:00','energy'],['12:00:00','webengineering'],['13:00:00','image'],['16:00:00','soft']],
				[['09:00:00','simulation'],['12:00:00','compiler'],['13:00:00','image'],['15:00:00','energy'],['16:00:00','soft']]			
			]
 
i = datetime.today().weekday()
print("\nToday's Classes Schedule\n")
for j in range (0,len(timetable[i])):
	print(timetable[i][j][0]+"  ----------  "+timetable[i][j][1]) 

print("\n")
time.sleep(20)
for j in range(0,len(timetable[i])):
	pt = date_return(current_time_string(),timetable[i][j][0])
	print(pt,timetable[i][j][1])
	if pt<0 and pt>-3600:
		pt=0
	if pt<(-3600):
		continue

	time.sleep(pt)
	classes(timetable[i][j][1])
	
	