from selenium.webdriver.common.by import By


class CartPage:
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def remove_item_from_cart(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
