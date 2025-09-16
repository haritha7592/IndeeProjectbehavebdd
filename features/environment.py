from utils.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.video_page import VideoPage

def before_all(context):
    context.driver = BrowserManager().get_driver()
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
    context.video_page = VideoPage(context.driver)

def after_all(context):
    try:
        context.driver.quit()
    except:
        pass

def after_step(context, step):
    if step.status == "failed":
        print(f"[ERROR] Step failed: {step.name}")
        context.driver.save_screenshot(
            f"reports/screenshots/{step.name.replace(' ', '_')}_failed.png"
        )