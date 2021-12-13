import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
from Pages.AddressPage import AddressPage
from Pages.EditAddressPage import EditAddressPage
from selenium.webdriver.support.ui import Select


# Constants
STORE_HOME = 'https://automationteststore.com/index.php?rt=account/login'


# Scenarios
scenarios('../features/Login.feature')
scenarios('../features/AddressBook.feature')


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


@when(parsers.parse('click on "Manage Address Book"'))
def goto_address_book(browser):
    account_page = AccountPage(browser)

    account_page.getAddressBookBtn().click()
    print('Step: "Manage Address Book" button clicked')


@when(parsers.parse('click on "New Address"'))
def goto_address_book(browser):
    address_page = AddressPage(browser)

    address_page.getNewAddressBtn().click()
    print('Step: "New Address" button clicked')


@when(parsers.parse('complete "{first_name}", "{last_name}", "{address_1}", "{city}", "{region}", "{zip}", "{country}"'))
def complete_address_book_fields(browser, first_name, last_name, address_1, city, region, zip, country):
    edit_address_page = EditAddressPage(browser)

    edit_address_page.getFirstNameField().send_keys(first_name)
    edit_address_page.getLastNameField().send_keys(last_name)
    edit_address_page.getAddress1Field().send_keys(address_1)
    edit_address_page.getCityField().send_keys(city)

    edit_address_page.getZipField().send_keys(zip)

    country_filter = Select(edit_address_page.getCountryField())
    country_filter.select_by_visible_text(country)

    region_filter = Select(edit_address_page.getRegionField())
    region_filter.select_by_visible_text(region)

    print('Step: Fields completed')


@when(parsers.parse('click Continue button'))
def save_address(browser):
    edit_address_page = EditAddressPage(browser)

    edit_address_page.getContinueBtn().click()
    print('Step: Address saved')


# Then Steps
@then(parsers.parse('Login correctly'))
def login_ok(browser):
    account_page = AccountPage(browser)

    assert account_page.getTitle().text == "MY ACCOUNT"
    print('Step: Login successfully - My Account Page is displayed.')


@then(parsers.parse('I get an Incorrect Login message "{error_message}"'))
def login_fail(browser, error_message):
    login_page = LoginPage(browser)

    assert error_message in login_page.getLoginError().text
    print('Step: Login wrong - Login Error is displayed.')


@then(parsers.parse('new address is saved correctly'))
def saved_address_ok(browser):
    address_page = AddressPage(browser)

    assert 'Your address has been successfully inserted' in address_page.getSuccessMsg().text
    print('Step: Address saved correctly')
