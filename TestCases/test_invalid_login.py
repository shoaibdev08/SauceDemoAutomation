import pytest

from Pages.login_page import LoginPage


# Test case: Verify user login with invalid credentials

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Log in with invalid credentials
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Verify error message
    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message