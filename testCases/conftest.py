import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime

@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Lauching Edge browser--")
        return driver

    elif browser=="firefox":
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching Firefox browser--")
        return driver

    else:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser--")
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

###Generating HTML report########
#Hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Prject Name']='AutomationTestingPractice'
    config._metadata['Module Name']='AccountCreation'


#Hook to delete/modify environment info for html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)


#Specifying report/folder directory
@pytest.mark.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+ "\\reports\\"+datetime.now().strftime("%d-%m-%y")+".html"





