import os
from datetime import datetime

# from webdriver_manager.core import driver

from utils.logger import LogGen

log = LogGen.get_logger(__name__)

class Screenshot:
    def __init__(self, driver, screenshot_dir="reports/screenshots"):
        self.driver = driver
        self.screenshot_dir = screenshot_dir
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def take_screenshot(self,name):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join(self.screenshot_dir, file_name)
        self.driver.save_screenshot(file_path)
        log.info(f'Screenshot saved to {file_path}')
        return file_path

# ss = Screenshot(driver)
<<<<<<< HEAD
# ss.take_screenshot("screenshot")
=======
# ss.take_screenshot("screenshot")
>>>>>>> b4fec5f24002fc095c1f7f04118be23f591b1319
