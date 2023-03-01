from selenium.webdriver.common.by import By
from resources.Department import Department


class NewDepartment:
    def __init__(self, driver):
        self.driver = driver

    def AddNewDepartment(self):

        self.driver.find_element(By.LINK_TEXT, "Departments").click()
        assert self.driver.current_url == Department.url

        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//input[@value='+ New Department']").click()
        new_department = Department.departmentName
        self.driver.find_element(By.ID, "department_DeptName").send_keys(new_department)
        self.driver.find_element(By.ID, "NewTemplateName").send_keys(Department.templateName)
        self.driver.find_element(By.ID, "NewTemplateDescription").send_keys(Department.templateDescription)
        self.driver.find_element(By.ID, "add_button").click()
        self.driver.find_element(By.XPATH, "//input[@class='orange-button right save_changes']").click()

        table = self.driver.find_element(By.XPATH, "//table[@id='departments']")

        row = None
        for tr in table.find_elements(By.TAG_NAME, 'tr'):
            if new_department in tr.text:
                row = tr
                break

        # Assert that the item was added to the table
        assert row is not None, f"Item '{new_department}' not found in table"
