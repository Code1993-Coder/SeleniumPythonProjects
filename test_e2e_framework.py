import json

import pytest
# pytest -n 2-m smoke --browser firefox --html reports/report.html - use this command in terminal to run in parallel mode and execute only
#smoke marked test case and generate html report in reports folder with failed screenshot attched to html

import sys
print(sys.path)
from pageObject.SignIn import LoginPage
#Data driven testing can be performed using parametrization which allows you to pass different sets of data

test_data_path = "data/test_e2e_framework.json"  #path of json file which holds test data for this test case
with open(test_data_path) as json_file: #this is used to access json file and to convert into python objects
    test_data = json.load(json_file)
    test_list=test_data['data']

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)#this enables storage of test data in list format
def test_e2e(BrowserInstance, test_list_item):
    
    driver = BrowserInstance
    log= LoginPage(driver)
    print(log.getTitle())
    shop=log.login(test_list_item['username'],test_list_item['password'])
    print("E2E Page:Functionality test")
    shop.add_product(test_list_item['product'])
    print(shop.getTitle())
    checkout_obj=shop.go_to_cart()
    checkout_obj.checkout_confirm()
    checkout_obj.submit_address(test_list_item['country'])
    checkout_obj.validate_order()


