import pytest
from pageObjects.LoginPage import LogIn


@pytest.mark.e2e
class TestInvalidCredentials:

    @pytest.mark.InvalidPassword
    def test_InvalidPassword(self):
        self.login = LogIn(self.driver)
        self.login.InvalidPassword()

    @pytest.mark.InvalidUsername
    def test_InvalidUsername(self):
        self.login = LogIn(self.driver)
        self.login.InvalidUsername()

    @pytest.mark.InvalidUsernameNPassword
    def test_InvalidUsernameNPassword(self):
        self.login = LogIn(self.driver)
        self.login.InvalidUsernameNPassword()

