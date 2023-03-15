import os
import time
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

@pytest.fixture(autouse=True)
def browser(request):
    global driver
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
    driver.set_page_load_timeout(20)
    driver.get(LoginData.url)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://s2.usw2.qa.lightning-bolt.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            extra.append(pytest_html.extras.image(file_name, ''))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "LightningBolt Report"
