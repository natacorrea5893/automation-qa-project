from selenium.webdriver.common.by import By


class AccountPageLocators():
    TITLE = (By.CSS_SELECTOR, 'span[class="maintext"]')
    ADDRESS_BOOK_BTN = (By.CSS_SELECTOR, 'a[title="Manage Address Book"]')


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*AccountPageLocators.TITLE)

    def getAddressBookBtn(self):
        return self.driver.find_element(*AccountPageLocators.ADDRESS_BOOK_BTN)
