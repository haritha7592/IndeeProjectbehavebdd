from behave import given, when, then

@when("user navigate to the Test Automation Project")
def step_open_project(context):
    # locating and clicking the Test Automation Project element
    context.home_page.open_project()

@when("user switch to the Details tab and wait")
def step_details_tab(context):
    #  switching to details tab and explicitly wits for some time
    context.video_page.goto_details_tab_and_wait()

@when("user switch back to the Videos tab")
def step_videos_tab(context):
    # switch back to videos tab
    context.video_page.goto_videos_tab()

@when("user play the video")
def step_play_video(context):
    context.video_page.play_video()

@when("user wait 10 seconds and pause the video")
def step_pause_video(context):
    # Pause the video at exact time
    context.video_page.wait_and_pause()

@when("user resume using Continue Watching")
def step_continue(context):
    context.video_page.continue_watching()

@when("user set the volume to 50 percent")
def step_volume(context):
    # Decrease the volume to 50%
    context.video_page.set_volume_percent(50)

@when("user change the resolution to 480p")
def step_res480(context):
    # Change the resolution to 480p
    context.video_page.change_resolution_480p("480p")

@when("user change the resolution to 720p")
def step_res720(context):
    # Change the resolution to 720p
    context.video_page.change_resolution_720p("720p")

@when("user pause the video and exit the project")
def step_exit(context):
    context.video_page.pause_and_exit()

@then("user should return to the All Titles screen")
def step_back_titles(context):
    assert "All Titles" in context.driver.page_source
