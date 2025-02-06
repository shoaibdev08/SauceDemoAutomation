import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage




def test_remove_from_cart(setup):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Log in with valid credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Add product to the cart
    inventory_page.add_to_cart()

    # Remove product from cart
    inventory_page.go_to_cart()
    cart_page.remove_item_from_cart()



    try:

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        print("Cart is empty.")
    except:
        print("Cart still has items or the badge is not found.")


    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge) == 0, "The cart badge still exists, meaning the cart is not empty."
    print("Test passed: Cart is empty.")

