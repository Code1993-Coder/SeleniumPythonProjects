import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.checkout_confirmation import Checkout_Confirmation
from utils.BrowserUtils import BrowserUtils




class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link=(By.LINK_TEXT, "Shop")
        self.products=(By.XPATH, "//div[@class='card h-100']")
        self.checkout = (By.XPATH,"//a[contains(normalize-space(.), 'Checkout')]")
        self.checkbox_shopping = (By.XPATH, "//button[contains(@class,'btn-success')]")
        self.shop_list=(By.XPATH, "//div[@class='card h-100']")
        self.product_name=(By.CSS_SELECTOR, ".card-title")
        self.product_image=(By.CSS_SELECTOR, "img[class='card-img-top']")
        self.product_price=(By.XPATH, ".//h5")
        self.product_text=(By.XPATH, ".//p[@class='card-text']")
        self.add_to_cart=(By.CSS_SELECTOR,".card-footer button")
        self.product_list=(By.CSS_SELECTOR,".card.h-100")

    # CSS for anchor tag->a[href*='shop']
    # Xpath->//a[contains(@href,'shop')]#
    # How to find the css and xpath via console- Xpath-$x("xpath locator"),CSS-$("css locator")
    def product_count(self):
        print("product_count")
        self.driver.find_element(*self.shop_link).click()
        wait =WebDriverWait(self.driver, 10)
        product_list=wait.until(EC.visibility_of_all_elements_located(self.shop_list))
        print("Product count:",len(product_list))
        assert len(product_list)==4

    def product_cart_structure(self):

        wait = WebDriverWait(self.driver, 5)
        product_list = wait.until(EC.visibility_of_all_elements_located(self.shop_list))
        print("***product_cart_structure****")
        print("Total products:", len(product_list))

        for index, product in enumerate(product_list, start=1):
            name = product.find_element(*self.product_name).text
            price = product.find_element(*self.product_price).text
            image = product.find_element(*self.product_image).is_displayed()
            add_btn = product.find_element(*self.add_to_cart).is_enabled()

            print(f"\nProduct {index}")
            print("Name :", name)
            print("Price:", price)
            print("Image displayed:", image)
            print("Add button enabled:", add_btn)

            # validations
            assert image
            assert name != ""
            assert price != ""
            assert add_btn



    # Increase quantity of item and then decrease on checkout page
    def dynamic_quantity_increment(self, product, quantity):
        print("***dynamic_quantity_increment****\n")
        items = self.driver.find_elements(*self.products)
        product_found = False


        for item in items:
            product_name = item.find_element(*self.product_name).text.strip()
            if product_name.lower() == product.lower():
                product_found = True


                for number_of_items in range(quantity):
                    add_btn = item.find_element(*self.add_to_cart)
                    add_btn.click()
                print(f"{product_name} added {quantity} items to cart")
                break
        if not product_found:
            raise AssertionError(f"Product '{product}' not found")

        # validation total items in cart is equal to number of items added

        checkout_total = self.driver.find_element(*self.checkout).text
        print(checkout_total)

        total_items = int(re.sub(r"([^\d])", "", checkout_total))
        print(f"Total items: {total_items}")
        assert total_items >= quantity, \
            f"Cart count mismatch. Expected at least {quantity}, but got {total_items}"



    def verify_total_products_equal_to_cart_items(self):
        print("***verify_total_products_equal_to_cart_items****")
        added_products = []
        cards = self.driver.find_elements(*self.product_list)
        print(f"Total products on page: {len(cards)}")

        for card in cards:
            # Re-fetch product card to avoid stale elements
            #card = self.driver.find_elements(*self.product_list)

            # Get product name
            name = card.find_element(*self.product_name).text.strip()

            #Add the product to cart
            card.find_element(*self.add_to_cart).click()

            #Update the list
            added_products.append(name)

            #Print in console
            print(f"Added to cart: {name}")



        #validation total items in cart is equal to number of products on page
        checkout_total=self.driver.find_element(*self.checkout).text
        print(checkout_total)

        total_items=int(re.sub(r"([^\d])", "", checkout_total))
        print(f"Total items: {total_items}")
        assert total_items >=len(cards), \
            f"Expected {len(cards)} items, but found {total_items}"

    def add_product(self,products):
        print("*** add_product ***")

        if isinstance(products, str):
            products = [products]

        expected_products = [p.lower() for p in products]

        self.driver.execute_script("window.scrollTo(500, 500);")

        product_elements = self.driver.find_elements(*self.products)

        for product in product_elements:
            product_name = product.find_element(*self.product_name).text.strip().lower()

            if product_name in expected_products:
                product.find_element(*self.add_to_cart).click()

        checkout_total = self.driver.find_element(*self.checkout).text
        print(checkout_total)

        total_items = int(re.sub(r"([^\d])", "", checkout_total))
        print(f"Total items: {total_items}")
        assert total_items >= len(expected_products), \
            f"Expected {len(expected_products)} items, but found {total_items}"


    def go_to_cart(self):
        print("***go_to_cart****")
        self.driver.find_element(*self.checkout).click()
        checkout_obj=Checkout_Confirmation(self.driver)
        return checkout_obj
