from behave import given, when, then

@given("user am on the All Titles screen")
def step_on_all_titles(context):
    # Verify that user on logout page  by checking presence of expected element
    assert "All Titles" in context.driver.page_source

@when("user logout")
def step_logout(context):
    # Locate the signout element and clicked on it
    context.home_page.logout()

@then("user should return to the login page")
def step_login_page(context):
    # Verifying after scucessful signout user enters to aagian login/base/home page
    assert context.login_page.is_login_page_displayed()