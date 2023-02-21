from pageObjects.LoginPage import LogIn


class testlogingfeature:
    def test_LogInFeature(self):
        self.loginpage = LogIn(self.driver)
        self.loginpage.LogInFeature()
