from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecurePage(BasePage):
    SECURE_PAGE_URL = 'https://the-internet.herokuapp.com/secure'

    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '#flash.success')
    MESSAGE_SUCCESS_TEXT = "You logged into a secure area!\n×"

    BUTTON_LOGOUT = (By.CSS_SELECTOR, "i.icon-signout")
    BUTTON_CLOSE_MESSAGE = (By.CLASS_NAME, "close")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_secure_page(self):
        self.driver.get(self.SECURE_PAGE_URL)

    def get_message_success_text(self):
        return self.find(self.MESSAGE_SUCCESS).text

    def is_success_message_present(self):
        return self.is_element_present(self.MESSAGE_SUCCESS)

    def is_success_message_displayed(self):
        return self.is_element_displayed(self.MESSAGE_SUCCESS)

    def close_error_message(self):
        self.click(self.BUTTON_CLOSE_MESSAGE)

    def click_logout_button(self):
        self.click(self.BUTTON_LOGOUT)




