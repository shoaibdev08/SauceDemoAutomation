import time

from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//*[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        time.sleep(1)
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(1)
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
        time.sleep(1)