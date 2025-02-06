from Pages.login_page import LoginPage


# Test case: Verify user login with valid credentials
def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Log in with valid credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    # Verify login success
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

