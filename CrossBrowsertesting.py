#river=webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com")
#driver.maximize_window()
#time.sleep(3)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Firefox
#driver=webdriver.Firefox()
#driver.get("https://rahulshettyacademy.com")
#driver.maximize_window()


#Edge
#driver=webdriver.Edge()
#driver.get("https://rahulshettyacademy.com")
#driver.maximize_window()

service_obj=Service(r"C:\Users\Manju Mohan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
time.sleep(2)