# Debugging approach allows you to do step by step execution of each code and does provide solution for it
# Setting Breakpoints:
# Using an Integrated Development Environment (IDE) like Eclipse or IntelliJ, you can set breakpoints in your code.
# When running in debug mode, execution will pause at these points, allowing you to inspect variable values and step through the code line by line


from pageObject.sort_table import Sort_table


def sort_tables(BrowserInstance):
    driver=BrowserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()

    #1 Sort the elements on column and verify  
    # #2 get the element and add into sorted_list
    table=Sort_table(driver)
    table.validate_sort_tables()


