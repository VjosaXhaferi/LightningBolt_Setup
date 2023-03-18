import pytest

from pageObjects.DepartmentPage import NewDepartment
from pageObjects.LoginPage import LogIn


@pytest.mark.department
class TestAddDepartment:
    def test_LogInFeature(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.department = NewDepartment(self.driver)
        self.department.AddNewDepartment()
