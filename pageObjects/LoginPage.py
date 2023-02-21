import pytest
from selenium.webdriver.common.by import By
from resources.LoginData import LoginData


# @pytest.mark.usefixtures("setup")
class LogIn:
    def __init__(self, driver):
        self.driver = driver

    def LogInFeature(self, username, password):
        print("login")
        self.driver.find_element(By.CLASS_NAME, "username").send_keys(username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(password)
