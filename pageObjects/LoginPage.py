import pytest
from selenium.webdriver.common.by import By
from resources.LoginData import LoginData


#@pytest.mark.usefixtures("setup")
class LogIn:
    def LogInFeature(self):
        print("login")
        self.driver.get(LoginData.url)
        self.driver.find_element(By.CLASS_NAME, "username").send_keys(LoginData.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(LoginData.password)
