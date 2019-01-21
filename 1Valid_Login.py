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
        time.sleep(1)

    def test_1b_Log_in_with_Valid_Credentials(self):
        time.sleep(1)
        self.user_name = self.driver.find_element_by_id("j_username")
        self.user_name.clear()
        self.user_name.send_keys("release@test.com")
        time.sleep(1)

        self.password = self.driver.find_element_by_id("j_pwd")
        self.password.clear()
        self.password.send_keys("R0cknit!")

        self.login = self.driver.find_element_by_class_name("login-button")
        self.login.submit()

        time.sleep(1)
        self.testlogin = self.driver.find_element_by_xpath('/html/body/oid-app/my-app/div[3]/div[2]/connections-tree-component/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[2]/div/tree-node-wrapper/div/div/tree-node-content/span')
        assert self.testlogin.text == 'Search All Connections'
        if self.testlogin.text == u'Search All Connections':
            print "Verify valid login:"

if __name__ == '__main__':
    unittest.main(verbosity=2)
unittest.main()    
