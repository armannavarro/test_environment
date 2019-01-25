import datetime
import time
import string
import random
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Full_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #create a new chrome test session
        #set the webdriver exec path
        self.driver = webdriver.Chrome(executable_path='C:/Users/kenma/Downloads/chromedriver_win/chromedriver')
        self.driver.implicitly_wait(2)

        #navigate the web address
        self.driver.get("https://test.id.overwatchid.com/login")
        self.driver.implicitly_wait(2)

        self.driver.maximize_window()


    def test_1a_Add_API_Keys(self):
        #Invalid username
        self.driver.implicitly_wait(2)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.send_keys("narman@test.com")
        self.driver.implicitly_wait(2)
        self.loginbtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div[4]/input')
        self.loginbtn.click()
        self.driver.implicitly_wait(2)
        #Invalid Password
        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.send_keys("Invalid")
        #Login
        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        self.driver.implicitly_wait(2)
        self.invalidmessage = self.driver.find_element_by_tag_name('p')
        assert self.invalidmessage.text == 'Your login attempt was not successful.'
        if self.invalidmessage.text == u'Your login attempt was not successful.':
            print ("Invalid login Verified")

        self.driver.implicitly_wait(2)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.clear()
        self.user_name.send_keys("release@test.com")
        self.driver.implicitly_wait(2)

        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.clear()
        self.password.send_keys("R0cknit!")

        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        self.driver.implicitly_wait(2)
        self.testlogin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/connections-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.testlogin.text == 'Search All Connections'
        if self.testlogin.text == u'Search All Connections':
            print ("Valid login verified")
        #Go to admin tab
        self.driver.implicitly_wait(2)
        self.admintab  = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[2]/div[2]/ul/li[4]/a')
        self.driver.implicitly_wait(2)
        self.admintab.click()
        self.driver.implicitly_wait(2)

        self.testadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.driver.implicitly_wait(2)
        assert self.testadmin.text == 'Account Administration'
        if self.testadmin.text == u'Account Administration':
            print "Admin tab verified"
        #Go to Account Administration
        self.driver.implicitly_wait(2)
        self.accntadmin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span')
        self.driver.implicitly_wait(2)
        self.accntadmin.click()
        self.driver.implicitly_wait(2)
        #Go to API Keys
        self.api = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/admin-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-children/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/div/tree-node-content/span')
        self.api.click()
        self.driver.implicitly_wait(2)
        #Add api key button
        self.addapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/tapik-component/app-master-view/div[1]/div[2]/config-button-component/div/button')
        self.addapi.click()
        time.sleep(1)
        self.driver.implicitly_wait(2)

        #Assert if Add API Modal is present
        time.sleep(2)
        self.addapimodal = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[1]/h4')
        assert self.addapimodal.text == 'Add API Key'
        if self.addapimodal.text == u'Add API Key':
            print "Add API key with Default Expiration"
        #add api
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apiname = self.driver.find_element_by_xpath('//*[@id="inputName"]')
        apiname = 'Automated Test '.join(random.choice(string.ascii_lowercase) for _ in range (2))
        self.apiname.send_keys(apiname) #api name

        #Add api key description
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.desapi = self.driver.find_element_by_xpath('//*[@id="inputDescription"]')
        des = 'Description'
        self.desapi.send_keys(des) #api description

        #Add api key email
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apiemail = self.driver.find_element_by_xpath('//*[@id="inputEmail"]')
        apiemail = 'arman.navarro@teravibe.com'
        self.apiemail.send_keys(apiemail) #api email

        #select Role
        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.apirole = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[2]/app-master-dropdown/form/div/ng-select/div/div')
        self.apirole.click()
        self.driver.implicitly_wait(2)
        self.pickrole = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[2]/app-master-dropdown/form/div/ng-select/select-dropdown/div/div/ul/li[1]')
        self.pickrole.click()
        self.driver.implicitly_wait(2)

        #select user groups
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.apigroup = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[3]/app-master-dropdown/form/div/ng-select/div/div')
        self.apigroup.click()
        self.driver.implicitly_wait(2)
        self.picgroup = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[3]/app-master-dropdown/form/div/ng-select/select-dropdown/div/div/ul/li[1]')
        self.picgroup.click()

        #save_api
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.saveapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/update-tapik-modal-component/div/div/div/div[2]/tabset/div/tab/div/div[4]/div/confirm-cancel-component/div/button[1]')
        self.saveapi.click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
