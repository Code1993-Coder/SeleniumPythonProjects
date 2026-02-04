import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(10)

#Dynamic dropdown
#Usecase-Need to select India from dynamic dropdown

#We made use of find_elements to iterate values
#text is used to get the values of the dropdown

driver.find_element(By.ID,'autosuggest').send_keys('ind')
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")


for country in countries:
    if country.text=="India":
        country.click()
        break



print(driver.find_element(By.ID,'autosuggest').text)

#To validate dynamic texts on browser use get_attributes of values

driver.find_element(By.ID,'autosuggest').get_attribute("value")=="India"
time.sleep(10)


