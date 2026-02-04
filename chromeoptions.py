from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

service_obj=Service(r"C:\Users\Manju Mohan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

#creating objects of ChromeOptions() class
chrome_options=webdriver.ChromeOptions()

#creating different actions that can be performed on Chrome browser
#Using ChromeOptions() class we can perform different methods to perform operation on browser
chrome_options.add_argument("--headless")#does not invoke browser
chrome_options.add_argument("--ignore-certificate-errors") #ignore ssl/tsl certificate erros
chrome_options.add_argument("start-maximized")#maximize the screen


driver=webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(2)


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)




