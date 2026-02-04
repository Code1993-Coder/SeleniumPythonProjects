import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


#Handling browser alerts/Java or Javscript alert popups using alert ,accept and dismiss method
name='Tango'


#Scenario-Give a name and select alert option ,this display alert on browser.Make sure to accept it
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(5)
alert=driver.switch_to.alert
alerttext=alert.text
print(alerttext)
assert name in alerttext
alert.accept()
#alert.dismiss()


