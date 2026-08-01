import os, json
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import LogGen


class LoginPage(BasePage):
    PIN_INPUT = (By.ID, "pin")
    SIGNIN_BTN = (By.ID, "sign-in-button")
    # PIN_INPUT = (By.XPATH, "//div[@id='input-pin-container']")
    # SIGNIN_BTN = (By.XPATH, "//div[@id='button-sign-in-button-inner-container']")
    ALL_TITLES = (By.XPATH, "//*[text()=' All Titles ']")

    def __init__(self, driver):
        super().__init__(driver)
        self.log = LogGen.get_logger(self.__class__.__name__)
        with open(os.path.join("test_data", "credentials.json")) as f:
            self.cfg = json.load(f)

    def load_login_page(self):
        """Loads the login page URL."""
        self.driver.get(self.cfg["base_url"])

    def enter_pin(self):
        """Wait for PIN input field and enter the provided PIN."""
        self.find(self.PIN_INPUT).send_keys(self.cfg["pin"])
        # self.find(self.PIN_INPUT).send_keys("WVMVHWBS")

    def submit(self):
        """Clicks the submit button to login."""
        self.click(self.SIGNIN_BTN)
        # self.click((By.ID, "brd-01fvc8gs4sa9kjs8wxs6gnsn76"))

    def verify_login_success(self):
        """Verify login by checking for element present after login."""
        # return " All Titles " in self.driver.page_source

        # state = self.driver.execute_script("return document.readyState")
        # print(state)
        element = self.find(self.ALL_TITLES)
        self.save_screenshot("verify_login_success")
        return element.text.strip() == "All Titles"

    def is_login_page_displayed(self):
        return bool(self.driver.find_element(*self.PIN_INPUT))
