import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
#Global Implict wait which will wait for max 2s and returns exception if element is not found on page
#It will apply wait from body of webpage elements and acts as dynamic wait
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


#Scenario :Search for an item and add to cart and proceed to checkout


driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys('ber')

#Static wait is required here as
      #implicit wait does not work for find_elements as no exception occur even if element is not found or list is empty
      #So in order to get the list we need to give static wait

time.sleep(2)
items=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(items)
assert count >0


#Chaining of web elements -from parent web element to child web element
for item in items:
    item.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Explict wait-This is given as this step requires additional wait
#This requires a condition to check as long as the element becomes present on page and resume the operation
#It a dynamic wait and does wait for max timeout
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))


print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert driver.find_element(By.CLASS_NAME,"promoInfo").text=='Code applied ..!'



