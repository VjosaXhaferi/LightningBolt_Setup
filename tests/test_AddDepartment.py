from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LogIn
from resources.Department import Department


class TestLogingfeature:
    def test_LogInFeature(self):
        self.login = LogIn(self.driver)
        self.login.LogInFeature()

        self.driver.find_element(By.LINK_TEXT, "Departments").click()
        assert self.driver.current_url == Department.url

        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//input[@value='+ New Department']").click()
        self.driver.find_element(By.ID, "department_DeptName").send_keys(Department.departmentName)
        self.driver.find_element(By.ID, "NewTemplateName").send_keys(Department.templateName)
        self.driver.find_element(By.ID, "NewTemplateDescription").send_keys(Department.templateDescription)
        self.driver.find_element(By.ID, "add_button").click()
        self.driver.find_element(By.XPATH, "//input[@class='orange-button right save_changes']").click()

        #table = self.driver.find_element(By.XPATH, "//table[@id='departments']")


