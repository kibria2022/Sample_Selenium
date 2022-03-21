import pytest
import time
# Calling LoginPage class from pageObjects- package
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasswordL()
    # this logger will send message to the Log files
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("***************** Verifying Home Page Title *****************")
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************** Home Page Title is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("***************** Home Page Title is failed *****************")
            assert False

    @pytest.mark.function
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************** Verifying login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # here self.driver is a constractor parameter of LoginPage class
        self.lp = LoginPage(self.driver)  # create a instance lp = LoginPage()
        # use setUserName() method from LoginPage() class
        self.lp.setUserName(self.username)
        # use setPassword() method from LoginPage() class
        self.lp.setPassword(self.password)
        # use clickLogin() method from LoginPage() class
        self.lp.clickLogin()
        act_title = self.driver.title
        # print("The Actual Title is:", act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************** login test is passed  *****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            time.sleep(2)
            self.driver.close()
            self.logger.error("***************** login test is failed  *****************")
            assert False

# pytest -v -s testCases/test_login.py
# pytest -s -v testCases/test_login.py
# pytest -m -s testCases/test_login.py

# Here Default browser is chrome: To run the test execute below on Terminal
# pytest -v --html=Reports\report.html testCases/test_login.py
# pytest -v --html=Reports\report_firefox.html testCases/test_login.py --browser firefox
# pytest -v --html=Reports\report_opera.html testCases/test_login.py --browser opera
# pytest -v --html=Reports\report_chrome.html testCases/test_login.py --browser chrome

# to run spefic mark test cases sanity, regression
# pytest -v -m "function" --html=Reports\report.html testCases --browser firefox
# pytest -v -m "sanity" --html=Reports\report.html testCases --browser firefox
# pytest -v -m "regression" --html=Reports\report.html testCases --browser firefox
# pytest -v -m "sanity and regression" --html=Reports\report_firefox.html testCases --browser firefox
# pytest -v -m "sanity or regression" --html=Reports\report.html testCases --browser firefox

