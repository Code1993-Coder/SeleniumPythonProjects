import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Close login popup

try:
    driver.find_element(By.XPATH, "//button[text()='✕']").click()
except:
    pass

driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']").click()

wait = WebDriverWait(driver, 15)
suggest = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,"//ul[contains(@class,'GZVzXz')]/li[.//a]//div[contains(@class,'URRkKz')]")))



suggestions =driver.find_elements(By.XPATH, "//ul[contains(@class,'GZVzXz')]/li[.//a]//div[contains(@class,'URRkKz')]")

for elements in suggestions:
    print(elements.text)
