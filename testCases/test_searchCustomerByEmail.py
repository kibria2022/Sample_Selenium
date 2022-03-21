import time
import pytest
from selenium.webdriver.common.by import By

# Calling LoginPage class from pageObjects- package
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByEmail:
    # getting these information from Config
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************** Test_004_SearchCustomerByEmail *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** login in Successfully  *****************")

        self.logger.info("***************** SearchCustomerByEmail  *****************")

        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("*****************  Searching Customer By Email_ID  *****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        searchcust.clickOnSearchBtn()
        time.sleep(2)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*****************  TC_SearchCustomerByEmail_004 Finished  *****************")

        self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchCustomerByEmail_screenshot.png")  # Screenshots
        self.driver.close()

# Here Default browser is chrome: To run the test execute below on Terminal
# pytest -v --html=Reports\report.html testCases/test_searchCustomerByEmail.py
# pytest -v --html=Reports\report.html testCases/test_searchCustomerByEmail.py --browser firefox
# pytest -v --html=Reports\report.html testCases/test_searchCustomerByEmail.py --browser opera
# pytest -v --html=Reports\report.html testCases/test_searchCustomerByEmail.py --browser chrome
