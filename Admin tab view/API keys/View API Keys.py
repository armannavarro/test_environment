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


    def test_1a_View_API_Keys(self):
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
            print ("Verify invalid login:")

    def test_1b_Log_in_with_Valid_Credentials(self):
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
            print ("Verify valid login:")
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
            print "Admin Tab Present:"
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
    
        time.sleep(2)
        self.driver.implicitly_wait(2)
        self.viewapi = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[4]/div/tapik-component/app-master-view/div[1]/div[1]/h3')
        assert self.viewapi.text == 'API Keys'
        if self.viewapi.text == u'API Keys':
            print "Verify API Keys Can be viewed:"

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()
