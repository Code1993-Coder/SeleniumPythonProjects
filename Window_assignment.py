from selenium import webdriver
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Edge()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/#/cart")
driver.maximize_window()

#Usecase-
   #1.click on  blinkinglink and get the username from complete text
   #2.Switch back to main window
   #3.Use the username which was extracted and password and submit it
   #Get the error message and print it

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windows_opened=driver.window_handles


driver.switch_to.window(windows_opened[1])
para=driver.find_element(By.XPATH,"//div//p[2]").text

#Get the username from text using regex
pattern=

username=re.search(pattern,para)
if username:
    value=username.group()
    print("Extracted email",value)
else:
    raise ValueError("No email found")




#Let's switch back to main window to login
driver.switch_to.window(windows_opened[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(value)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys('password@1')
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

#Explicit wait to validate alert
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert")))

#print alert text for incorrect credentials
print(driver.find_element(By.CSS_SELECTOR,".alert").text)

