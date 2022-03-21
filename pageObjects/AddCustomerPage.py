import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    textEmail_xpath = "//input[@id='Email']"
    textPassword_xpath = "//input[@id='Password']"
    textFirstName_xpath = "//input[@id='FirstName']"
    textLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    textGenderMale_xpath = "//input[@id='Gender_Male']"
    textGenderFemale_xpath = "//input[@id='Gender_Female']"
    textDateOfBirth_xpath = "//input[@id='DateOfBirth']"


    newsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap'][1]"
    # textCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap'][1]"
    textCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//input[@role='listbox']"
    listitemAdministrators_xpath = "//li[contains(text(), 'Administrator')]"
    listitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    listitemGuest_xpath = "//li[contains(text(), 'Guests')]"
    listitemVendor_xpath = "//li[contains(text(), 'Vendors')]"
    # drpmgrOfVendor_xpath = "//*[@id ='VendorId']"
    drpmgrOfVendor_ID = "VendorId"
    drpVendor1_xpath = "//option[normalize-space()='Vendor 1']"

    textCompanyName_xpath = "//input[@id= 'Company']"
    textAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        # self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath)
        self.driver.find_element_by_xpath (self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        # self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath)
        self.driver.find_element_by_xpath (self.lnkCustomers_menuitem_xpath).click()

    def clickOnbtnAddnew(self):
        # self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath)
        self.driver.find_element_by_xpath (self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.textEmail_xpath).send_keys(email)
        # self.driver.find_element_by_xpath (self.btnAddnew_xpath).click()

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.textCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemAdministrators_xpath)
        elif role == "Guest":
            # Here user Role can be Registered or Guest only one
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuest_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuest_xpath)
        time.sleep(3)
        # self.listitem.click();
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        vendor = self.driver.find_element(By.ID, self.drpmgrOfVendor_ID)
        ven = Select(vendor)
        ven.select_by_visible_text(value)


    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_id)
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdFemaleGender_id)
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_id)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.textFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.textLastName_xpath).send_keys(lastname)

    def setDateOfBirth(self,dob):
        self.driver.find_element(By.XPATH, self.textDateOfBirth_xpath).send_keys(dob)

    def setCompanyName(self,company):
        self.driver.find_element(By.XPATH, self.textCompanyName_xpath).send_keys(company)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.textAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    # character size=8 and lowercase and
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(8))

    # def random_char(char_num):
    #     return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# -------------------------------------------------------------------------------------------------
# To Generate Random Email
# import random
# import string
# domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
# letters = ["1", "2","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"  ]
#
# def get_one_random_domain(domains):
#         return domains[random.randint( 0, len(domains)-1)]
#
# def get_one_random_name(letters):
#     email_name = ""
#     for i in range(8):
#         email_name = email_name + letters[random.randint(0,11)]
#     return email_name
#
# def generate_random_emails():
#     for i in range(0,1):
#          one_name = str(get_one_random_name(letters))
#          one_domain = str(get_one_random_domain(domains))
#          print(one_name  + "@" + one_domain)
#
# def testemail():
#     generate_random_emails()

# -------------------------------------------------------------------------------------------------