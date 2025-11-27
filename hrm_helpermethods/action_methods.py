from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionMethods:

    def __init__(self, driver):
        self.driver = driver

    def enter_valuein_webelement(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_webelement(self, locator):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()



