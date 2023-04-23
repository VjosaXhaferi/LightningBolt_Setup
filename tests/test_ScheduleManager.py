import pytest
from pageObjects.ScheduleManagerPage import ScheduleManager
from pageObjects.LoginPage import LogIn


@pytest.mark.e2e
class TestScheduleManager:

    @pytest.mark.manual
    def test_AddNewSchedule(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.schedule = ScheduleManager(self.driver)
        self.schedule.NewSchedule()

    @pytest.mark.autogeneranted
    def test_AutoGeneratedSchedule(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.schedule = ScheduleManager(self.driver)
        self.schedule.NewAutoGeneratedSchedule()
