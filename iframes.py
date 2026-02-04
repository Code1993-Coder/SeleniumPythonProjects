import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

#frames are embedded on top of the html
#frames can be defined either id or name
#driver only works for html content on webpage it does not work for frames
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear
time.sleep(2)
driver.find_element(By.ID,"tinymce").send_keys("automating iframes content box")

#Swicting to default content on page which are html elements

driver.switch_to.default_content()
print(driver.find_element(By.XPATH,'//h3').text)
time.sleep(3)