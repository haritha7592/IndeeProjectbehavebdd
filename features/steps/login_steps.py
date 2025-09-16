from behave import given, when, then

@given("user launch the Indee demo site")
def step_launch_site(context):
    # Load the Indee demo login page
    context.login_page.load_login_page()

@when("user login with the valid PIN")
def step_login(context):
    # Enter the provided PIN and submit the login form
    context.login_page.enter_pin()
    context.login_page.submit()

@then("user should be on the All Titles screen")
def step_verify_login(context):
    # Verify that login was successful by checking presence of expected element
    assert context.login_page.verify_login_success(), "Login failed"
