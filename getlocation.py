from selenium 
import webdriver
from selenium.webdriver.chrome.service 
import Servicefrom webdriver_manager.chrome 
import ChromeDriverManagerfrom selenium.webdriver.chrome.options 
import Optionsfrom selenium.webdriver.support.ui 
import WebDriverWaitfrom selenium.webdriver.common.by import By
import time
def getLocation():    
	options = Options()    
	options.add_argument("--use--fake-ui-for-media-stream")    
	# options.add_argument('--headless')    
	options.add_argument('--no-sandbox')    
	options.add_argument('--disable-dev-shm-usage')    
	driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=options)  # Edit path of chromedriver accordingly    
	# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)    
	driver.minimize_window()    
	timeout = 2000    
	driver.get("https://mycurrentlocation.net/")    
	time.sleep(20)    
	output = driver.find_element(By.CLASS_NAME, 'mapboxgl-popup-content').text    
	print('output.....', output)    
	# try:    
	#     output = driver.find_element(By.CLASS_NAME, 'mapboxgl-popup-content').text    
	#     print('output.....', output)    
	# except:    
	#     print('no response....')    
	# wait = WebDriverWait(driver, timeout)    
	time.sleep(10)    
	driver.close()
getLocation()
