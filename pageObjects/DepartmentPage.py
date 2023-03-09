from selenium.webdriver.common.by import By
from resources.DepartmentData import Department
from sharedActions.SharedActions import MainPage
from utilities.CustomLogger import CustomLogger


class NewDepartment(MainPage):

    def __int__(self, driver):
        super().__init__(driver)

    DEPARTMENTS_TAB = (By.XPATH, "//a[contains(.,'Departments')]")
    NEW_DEPARTMENTS_BUTTON = (By.XPATH, "//input[@value='+ New Department']")
    DEPARTMENT_NAME = (By.ID, "department_DeptName")
    TEMPLATE_NAME = (By.ID, "NewTemplateName")
    TEMPLATE_DESCRIPTION = (By.ID, "NewTemplateDescription")
    ADD_TEMPLATE = (By.ID, "add_button")
    SAVE_BUTTON = (By.XPATH, "//input[@class='orange-button right save_changes']")

    log = CustomLogger.customLogger()

    def AddNewDepartment(self):

        self.click_element(self.DEPARTMENTS_TAB)
        assert self.driver.current_url == Department.url

        self.driver.switch_to.frame(0)
        self.click_element(self.NEW_DEPARTMENTS_BUTTON)
        new_department = Department.departmentName
        self.send_keys(self.DEPARTMENT_NAME, new_department)
        self.send_keys(self.TEMPLATE_NAME, Department.templateName)
        self.send_keys(self.TEMPLATE_DESCRIPTION, Department.templateDescription)
        self.click_element(self.ADD_TEMPLATE)
        self.click_element(self.SAVE_BUTTON)

        table = self.driver.find_element(By.XPATH, "//table[@id='departments']")

        row = None
        for tr in table.find_elements(By.TAG_NAME, 'tr'):
            if new_department in tr.text:
                row = tr
                self.log.info("Department has been found!")
                break

        # Assert that the item was added to the table
        assert row is not None, f"Item '{new_department}' not found in table"
