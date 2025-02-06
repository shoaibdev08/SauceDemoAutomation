import time

import pytest

from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage


# Test case: Checkout flow

def test_checkout_flow(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Log in with valid credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Add product to the cart
    inventory_page.add_to_cart()

    # Proceed to checkout
    inventory_page.go_to_cart()
    cart_page.checkout()

    # Enter checkout details
    checkout_page.enter_checkout_details("Test1", "Test2", "112233")
    time.sleep(1)
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    # Verify order completion
    thank_you_message = checkout_page.get_thank_you_message()
    assert "Thank you for your order!" in thank_you_message
