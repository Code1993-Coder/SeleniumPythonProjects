from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Sort_table():
    def __init__(self,driver):
        self.driver=driver
        sort_column=(By.CSS_SELECTOR, ".sort-icon")
        total_items=(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")



    def validate_sort_tables(self):
        # Sort the elements on column and verify
        sorted_list = []
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.sort_column))
        self.driver.find_element(*self.sort_column).click()
        total_items = self.driver.find_elements(*self.total_items)
        # get the element and add into sorted_list

        for item in total_items:
            sorted_list.append(item.text)

        print(sorted_list)
        print("***************************************")
        original_list = sorted_list.copy()
        sorted_list.sort()

        print("***************************************")
        print(sorted_list)

        assert original_list == sorted_list