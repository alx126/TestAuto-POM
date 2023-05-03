from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    BASE_URL = 'https://the-internet.herokuapp.com/'

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    def wait_for_element_to_be_absent(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(expected_conditions.none_of(expected_conditions.presence_of_element_located(element_locator)))


