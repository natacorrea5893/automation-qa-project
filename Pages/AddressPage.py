from selenium.webdriver.common.by import By


class AddressPageLocators():
    NEW_ADDRESS_BTN = (By.CSS_SELECTOR, 'a[title="New Address"]')

    SUCCESS_MSG = (By.CSS_SELECTOR, 'div.alert.alert-success')


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def getNewAddressBtn(self):
        return self.driver.find_element(*AddressPageLocators.NEW_ADDRESS_BTN)

    def getSuccessMsg(self):
        return self.driver.find_element(*AddressPageLocators.SUCCESS_MSG)
