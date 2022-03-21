import pytest
import time
from selenium import webdriver
# Calling LoginPage class from pageObjects- package
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path= ".//TestData/LoginData.xlsx"
    # this logger will send message to the Log files
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*****************   Test_002_DDT_Login     *****************")
        self.logger.info("*****************    Verifying login DDT test    *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)  # create a instance lp = LoginPage()
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number or Rows in a Excel:", self.rows)

        lst_status = [] # Empty List variable
        for row in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, "Sheet1",row, 1)
            self.password = XLUtils.readData(self.path, "Sheet1",row, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1",row,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            # self.lp.setUserName(self.username)
            # self.lp.setPassword(self.password)
            # self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass") # append/add this pass status into this empty list lst_status = []
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT is Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT is Failed ***")
            self.driver.close()
            assert False

        self.logger.info("********   End of Login DDT Test   ******************")
        self.logger.info("***********    Compleate TC_LoginDDT_002 ******************")

# To Execut this DDT test type on Terminal
# C:\Selenium\Framwork>>  pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser Chrome
# OR C:\Selenium\Framwork>>  pytest -v --html=Reports\report.html testCases/test_login_ddt.py
# C:\Selenium\Framwork>>  pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser Firefox
# C:\Selenium\Framwork>>  pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser Opera

# pytest -v -s --html=Reports\report.html testCases/test_login.py
# pytest -s -v --html=Reports\report.html testCases/test_login.py
# pytest -s -v --html=Reports\report.html testCases/test_login_ddt.py
# pytest -v --html=Reports\report.html testCases/test_login.py
# pytest -v testCases/test_login.py
# pytest -s -v testCases/test_login.py
# pytest -m -s testCases/test_login.py
