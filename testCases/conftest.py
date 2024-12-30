from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#Pytest html - report

#These are all the below details which will be added into the html report

"""def pytest_configure(config):
    config._metadata['Project Name'] = 'Practice Test Automation'
    config._metadta['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Ammu Sriram'
#This throws error"""

#These are all the below details which will be removed from the html report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

