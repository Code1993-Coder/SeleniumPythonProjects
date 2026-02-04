import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action=ActionChains(driver)
#action.double_click(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click()
#action.drag_and_drop()
time.sleep(5)
#action.scroll_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(5)
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(10)
