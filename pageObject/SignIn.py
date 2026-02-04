#POM -Page object model is designed to develop a class per page which is used to separate page locators and actions from
# test files .This improves code reusability,readability and maintainability
#page object should only have action methods and locator

#locators has to be defined in constructor so that if their any changes in properties of web elements we will have to update the changes
#at centralized place that is constructor

#All actions on a page are defined within methods
#To access locators outside the constructor we have to make use of self keyword so that I can use it anywhere

from selenium.webdriver.common.by import By

from pageObject.Shop import ShopPage
from utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.SigIn=(By.ID, "signInBtn")


    def login(self,username,password):

        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.SigIn).click()

        shop = ShopPage(self.driver)
        return shop


