# import allure
# from utils.self_healing import SelfHealingDriver
# from selenium.webdriver.common.by import By

# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.healer = SelfHealingDriver(driver)

#     @allure.step("Open login page")
#     def open(self):
#         self.driver.get("https://www.saucedemo.com/")

#     @allure.step("Enter username: {username}")
#     def enter_username(self, username):
#         self.driver.find_element("id", "user-name").send_keys(username)

#     @allure.step("Enter password")
#     def enter_password(self, password):
#         self.driver.find_element("id", "password").send_keys(password)

#     @allure.step("Click login button")
#     def click_login(self):
#         self.driver.find_element("id", "login-button").click()

#     @allure.step("Perform login")
#     def login(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()

import allure
from utils.self_healing import SelfHealingDriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.healer = SelfHealingDriver(driver)

    @allure.step("Open login page")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.healer.find_element([
            (By.ID, "username"),  
            (By.NAME, "username"),
            (By.XPATH, "//input[@placeholder='Username']")
        ]).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.healer.find_element([
            (By.ID, "password"),
            (By.NAME, "password")
        ]).send_keys(password)

    @allure.step("Click login button")
    def click_login(self):
        self.healer.find_element([
            (By.ID, "login-button"),
            (By.XPATH, "//input[@type='submit']")
        ]).click()

    @allure.step("Perform login")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()