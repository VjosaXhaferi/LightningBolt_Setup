import pytest

from pageObjects.DepartmentPage import NewDepartment
from pageObjects.LoginPage import LogIn


@pytest.mark.e2e
class TestAddDepartment:

    @pytest.mark.AddNewDepartment
    def test_AddNewDepartment(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.department = NewDepartment(self.driver)
        self.department.AddNewDepartment()
