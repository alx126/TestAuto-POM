from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = 'https://the-internet.herokuapp.com/login'

    FIELD_USERNAME = (By.ID, 'username')
    FIELD_PASSWORD = (By.ID, 'password')

    MESSAGE_ERROR = (By.CSS_SELECTOR, '#flash.error')
    MESSAGE_ERROR_TEXT = "Your username is invalid!\n×"

    USERNAME = 'tomsmith'
    PASSWORD = 'SuperSecretPassword!'
    WRONG_USERNAME = 'wrong_user'
    WRONG_PASSWORD = 'wrong_pass'

    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button.radius')
    BUTTON_CLOSE_MESSAGE = (By.CLASS_NAME, "close")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def get_message_error_text(self):
        return self.get_element_text(self.MESSAGE_ERROR)

    def insert_correct_username(self):
        self.type(self.FIELD_USERNAME, self.USERNAME)

    def insert_wrong_username(self):
        self.type(self.FIELD_USERNAME, self.WRONG_USERNAME)

    def insert_correct_password(self):
        self.type(self.FIELD_PASSWORD, self.PASSWORD)

    def insert_wrong_password(self):
        self.type(self.FIELD_PASSWORD, self.WRONG_PASSWORD)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def close_error_message(self):
        self.click(self.BUTTON_CLOSE_MESSAGE)

    def is_error_message_present(self):
        self.is_element_present(self.MESSAGE_ERROR)
    def is_error_message_displayed(self):
        self.is_element_displayed(self.MESSAGE_ERROR)

    def login_correct_credentials(self):
        self.driver.insert_correct_username()
        self.driver.insert_correct_password()
        self.driver.click_login_button()
        self.driver.implicitly_wait(2)




