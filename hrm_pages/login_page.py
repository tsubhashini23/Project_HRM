from hrm_helpermethods.action_methods import ActionMethods
from selenium.webdriver.common.by import By

class LoginPage(ActionMethods):

    email_element = (By.XPATH, '//input[@name="username"]')
    password_element = (By.XPATH, '//input[@name="password"]')
    login_button = (By.XPATH, '//button')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_valuein_webelement(self.email_element, username)
        self.enter_valuein_webelement(self.password_element, password)
        self.click_webelement(self.login_button)


