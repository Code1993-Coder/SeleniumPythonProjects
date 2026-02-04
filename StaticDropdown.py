
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


service_obj=Service(r"C:\Users\Manju Mohan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Static dropdown-This will have Select tag in html for the dropdown then only use Select class else no

time.sleep(10)
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text('Female')
#dropdown.select_by_value()

