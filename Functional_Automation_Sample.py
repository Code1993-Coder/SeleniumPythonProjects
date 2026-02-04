import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


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

expected_list=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list=[]

#Chaining of web elements -traversing from parent web element to child web element
for item in items:
    #Get the title of each items and add to new list via chaining
    actual_list.append(item.find_element(By.XPATH,"h4").text)
    item.find_element(By.XPATH,"div/button").click()
assert expected_list==actual_list

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation

#Validate total amt is sum of total items in table
#Lets get iterate total col values

prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum  = 0
for price in prices:
    sum = sum+int(price.text)

print(sum)

total_amt=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == total_amt


#Apply PromoCode
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Explict wait-This is given as this step requires additional wait
#This requires a condition to check as long as the element becomes present on page and resume the operation
#It a dynamic wait and does wait for max timeout
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))


print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert driver.find_element(By.CLASS_NAME,"promoInfo").text=='Code applied ..!'

#Validate amt after discount is less than total amount

discount_amt=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert discount_amt < total_amt



