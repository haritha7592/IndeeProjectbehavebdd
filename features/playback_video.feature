@skip_jenkins
Feature: Video Playback and Controls

  Scenario: Automate Indee video playback and controls
    When user navigate to the Test Automation Project
    And user switch to the Details tab and wait
    And user switch back to the Videos tab
    And user play the video
    And user wait 10 seconds and pause the video
    And user resume using Continue Watching
    And user set the volume to 50 percent
    And user change the resolution to 480p
    And user change the resolution to 720p
    And user pause the video and exit the project
    Then user should return to the All Titles screen
