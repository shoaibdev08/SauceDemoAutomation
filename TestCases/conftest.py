import pytest
from selenium import webdriver

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function")
def setup():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()  # You can use Firefox or other browsers if needed
    driver.get("https://www.saucedemo.com/")  # Open the SauceDemo website
    driver.maximize_window()
    yield driver  # Yield the driver to be used in the tests
    driver.quit()  # Cleanup (close the browser) after test execution





#pytest --alluredir=E:/Automations_Folder/sauce_demo_test/Reports/allure-results
#allure generate E:/Automations_Folder/sauce_demo_test/Reports/allure-results --output E:/Automations_Folder/sauce_demo_test/Reports/allure-report

