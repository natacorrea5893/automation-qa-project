import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage


# Constants
STORE_HOME = 'https://automationteststore.com/index.php?rt=account/login'


# Scenarios
scenarios('../features/Login.feature')


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('the Store webPage')
def go_login_page(browser):
    browser.get(STORE_HOME)


# When Steps
@when(parsers.parse('complete "{user}" and "{password}"'))
def login(browser, user, password):
    login_page = LoginPage(browser)

    login_page.getInputName().send_keys(user)
    login_page.getInputPassword().send_keys(password)
    login_page.getBtnLogin().click()
    print('Step: Complete user & password')


# Then Steps
@then(parsers.parse('Login correctly'))
def is_ok(browser):
    account_page = AccountPage(browser)

    assert account_page.getTitle().text == "MY ACCOUNT"
    print('Step: Login successfully - My Account Page is displayed.')
