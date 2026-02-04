from os.path import exists

from openpyxl.styles.builtins import total
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.BrowserUtils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = (By.XPATH,"//a[contains(normalize-space(.), 'Checkout')]")

        self.country=(By.ID, "country")
        self.country_selections=(By.CSS_SELECTOR, "div.suggestions ul li a")
        self.checkbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.checkbox_shopping=(By.XPATH, "//button[contains(@class,'btn-success')]")
        self.submit=(By.CSS_SELECTOR, "input[type='submit']")
        self.alert=(By.CLASS_NAME, "alert")
        self.product_table=(By.XPATH,"//table[contains(@class, 'table')]")
        self.table_rows=(By.XPATH,".//tbody/tr[.//h4/a]")
        self.product_name=(By.XPATH,".//h4/a")
        self.product_remove = (By.XPATH,".//button[contains(@class,'btn-danger') and contains(normalize-space(.),'Remove')]")
        self.quantity=(By.XPATH,".//input[@type='number']")
        self.product_cart=(By.CSS_SELECTOR,".card.h-100")
        self.add_to_cart = (By.CSS_SELECTOR, ".card-footer button")

    #Verify product table exists
    def product_order_table(self):
         table= self.driver.find_element(*self.product_table)
         assert table.is_displayed(), "Product table is not visible"

    #verify list of  product is removed dynamically
    def product_removal(self, products):

        #Convert single product into list
        if isinstance(products, str):
            products = [products]


        # Get all products on page before removal
        order_table = self.driver.find_element(*self.product_table)
        rows = order_table.find_elements(*self.table_rows)
        before_removal = [row.find_element(*self.product_name).text.strip() for row in rows]
        print("Products before removal:", before_removal)

        # Remove product when there is match
        for product_item in products:
            print(f"Removing product: {product_item}")

            for row in rows:
                product_name = row.find_element(*self.product_name).text.strip()
                if product_name.lower() == product_item.lower():
                    row.find_element(*self.product_remove).click()
                    product_found = True
                    break

            assert product_found, f"Product '{product_item}' not found in cart"

            # Wait until the product link is no longer present
            wait=WebDriverWait(self.driver, 5)
            product_xpath = f"//h4/a[normalize-space()='{product_item}']"
            wait.until(EC.invisibility_of_element_located((By.XPATH, product_xpath)))

        # Collect product names after removal

        updated_rows = order_table.find_elements(*self.table_rows)
        after_removal =[row.find_element(*self.product_name).text.strip() for row in updated_rows]
        print("Products after removal:", after_removal)

        # Final validation
        for removed_product in products:
            assert removed_product not in after_removal, f"{removed_product} was NOT removed!"



        raise AssertionError(f"Product '{product_name}' not found in cart")

    #Verify TotalPrice after product update:
    def price_evaluate(self,products):
        # Convert single product into list
        if isinstance(products, str):
            products = [products]

        found_products=[]
        order_table = self.driver.find_element(*self.product_table)
        rows = order_table.find_elements(*self.table_rows)


        for product in products:

            for row in rows:

                product_name= row.find_element(*self.product_name).text.strip()

                
                if product_name.lower() == product.lower():
                    #get the price
                    price_text = row.find_element(By.XPATH,".//td[3]").text.strip()
                    price_value = float(price_text.replace("₹", "").replace(".", "").strip())
                    print("*****************************************")
                    print(f"Price of {product_name}: {price_value}")

                    #Get the quantity
                    try:
                        quantity_input =int(row.find_element(*self.quantity).get_attribute("value"))
                    except:
                        quantity_input = 1

                    #Get the displayed total price
                    total_text = row.find_element(By.XPATH, ".//td[4]").text.strip()
                    displayed_total = float(total_text.replace("₹", "").replace(".", "").strip())
                    print("*****************************************")
                    print(f"Displayed total price of {product}: {displayed_total}")

                    #Calculate expected total price
                    expected_total = price_value * quantity_input
                    print("*****************************************")
                    print(f"Expected total price of {product}: {expected_total}")

                    print("*****************************************")
                    print(f"Product:{product}")
                    print(f"Price: {price_value}")
                    print(f"Quantity: {quantity_input}")
                    print(f"Expected Total: {expected_total}")
                    print(f"Diplayed/Actual Total Price: {displayed_total}")


                    #Validation
                    print("*****************************************")
                    assert expected_total == displayed_total, \
                    f"Total mismatch for {product}: Expected {expected_total}, but got {displayed_total}"
                    found_products.append(product_name)
                    print(found_products)

        #Check missing products after all rows are processed
        missing = set(products) - set(found_products)
        if missing:
            print("*****************************************")
            raise AssertionError(f"Products not found in cart: {missing}")


    def quantity_decrement(self,product):
        order_table = self.driver.find_element(*self.product_table)
        rows = order_table.find_elements(*self.table_rows)
        for row in rows:
            product_name=row.find_element(*self.product_name).text.strip()
            if product.lower() == product_name.lower():
                #read the web element
                qty_element = row.find_element(*self.quantity)
                # Read the current quantity
                current_quantity=int(qty_element.get_attribute("value"))
                # Calculate new quantity
                new_quantity=current_quantity-1

                if new_quantity<=0:# clear existing number
                    new_quantity = 1

                # Update input field
                qty_element.clear()
                qty_element.send_keys(str(new_quantity))


                print(f"Updated quantity for {product} to {new_quantity}")
                return

    #Select Checkout button
    def checkout_confirm(self):
        self.driver.find_element(*self.checkbox_shopping).click()

    #Country Selection
    def submit_address(self,country_name):
        self.driver.find_element(*self.country).send_keys(country_name)
        wait = WebDriverWait(self.driver, 15)
        options=wait.until(EC.visibility_of_all_elements_located(self.country_selections))#this will already be in unpacked locator format
        for option in options:
            if option.text.strip() == country_name:
                option.click()
                break


        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()

    #Validate success message
    def validate_order(self):
        success_message = self.driver.find_element(*self.alert).text
        assert "Success!" in success_message
