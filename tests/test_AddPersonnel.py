from pageObjects.AddPersonnel import NewPersonnel
from pageObjects.LoginPage import LogIn


class TestAddPersonnel:

    def test_LogInFeature(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()

    def test_AddNewPersonnel(self):
        self.personnel = NewPersonnel(self.driver)
        self.personnel.AddNewPersonnel()

