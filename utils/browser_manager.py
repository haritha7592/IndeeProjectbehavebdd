from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BrowserManager:
    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-allow-origins=*")
        chrome_options.add_argument("--window-size=1920,1080")

        # Uncomment this only if Jenkins runs as a Windows Service
        # chrome_options.add_argument("--headless=new")

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )

        driver.implicitly_wait(10)

        return driver
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--disable-software-rasterizer")
        # chrome_options.add_argument("--disable-features=UseVideoOverlay,UseHardwareOverlays,HardwareMediaKeyHandling,MediaSessionService")
        # chrome_options.add_argument("--disable-accelerated-video-decode")
        # chrome_options.add_argument("--disable-accelerated-mjpeg-decode")

        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        # return driver
