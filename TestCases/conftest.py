from selenium import webdriver
import pytest

from TestCases.test_login_ddt import Test_002_DDT_Login

@pytest.fixture()
def setup():
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Firefox browser")
    driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# pytest html report
# it is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopcommerceapp'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'
# it is hook for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


