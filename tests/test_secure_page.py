import time
import unittest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.driverfactory import DriverFactory


class TestSecurePage(unittest.TestCase):
    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.login_page = LoginPage(self.driver)
        self.secure_page = SecurePage(self.driver)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_navigate_to_secure_page(self):
        self.secure_page.navigate_to_secure_page()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_success_message_text(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.assertTrue(self.secure_page.is_success_message_displayed())
        self.assertEqual(self.secure_page.MESSAGE_SUCCESS_TEXT, self.secure_page.get_element_text(self.secure_page.MESSAGE_SUCCESS))

    def test_close_success_message(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.secure_page.close_error_message()
        time.sleep(1)
        self.assertFalse(self.secure_page.is_success_message_present())

    def test_logout(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.driver.implicitly_wait(2)
        self.secure_page.click_logout_button()
        self.assertIn("login", self.driver.current_url)



