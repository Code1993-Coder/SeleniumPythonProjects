#Elements can be identified via ID,Classname,name,linktext,Xpath,CSSSelector
#Xpath- //tagname[@attribute='value'],
# webpage has same element property then index can be used -/(/tagname[attribute='value'])[index_number]
#CSSSelector- tagname[attribute='value'],#id,.classname


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service(r"C:\Users\Manju Mohan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

#Parent to child properties
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys('demo@test.com')
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys('test@123')
driver.find_element(By.XPATH,"//input[@placeholder='Confirm Passsword']").send_keys('test@123')
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


