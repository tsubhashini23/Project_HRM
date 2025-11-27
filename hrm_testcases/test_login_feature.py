# import time
import pytest
from conftest import *
from hrm_pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_setup")
class TestLogin:

    def setup_class(self):
        self.driver.get(base_url)
        self.login_page = LoginPage(self.driver)

    def test_validate_login(self):
        self.login_page.login(username, password)
        print("Successfully logged in")

    def teardown_class(self):
        # time.sleep(5)
        self.driver.quit()