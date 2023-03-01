from selenium.webdriver.common.by import By
from resources.Personnel import Personnel


class NewPersonnel:
    def __init__(self, driver):
        self.driver = driver

    def AddNewPersonnel(self):
        self.driver.find_element(By.LINK_TEXT, "Personnel").click()
        assert self.driver.current_url == Personnel.url

        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "addnew_button").click()
        self.driver.find_element(By.ID, "personnel_Last_Name").send_keys(Personnel.LastName)
        self.driver.find_element(By.ID, "personnel_First_Name").send_keys(Personnel.FirstName)
        displayName = Personnel.displayNameString
        self.driver.find_element(By.ID, "personnel_Display_Name").send_keys(displayName)
        self.driver.find_element(By.ID, "personnel_Compact_Name").send_keys(Personnel.CompactName)
        self.driver.find_element(By.XPATH, "//input[@class='orange-button right save_changes']").click()

        table = self.driver.find_element(By.ID, "personnel_grid")

        row = None
        for tr in table.find_elements(By.TAG_NAME, 'tr'):
            if displayName in tr.text:
                row = tr
                break

        # Assert that the item was added to the table
        assert row is not None, f"Item '{displayName}' not found in table"
