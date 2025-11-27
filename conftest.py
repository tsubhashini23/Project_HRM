import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chr_options = Options()
    chr_service = Service(ChromeDriverManager().install())
    chr_options.add_argument("--start-maximized")
    chr_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chr_options
    )
    request.cls.driver = driver