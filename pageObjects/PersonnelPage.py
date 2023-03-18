import pytest
from selenium.webdriver.common.by import By
from resources.PersonnelData import Personnel
from sharedActions.SharedActions import MainPage
from utilities.CustomLogger import CustomLogger


class NewPersonnel(MainPage):
    def __init__(self, driver):
        self.driver = driver

    PERSONNEL_TAB = (By.LINK_TEXT, "Personnel")
    NEW_PERSONNEL_BUTTON = (By.ID, "addnew_button")
    FIRST_NAME = (By.ID, "personnel_First_Name")
    LAST_NAME = (By.ID, "personnel_Last_Name")
    DISPLAY_NAME = (By.ID, "personnel_Display_Name")
    COMPACT_NAME = (By.ID, "personnel_Compact_Name")
    SAVE_BUTTON = (By.XPATH, "//input[@class='orange-button save_changes']")

    log = CustomLogger.customLogger()

    def AddNewPersonnel(self):
        self.click_element(self.PERSONNEL_TAB)
        assert self.driver.current_url == Personnel.url

        self.driver.switch_to.frame(0)
        self.click_element(self.NEW_PERSONNEL_BUTTON)
        self.send_keys(self.LAST_NAME, Personnel.LastName)
        self.send_keys(self.FIRST_NAME, Personnel.FirstName)
        displayName = Personnel.DisplayName
        self.send_keys(self.DISPLAY_NAME, displayName)
        self.send_keys(self.COMPACT_NAME, Personnel.CompactName)
        self.click_element(self.SAVE_BUTTON)

        assert self.driver.current_url == Personnel.url

        table = self.driver.find_element(By.ID, "personnel_grid")

        row = None
        for tr in table.find_elements(By.TAG_NAME, 'tr'):
            if displayName in tr.text:
                row = tr
                break

        # Assert that the item was added to the table
        try:
            assert row is not None
        except AssertionError as err:
            self.log.exception(f"Personnel '{displayName}' was not found!")
            raise err
        else:
            self.log.info(f"Personnel '{displayName}' has been found!")
