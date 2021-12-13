from selenium.webdriver.common.by import By


class LoginPageLocators():
    TITLE = (By.CSS_SELECTOR, 'span[class="maintext"]')


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*LoginPageLocators.TITLE)
