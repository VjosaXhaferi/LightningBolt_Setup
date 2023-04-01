from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    # Class constructor
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    def click_element(self, by_locator):
        try:
            WebDriverWait(self.driver, 50) \
                .until(EC.element_to_be_clickable(by_locator)) \
                .click()
        except WebDriverException as wd_exc:
            raise Exception(str("message") + 'Button: ', str(by_locator), 'was Not found in page!') from wd_exc

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 50) \
                .until(EC.visibility_of_element_located(by_locator)) \
                .clear()
            self.driver.find_element(*by_locator).send_keys(text)
        except TimeoutException as timeout:
            raise Exception(str("message") + 'Locator' + str(by_locator) + 'was NOT found in page') from timeout
