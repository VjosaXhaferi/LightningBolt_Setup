import pytest
from selenium.webdriver.common.by import By
from resources.LoginData import LoginData


class LogIn:
    def __init__(self, driver):
        self.driver = driver

    def LogInFeature(self):

        assert self.driver.current_url == LoginData.url

        self.driver.find_element(By.CLASS_NAME, "username").send_keys(LoginData.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(LoginData.password)
        self.driver.find_element(By.CLASS_NAME, "button").click()


