from selenium import webdriver

#Enables Headless mode where the browser is invoked from backend and is not visible in frontend
chrome_options=webdriver.ChromeOptions() #ChromeOptions is a class which can be used to enable headless mode
chrome_options.add_argument('--headless')

#this ignre ssl certificate errors and directly land to website

chrome_options.add_argument("ignore-certificate-errors")
#
driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")



#browser are designed on javascript so in order to scroll the application selenium  does not have the method to do it.
#in such situation to switch to scroll you may need to use to switch to execute_script which can scroll the page
#you can use the console tab and enter the followining command -window.scrollBy(x,y) and then hit enter
#this you will be able to see window scrolls on the page .
# Here x reprsents horizontal axis and y as vertical axis
#document.body.scrollHeight)")- this returns the max height of the web page


driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#to get screenshots u can make use of below command
driver.get_screenshot_as_file("scroll.png")