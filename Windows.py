import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()

#This list holds number of open windows in the current session beginning  with index 0 for first window and 1 for second
#window

#switch to child windows
windowsopened=driver.window_handles
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(2)
driver.close()

#switch back to parent window
driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text