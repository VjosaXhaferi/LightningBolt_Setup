from pageObjects.LoginPage import LogIn


class TestInvalidCredentials:

    def test_InvalidPassword(self):
        self.login = LogIn(self.driver)
        self.login.InvalidPassword()

    def test_InvalidUsername(self):
        self.login = LogIn(self.driver)
        self.login.InvalidUsername()

    def test_InvalidUsernameNPassword(self):
        self.login = LogIn(self.driver)
        self.login.InvalidUsernameNPassword()

