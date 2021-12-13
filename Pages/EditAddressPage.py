from selenium.webdriver.common.by import By


class EditAddressPageLocators():
    CONTINUE_BTN = (By.CSS_SELECTOR, 'button[title="Continue"]')

    FIRST_NAME = (By.ID, 'AddressFrm_firstname')
    LAST_NAME = (By.ID, 'AddressFrm_lastname')
    ADDRESS_1 = (By.ID, 'AddressFrm_address_1')
    CITY = (By.ID, 'AddressFrm_city')
    REGION = (By.ID, 'AddressFrm_zone_id')
    ZIP = (By.ID, 'AddressFrm_postcode')
    COUNTRY = (By.ID, 'AddressFrm_country_id')


class EditAddressPage:
    def __init__(self, driver):
        self.driver = driver

    def getContinueBtn(self):
        return self.driver.find_element(*EditAddressPageLocators.CONTINUE_BTN)

    def getFirstNameField(self):
        return self.driver.find_element(*EditAddressPageLocators.FIRST_NAME)

    def getLastNameField(self):
        return self.driver.find_element(*EditAddressPageLocators.LAST_NAME)

    def getAddress1Field(self):
        return self.driver.find_element(*EditAddressPageLocators.ADDRESS_1)

    def getCityField(self):
        return self.driver.find_element(*EditAddressPageLocators.CITY)

    def getRegionField(self):
        return self.driver.find_element(*EditAddressPageLocators.REGION)

    def getZipField(self):
        return self.driver.find_element(*EditAddressPageLocators.ZIP)

    def getCountryField(self):
        return self.driver.find_element(*EditAddressPageLocators.COUNTRY)
