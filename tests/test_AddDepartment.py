from pageObjects.AddDepartment import NewDepartment
from pageObjects.LoginPage import LogIn


class TestAddDepartment:
    def test_LogInFeature(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()

    def test_AddNewDepartment(self):
        self.department = NewDepartment(self)
        self.department.AddNewDepartment()


