import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

title = 'Blackberry'
#CSS for anchor tag->a[href*='shop']
#Xpath->//a[contains(@href,'shop')]#
#How to find the css and xpath via console- Xpath-$x("xpath"),CSS-$("css")

driver.find_element(By.LINK_TEXT, "Shop").click()

time.sleep(5)

driver.execute_script("window.scrollTo(500, 500);")

#items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
items=driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for item in items:
    #if item.find_element(By.XPATH, "//h4[@class='card-title']/a").text == title:
    if item.find_element(By.XPATH,"div/h4/a").text==title:
        item.find_element(By.XPATH, "div/button").click()
        break

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()

driver.find_element(By.CSS_SELECTOR,".btn-success").click()

driver.find_element(By.ID,"country").send_keys("India")

wait = WebDriverWait(driver, 10)


countries = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".suggestions li")))

print(driver.find_element(By.CSS_SELECTOR,".suggestions li").text)


for country in countries:
    if country.text=='India':
        country.click()
        break

driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
success_message=driver.find_element(By.CLASS_NAME, "alert").text

assert "Success!" in success_message



driver.close()


