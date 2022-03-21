import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#---------------------------- working fine --------------------------------------
# @pytest.fixture()
# def setup():
#     # driver = webdriver.Chrome()
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     return driver
#------------------------------------------------------------------------
@pytest.fixture()
def setup(browser):
    if browser == "Firefox":
        # driver = webdriver.Firefox()
        # driver = webdriver.Firefox(r'C:\Users\kibri\drivers\geckodriver.exe')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Lunching Firefox Browser")
    elif browser == "Edge":
        driver = webdriver.Edge(r'C:\Users\kibri\drivers\msedgedriver.exe')
        print("Lunching Edge Browser ")

    elif browser == "Opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print("Lunching Edge Browser ")

    else:
        driver = webdriver.Chrome(r'C:\Users\kibri\drivers\chromedriver.exe')
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Lunching Chrome Default Browser")
    return driver

def pytest_addoption(parser): # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

################    PyTest HTML Report    ##########################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Login"
    config._metadata["Tester Name"] = "Golam Kibria"
    config._metadata['Package'] = "python"


# It is hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def ptyest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




# To Generate html=Reports in to Reports folder
# pytest -s -v --html=Reports\report.html testCases/test_login.py --browser Chrome










# Not Working--> -n=2 define number of test cases run parallel
# pytest -s -v -n=2 testCases/test_login.py --browser Opera
# pytest -s -v -n=2 testCases/test_login.py --browser Chrome
# pytest -s -v -n=2 testCases/test_login.py --browser Firefox
# pytest -s -v -n=2 testCases/test_login.py --browser Edge

