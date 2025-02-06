import pytest
from selenium import webdriver

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function")
def setup():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()


    yield driver  # Yield the driver to be used in the tests
    driver.quit()  # Cleanup (close the browser) after test execution






