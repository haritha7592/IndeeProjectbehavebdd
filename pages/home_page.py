import os, json
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open(os.path.join("test_data", "credentials.json")) as f:
            self.cfg = json.load(f)

    def open_project(self):
        """ Clicks the 'Test automation project' on the page."""
        project = self.find((By.XPATH, "//img[@alt='Test automation project']"))
        self.js("arguments[0].scrollIntoView();", project)
        project.click()

    def logout(self):
        """Locate the sign-out element and clicked on it"""
        sidebar = self.find((By.ID, "SideBar"))
        self.js("arguments[0].scrollIntoView();", sidebar)
        signout_btn = self.find((By.XPATH, "//a[@id='signOutSideBar']//button"))
        self.js("arguments[0].click();", signout_btn)

        """removing this wait doesn't affect the run,just for pretty demo. """
        time.sleep(0.5)
