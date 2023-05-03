import time
import unittest

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.driverfactory import DriverFactory


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.login_page = LoginPage(self.driver)
        self.secure_page = SecurePage(self.driver)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_correct_credentials(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.assertEqual(self.secure_page.SECURE_PAGE_URL, self.driver.current_url)
        self.assertTrue(self.secure_page.MESSAGE_SUCCESS)

    def test_login_no_credentials(self):
        self.login_page.navigate_to_login_page()
        self.login_page.click_login_button()
        time.sleep(1)
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_login_incorrect_credentials(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_wrong_username()
        self.login_page.insert_wrong_password()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_login_no_username(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_login_incorrect_username(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_wrong_username()
        self.login_page.insert_correct_password()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_login_no_password(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_login_incorrect_password(self):
        self.login_page.navigate_to_login_page()
        self.login_page.insert_correct_username()
        self.login_page.insert_wrong_password()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.MESSAGE_ERROR)

    def test_error_message_text(self):
        self.login_page.navigate_to_login_page()
        self.login_page.click_login_button()
        self.assertEqual(self.login_page.MESSAGE_ERROR_TEXT, self.login_page.get_element_text(self.login_page.MESSAGE_ERROR))

    def test_close_error_message(self):
        self.login_page.navigate_to_login_page()
        self.login_page.click_login_button()
        self.login_page.close_error_message()
        self.assertFalse(self.login_page.is_error_message_displayed())







