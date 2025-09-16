import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """ Waits for the element to be clickable, then clicks it.
    Args:
        locator (tuple): Locator of the element (By.ID, By.XPATH, etc.).
    Returns:
        WebElement: The clicked WebElement.   """
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def find(self, locator):
        """  Waits until the element is visible on the page and returns it.
         Args:
             locator (tuple): Locator of the element (By.ID, By.XPATH, etc.).
         Returns:
             WebElement: The visible WebElement.    """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def js(self, script, *args):
        """ Executes JavaScript code in the context of the current page.
        Args:
            script (str): The JavaScript code to execute.
            *args: Optional arguments to pass to the script.
        Returns:
            Any: The result of the JavaScript execution. """
        return self.driver.execute_script(script, *args)

    def save_screenshot(self, name):
        """ Saves a screenshot of the current browser window to the reports/screenshots directory.
        Args:
            name (str): The filename for the saved screenshot. """
        path = os.path.join("reports/screenshots", name)
        self.driver.save_screenshot(path)
        print(f"[INFO] Screenshot saved: {path}")