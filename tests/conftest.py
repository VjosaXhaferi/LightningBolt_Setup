import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from resources.LoginData import LoginData


# @pytest.fixture(scope="class")  # scope="class, it executes before the class where we are calling the fixture
# def setup():  # request is an instance by default for fixtures
#    service_obj = Service("/Users/vjosaxhaferi/Downloads/chromedriver_mac64/chromedriver.exe")
#    driver = webdriver.Chrome(service=service_obj)
#    driver.get("https://s2.usw2.qa.lightning-bolt.com/")
#    driver.maximize_window()
#    return driver

#@pytest.fixture(autouse=True, scope="function")
def browser(request):
    if LoginData.browser == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = LoginData.HEADLESS_BROWSER
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif LoginData.browser == "Firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = LoginData.HEADLESS_BROWSER
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.get(LoginData.url)
    request.cls.driver = driver
    yield
    driver.quit()