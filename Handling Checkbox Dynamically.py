import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


#Handling checkbox dynamically via for loop

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=='option3':
        checkbox.click()
        assert checkbox.is_selected()
        break

#Handling radio button dynamically via for loop using index if radio buttons position is static
radio_buttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()
radio_buttons[2].click()
time.sleep(3)

#Verifying whether text field is displayed or not
assert driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()
assert not driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
time.sleep(5)

