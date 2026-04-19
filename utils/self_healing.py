import allure
from selenium.common.exceptions import NoSuchElementException

class SelfHealingDriver:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_list):
        for by, value in by_list:
            try:
                message = f"Trying locator: {by}={value}"
                print(message)
                allure.attach(message, name="Locator Attempt")

                element = self.driver.find_element(by, value)

                success_msg = f"SUCCESS with locator: {by}={value}"
                print(success_msg)
                allure.attach(success_msg, name="Locator Success")

                return element

            except NoSuchElementException:
                fail_msg = f"FAILED locator: {by}={value}"
                print(fail_msg)
                allure.attach(fail_msg, name="Locator Failed")

        raise Exception("All locators failed!")