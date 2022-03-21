from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchCustomer:
    # Add Customer Page
    textEmail_id = "SearchEmail"
    textFirstName_id = "SearchFirstName"
    textLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tableSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textEmail_id).clear()
        self.driver.find_element(By.ID, self.textEmail_id).send_keys(email)

    def setFirstName(self, firstName):
        self.driver.find_element(By.ID, self.textFirstName_id).clear()
        self.driver.find_element(By.ID, self.textFirstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.textLastName_id).clear()
        self.driver.find_element(By.ID, self.textLastName_id).send_keys(lastName)

    def clickOnSearchBtn(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH,
                                             "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == name:
                flag = True
                break
        return flag
