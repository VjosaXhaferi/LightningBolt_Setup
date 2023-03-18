import pytest
from pageObjects.PersonnelPage import NewPersonnel
from pageObjects.LoginPage import LogIn


@pytest.mark.personnel
class TestAddPersonnel:

    def test_AddNewDepartment(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.personnel = NewPersonnel(self.driver)
        self.personnel.AddNewPersonnel()

