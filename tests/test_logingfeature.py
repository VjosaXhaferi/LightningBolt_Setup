from pageObjects.LoginPage import LogIn
from resources.LoginData import LoginData


class TestLogingfeature:
    def test_LogInFeature(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature(LoginData.username, LoginData.password)
