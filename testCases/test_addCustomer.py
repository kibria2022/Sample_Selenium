import string
import random
import time
import pytest
from selenium.webdriver.common.by import By

# Calling LoginPage class from pageObjects- package
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    # getting these information from Config
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("***************** Test_003_AddCustomer *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** login in Successfully  *****************")

        self.logger.info("***************** Starting Add Customer Test  *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(1)
        self.addcust.clickOnbtnAddnew()
        time.sleep(2)
        self.logger.info("***************** Providing Customer information  *****************")
        self.email = self.random_email_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)

        time.sleep(2)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guest")

        time.sleep(2)
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Golam")
        self.addcust.setLastName("Kibria")
        self.addcust.setDateOfBirth("07/20/1995")
        self.addcust.setCompanyName("Ilham LLC")
        self.addcust.setAdminContent("This is Test Admin Content....")
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "addCustomer_info_scr.png")  # Screenshots
        self.addcust.clickOnSave()
        self.logger.info("***************** Saving Customer info Successfully  *****************")

        self.logger.info("***************** Add Customer Validation Started  *****************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        # self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_Done_scr.png") # Screenshots


        # print("The Actual Title is:", act_title)
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***************** Add Customer Test Passed  *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "addCustomer_screenshot.png") # Screenshots
            self.logger.error("***************** Add Customer Test failed  *****************")
            assert True == False

        self.driver.close()
        self.logger.error("***************** Ending Test_003_AdCustomer test *****************")



    # generate Random Emails character size=8 and lowercase and
    def random_email_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(8))



# Here Default browser is chrome: To run the test execute below on Terminal
# pytest -v --html=Reports\report.html testCases/test_addCustomer.py
# pytest -v --html=Reports\report.html testCases/test_addCustomer.py --browser firefox
# pytest -v --html=Reports\report.html testCases/test_addCustomer.py --browser opera
# pytest -v --html=Reports\report.html testCases/test_addCustomer.py --browser chrome
