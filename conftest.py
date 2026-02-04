import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=None
#this steps is used to register the browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome",help="browser type")

@pytest.fixture
def BrowserInstance(request):#request is used to get configuration options from terminal
    global driver
    browser=request.config.getoption("browser")
    service_obj = Service(r"C:\Users\Manju Mohan\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    if browser=="chrome":
        options = webdriver.ChromeOptions()

        chrome_prefs = {

            "credentials_enable_service": False,

            "profile.password_manager_enabled": False,

            "profile.password_manager_leak_detection": False

        }

        options.add_experimental_option('prefs', chrome_prefs)
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser=='firefox':
        driver=webdriver.Firefox()
    driver.implicitly_wait(8)
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.maximize_window()
    yield driver#this give control back to test function to work on test steps written in it and will run before test function execution
    driver.close()#this is post condition step where the control comes back from test function after business process step is completed


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_").replace("/", "_") + ".png")
            print("file name is " + file_name)

            driver = item.funcargs.get("BrowserInstance")
            if driver:
                _capture_screenshot(driver, file_name)
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extras = extra






def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)