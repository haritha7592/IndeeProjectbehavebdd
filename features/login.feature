Feature: Login to Indee Demo Site

  Scenario: User logs in with valid PIN
    Given user launch the Indee demo site
    When user login with the valid PIN
    Then user should be on the All Titles screen
