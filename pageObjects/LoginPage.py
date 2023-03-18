import pytest
from selenium.webdriver.common.by import By
from resources.LoginData import LoginData, InvalidPassword, InvalidUsername, InvalidUsernameNPassword
from utilities.CustomLogger import CustomLogger


class LogIn:
    def __init__(self, driver):
        self.driver = driver

    log = CustomLogger.customLogger()

    def LogInFeature(self):
        assert self.driver.current_url == LoginData.url

        self.driver.find_element(By.CLASS_NAME, "username").send_keys(LoginData.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(LoginData.password)
        self.driver.find_element(By.CLASS_NAME, "button").click()

    def InvalidPassword(self):
        assert self.driver.current_url == InvalidPassword.url

        self.driver.find_element(By.CLASS_NAME, "username").send_keys(InvalidPassword.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(InvalidPassword.password)
        self.driver.find_element(By.CLASS_NAME, "button").click()
        errorMessage = self.driver.find_element(By.ID, "errorDiv").text

        assert errorMessage == "* Unable to validate your user account. Please note that both the username and password are case-sensitive."

    def InvalidUsername(self):
        assert self.driver.current_url == InvalidUsername.url

        self.driver.find_element(By.CLASS_NAME, "username").send_keys(InvalidUsername.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(InvalidUsername.password)
        self.driver.find_element(By.CLASS_NAME, "button").click()
        errorMessage = self.driver.find_element(By.ID, "errorDiv").text

        assert errorMessage == "* Unable to validate your user account. Please note that both the username and password are case-sensitive."

    def InvalidUsernameNPassword(self):
        assert self.driver.current_url == InvalidUsernameNPassword.url

        self.driver.find_element(By.CLASS_NAME, "username").send_keys(InvalidUsernameNPassword.username)
        self.driver.find_element(By.CLASS_NAME, "password").send_keys(InvalidUsernameNPassword.password)
        self.driver.find_element(By.CLASS_NAME, "button").click()
        errorMessage = self.driver.find_element(By.ID, "errorDiv").text

        assert errorMessage == "* Unable to validate your user account. Please note that both the username and password are case-sensitive."
