import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from resources.LoginData import LoginData


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="Chrome")


@pytest.fixture(autouse=True)
def browser(request):
    browser_name = request.config.getoption("browser")
    global driver
    if browser_name == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = LoginData.HEADLESS_BROWSER
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name == "Firefox":
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


@pytest.fixture(scope='session', autouse=True)
def setup():
    # Remove all files and directories in the folder
    folder_path = "./reports"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            os.rmdir(file_path)
        else:
            os.remove(file_path)


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
            destination_file = os.path.join(report_directory, file_name)
            # Take the actual screenshot
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
                report.extra = extra


def pytest_html_report_title(report):
    report.title = "LightningBolt Report"
