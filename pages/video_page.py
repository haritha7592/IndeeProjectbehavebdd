import os, json, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class VideoPage(BasePage):
    # Locators for player iframe and video element
    PLAYER_IFRAME = (By.ID, "video_player")
    PLAYER = (By.TAG_NAME, "video")

    def __init__(self, driver):
        """ Initialize VideoPage with driver, config, and action chains. """
        super().__init__(driver)
        with open(os.path.join("test_data", "credentials.json")) as f:
            self.cfg = json.load(f)
        self.actions = ActionChains(driver)

    def hover_on_video(self):
        """Reusable helper to hover mouse over the video player area."""
        video_area = self.find((By.XPATH, "//div[contains(@class,'jw-media')]"))
        self.actions.move_to_element(video_area).perform()
        return video_area

    def goto_details_tab_and_wait(self):
        """
         Click the 'Details' tab and wait explicitly for 5 seconds as per assignment.
         """
        self.click((By.ID, "detailsSection"))
        time.sleep(5)  # assignment requires explicit wait
        print("✅ Switched to Details tab")

    def goto_videos_tab(self):
        """ Click the 'Videos' tab to switch back to the video list. """
        self.click((By.ID, "videosSection"))
        print("✅ Switched back to Videos tab")

    def play_video(self):
        """ Wait for the play button to be clickable, then click it to start video playback. """
        play_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='icon-width-gen wds-cursor-pointer']"))
        )
        play_btn.click()
        print("▶️ Video started playing")

    def wait_and_pause(self, seconds=10, hold_pause_seconds=5):
        """ Wait until video plays for 'seconds', then pause and hold for 'hold_pause_seconds'.
          Args:
            seconds (int): Time to wait before pausing the video.
            hold_pause_seconds (int): Time to keep the video paused.   """

        # Switch into iframe only when controlling the video
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.PLAYER_IFRAME))
        video = self.find(self.PLAYER)

        # Wait until current playback time reaches specified 'seconds'
        while True:
            current_time = self.js("return arguments[0].currentTime;", video)
            if current_time and float(current_time) >= seconds:
                break
            # time.sleep(0.25)  # small polling delay

        # Pause at N seconds
        self.js("arguments[0].pause();", video)
        print(f"⏸ Paused at ~{seconds} seconds of video playback")

        # Keep paused for hold_pause_seconds
        time.sleep(hold_pause_seconds)
        print(f"⏳ Stayed paused for {hold_pause_seconds} seconds")

    def continue_watching(self):
        """ Resume video playback by using JS to call play().    """
        video = self.find(self.PLAYER)
        self.js("arguments[0].play();", video)
        print("▶️ Resumed playback via JS after 5sces")
        # time.sleep(3) # removing this wait doesn't affect the run,just for a pretty demo

    def set_volume_percent(self, pct):
        """ Set video volume to a percentage value (0 to 100).
        Args:
            pct (int): Volume percentage to set. """
        video = self.find(self.PLAYER)
        try:
            self.js("arguments[0].volume = arguments[1];", video, pct / 100)
            print(f"🔊 Volume set to {pct}%")
            # Hover over volume button to visually confirm change
            volume_btn = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'jw-icon-volume')]")))
            self.actions.move_to_element(volume_btn).pause(2).perform()
            print("🖱 Hovered over volume button to verify change")
        except Exception as e:
            print(f'Setting volume failed: {e}')

    def change_resolution_480p(self, label):
        """ Change video resolution to 480p.
        Args:
            label (str): Label of the resolution option '480p'. """
        self.hover_on_video()
        settings_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'jw-icon-settings')]"))
        )
        self.js("arguments[0].click();", settings_btn)
        res = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(),'{label}')]"))
        )
        res.click()
        print(f"📺 Resolution switched to {label}")
        # time.sleep(2)  # removing this wait doesn't affect the run,just for a pretty demo

    def change_resolution_720p(self, label):
        """ Change video resolution to 480p.
        Args:
            label (str): Label of the resolution option '720p'. """
        self.hover_on_video()
        settings_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'jw-icon-settings')]"))
        )
        self.js("arguments[0].click();", settings_btn)
        res = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(),'{label}')]"))
        )
        res.click()
        print(f"📺 Resolution switched to {label}")
        self.actions.move_to_element(settings_btn).pause(2).perform()
        self.js("arguments[0].click();", settings_btn)
        # time.sleep(1) #  removing this wait doesn't affect the run,just for a pretty demo

    def pause_and_exit(self):
        """ Pause video playback and navigate back to the All Titles page. """
        self.hover_on_video()
        video = self.find(self.PLAYER)
        self.js("arguments[0].pause();", video)
        print("⏸ Video paused before exit")
        time.sleep(1) #  removing this wait doesn't affect the run,just for a pretty demo

        self.driver.switch_to.default_content()
        self.driver.back()
        print("⬅️ Navigated back to All Titles")
        time.sleep(1) #  removing this wait doesn't affect the run,just for a pretty demo
