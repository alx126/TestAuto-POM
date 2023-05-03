from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    HOME_PAGE_URL = 'https://the-internet.herokuapp.com/'

    LINK_AB_TESTING = (By.XPATH, '//*[@id="content"]/ul/li[1]/a')
    LINK_FORM_AUTHENTICATION = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    LINK_FILE_DOWNLOAD = (By.XPATH, '//*[@id="content"]/ul/li[17]/a')
    LINK_FILE_UPLOAD = (By.XPATH, '//*[@id="content"]/ul/li[18]/a')
    LINK_SECURE_FILE_DOWNLOAD = (By.XPATH, '//*[@id="content"]/ul/li[37]/a')
    LINK_WYSIWYG_EDITOR = (By.XPATH, '//*[@id="content"]/ul/li[44]/a')

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)

    def select_ab_testing(self):
        self.click(self.LINK_AB_TESTING)

    def select_form_authentication(self):
        self.click(self.LINK_FORM_AUTHENTICATION)

    def select_file_download(self):
        self.click(self.LINK_FILE_DOWNLOAD)

    def select_file_upload(self):
        self.click(self.LINK_FILE_UPLOAD)

    def select_secure_file_download(self):
        self.click(self.LINK_SECURE_FILE_DOWNLOAD)

    def select_wysiwig_editor(self):
        self.click(self.LINK_WYSIWYG_EDITOR)