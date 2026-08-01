from utils.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.video_page import VideoPage
from utils.logger import LogGen
from utils.screenshot import Screenshot

log = LogGen.get_logger("Environment")

def before_all(context):
    log.info("Execution started")

def before_scenario(context, scenario):
    log.info(f"starting Scenario : {scenario.name}")
    context.driver = BrowserManager().get_driver()
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.load_login_page()
    context.login_page.enter_pin()
    context.login_page.submit()
    context.home_page = HomePage(context.driver)
    context.video_page = VideoPage(context.driver)

def before_step(context, step):
    log.info(f"Executing Step : {step.name}")

def after_step(context, step):
    if step.status == "failed":
        failure_screenshot = Screenshot(context.driver)
        failure_screenshot.take_screenshot(step.name.replace(" ", "_"))

def after_scenario(context, scenario):
    log.info(f"Finished Scenario : {scenario.name}")

    try:
        context.driver.quit()
    except Exception as e:
        # print(e)
        log.exception(e)

def after_all(context):
    log.info(f"Execution Finished")






        # os.makedirs("reports/screenshots", exist_ok = True)
        # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # file_name = f"{step.name}_ {timestamp}.png"
        # file_path = os.path.join("reports/screenshots", f"{file_name}.png")
        # # print(f"[ERROR] Step failed: {step.name}")
        # logger.error(f"{step.status}: {step.reason}")
        # # context.driver.save_screenshot(os.path.join("reports", "screenshots", file_name))
        # context.driver.save_screenshot(file_path)