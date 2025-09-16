Feature: Logout from Indee Demo Site

  Scenario: User logs out successfully
    Given user am on the All Titles screen
    When user logout
    Then user should return to the login page
