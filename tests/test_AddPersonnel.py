import pytest
from pageObjects.PersonnelPage import NewPersonnel
from pageObjects.LoginPage import LogIn


@pytest.mark.e2e
class TestAddPersonnel:

    @pytest.mark.AddNewPersonnel
    def test_AddNewPersonnel(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.personnel = NewPersonnel(self.driver)
        self.personnel.AddNewPersonnel()

