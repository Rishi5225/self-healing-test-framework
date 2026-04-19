import allure
from pages.login_page import LoginPage

@allure.feature("Login Feature")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    # assert "inventory" in driver.current_url
    assert "inventory" in driver.current_url

    