from pageObjects.ScheduleManagerPage import ScheduleManager
from pageObjects.LoginPage import LogIn


class TestScheduleManager:

    def test_AddNewSchedule(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()
        self.schedule = ScheduleManager(self.driver)
        self.schedule.NewSchedule()
