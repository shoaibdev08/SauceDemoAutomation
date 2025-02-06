import time

import pytest
from selenium.webdriver.common.by import By  # Importing By
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage


def test_add_to_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Log in with valid credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Add product to the cart
    inventory_page.add_to_cart()
    time.sleep(2)

    # Verify that the product is added to the cart
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text  # Use By.CLASS_NAME instead
    assert cart_count == "1"


