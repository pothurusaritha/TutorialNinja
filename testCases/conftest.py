import os.path

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from datetime import datetime
@pytest.fixture()
def setup(browser):
    if browser=='edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        print("Launching Edge browser........")
    elif browser=='firefox':
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options)
        print("Launching Firefox browser........")
    else:
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options)
        print("Launching Chrome browser........")
    yield driver
    driver.quit()
def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#It is hook for adding environment info to html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name']='TutorialNinja'
    config.stash[metadata_key]['Module Name'] = 'Customer Registration'
    config.stash[metadata_key]['Tester Name'] = 'Saritha'

#It is hook for delete/modify environmental info to HTML Report
@pytest.hookimpl(optionalhook=True)
# @pytest.mark.optionalhook  #Deprecated
def pytest_metada(metadata):
    metadata.pop("Python",None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=(os.path.dirname(os.getcwd()) + "\\TutorialsninjaProject\\reports\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html")