import time
from selenium.webdriver.common.by import By
from resources.ScheduleManagerData import ScheduleManagerData
from sharedActions.SharedActions import MainPage
from utilities.CustomLogger import CustomLogger


class ScheduleManager(MainPage):

    def __int__(self, driver):
        super().__init__(driver)

    ADMINISTRATION_SETUP_MENU = (By.ID, "miTopAdmin")
    SCHEDULE_MANAGER_TAB = (By.ID, "miConsole")
    DEPARTMENT_SELECTOR = (By.ID, "select2-departmentsSelect-container")
    DEPARTMENT_SEARCHBOX = (By.XPATH, "//input[@role='searchbox']")
    ADD_SCHEDULE_BUTTON = (By.CLASS_NAME, "lb-button")
    SCHEDULE_NAME = (By.ID, "txtScheduleName")
    TEMPLATE_SELECTOR = (By.XPATH, "//span[@class='select-wrapper single-select default-theme display-inline']//span["
                                   "@class='select-box']")
    CREATE_SAVE_BUTTON = (By.XPATH, "//a[normalize-space()='Create and Save']")
    OK_BUTTON = (By.XPATH, "//a[normalize-space()='Ok']")
    RADIO_BUTTON = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]")

    log = CustomLogger.customLogger()

    def NewSchedule(self):

        self.click_element(self.ADMINISTRATION_SETUP_MENU)
        self.click_element(self.SCHEDULE_MANAGER_TAB)

        assert self.driver.current_url == ScheduleManagerData.url

        self.click_element(self.DEPARTMENT_SELECTOR)
        self.send_keys(self.DEPARTMENT_SEARCHBOX, ScheduleManagerData.SearchDepartment)

        department_results = self.driver.find_elements(By.CLASS_NAME, "select2-results")

        if department_results is not None:
            for department in department_results:
                if department.text == ScheduleManagerData.SearchDepartment:
                    department.click()
                    break

        time.sleep(7)

        self.driver.switch_to.frame(0)
        self.click_element(self.ADD_SCHEDULE_BUTTON)
        schedule_name = ScheduleManagerData.ScheduleName
        self.send_keys(self.SCHEDULE_NAME, schedule_name)
        self.click_element(self.TEMPLATE_SELECTOR)

        template_results = self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'select-list-items')]/li")

        for template in template_results:
            if template.text == ScheduleManagerData.Template:
                template.click()
                break

        self.click_element(self.CREATE_SAVE_BUTTON)
        self.click_element(self.OK_BUTTON)
        time.sleep(7)

        schedule_table = self.driver.find_element(By.ID, "tablesorter")

        for tr in schedule_table.find_elements(By.TAG_NAME, 'tr'):
            if schedule_name in tr.text:
                tds = tr.find_elements(By.TAG_NAME, "td")
                tds[5].find_element(By.TAG_NAME, "a").click()
                break

        self.click_element(self.RADIO_BUTTON)
        self.click_element(self.OK_BUTTON)

        time.sleep(3)

        try:
            assert tds[5].text == "Published to Everyone"
        except AssertionError as err:
            self.log.exception("Status not updated!")
            raise err
        else:
            self.log.info("Status updated!")

